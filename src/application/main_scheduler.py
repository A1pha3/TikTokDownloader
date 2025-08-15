from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import asyncio
from datetime import datetime
from typing import TYPE_CHECKING, List, Tuple
from ..translation import _

if TYPE_CHECKING:
    from ..config import Parameter
    from ..manager import Database
    from .main_terminal import TikTok

__all__ = ["ScheduledDownloader"]


class ScheduledDownloader:
    """定时下载器类，用于管理定时下载任务"""
    
    def __init__(self, parameter: "Parameter", database: "Database"):
        self.parameter = parameter
        self.database = database
        self.console = parameter.console
        self.logger = parameter.logger
        self.scheduler = AsyncIOScheduler()
        self.running = False
        
        # 默认执行时间：凌晨2点、中午12点、下午7点
        self.schedule_times = [(2, 0), (12, 0), (19, 0)]
        
    def start_scheduler(self):
        """启动定时下载器"""
        if self.running:
            self.console.warning(_("定时下载器已在运行中！"))
            return
            
        try:
            # 清除所有现有任务
            self.scheduler.remove_all_jobs()
            
            # 为每个时间点添加定时任务
            for i, (hour, minute) in enumerate(self.schedule_times):
                trigger = CronTrigger(hour=hour, minute=minute)
                self.scheduler.add_job(
                    self._execute_download_tasks,
                    trigger=trigger,
                    id=f"download_task_{i}",
                    name=f"定时下载任务 {hour:02d}:{minute:02d}"
                )
            
            # 启动调度器
            self.scheduler.start()
            self.running = True
            
            time_str = ", ".join([f"{h:02d}:{m:02d}" for h, m in self.schedule_times])
            self.console.print(
                _("定时下载器已启动，将在每天 {times} 执行下载任务").format(times=time_str),
                style="green"
            )
            
        except Exception as e:
            self.logger.error(_("启动定时下载器失败: {error}").format(error=str(e)))
            self.console.warning(_("启动定时下载器失败: {error}").format(error=str(e)))
            
    def stop_scheduler(self):
        """停止定时下载器"""
        if not self.running:
            self.console.warning(_("定时下载器未在运行！"))
            return
            
        try:
            self.scheduler.shutdown(wait=False)
            self.running = False
            self.console.print(_("定时下载器已停止"), style="yellow")
        except Exception as e:
            self.logger.error(_("停止定时下载器失败: {error}").format(error=str(e)))
            
    async def _execute_download_tasks(self):
        """执行异步下载任务"""
        try:
            self.console.print(
                _("开始执行定时下载任务 - {time}").format(
                    time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ),
                style="blue"
            )
            
            from .main_terminal import TikTok
            
            # 创建TikTok实例
            tiktok = TikTok(self.parameter, self.database)
            
            # 1. 批量下载账号作品
            if self.parameter.accounts_urls:
                self.console.print(_("正在执行：批量下载账号作品"), style="cyan")
                await tiktok.account_detail_batch()
                
            # 2. 批量下载合集作品
            if self.parameter.mix_urls:
                self.console.print(_("正在执行：批量下载合集作品"), style="cyan")
                await tiktok.mix_batch()
                
            # 3. 批量下载收藏作品
            if self.parameter.owner_url:
                self.console.print(_("正在执行：批量下载收藏作品"), style="cyan")
                await tiktok.collection_interactive()
                
            self.console.print(_("定时下载任务执行完成"), style="green")
            
        except Exception as e:
            self.logger.error(_("定时下载任务执行失败: {error}").format(error=str(e)))
            self.console.warning(_("定时下载任务执行失败: {error}").format(error=str(e)))
            
    def get_status(self) -> str:
        """获取定时器状态"""
        if self.running:
            time_str = ", ".join([f"{h:02d}:{m:02d}" for h, m in self.schedule_times])
            jobs_info = []
            for job in self.scheduler.get_jobs():
                next_run = job.next_run_time
                if next_run:
                    jobs_info.append(f"  - {job.name}: {next_run.strftime('%Y-%m-%d %H:%M:%S')}")
            
            status = _("定时下载器正在运行\n执行时间: 每天 {times}").format(times=time_str)
            if jobs_info:
                status += "\n" + _("下次执行:") + "\n" + "\n".join(jobs_info)
            return status
        else:
            return _("定时下载器未运行")
            
    def set_custom_times(self, times: List[Tuple[int, int]]):
        """设置自定义执行时间列表"""
        for hour, minute in times:
            if not (0 <= hour <= 23) or not (0 <= minute <= 59):
                raise ValueError(_("时间格式错误：小时应在0-23之间，分钟应在0-59之间"))
                
        self.schedule_times = times
        
        # 如果调度器正在运行，重新启动以应用新时间
        if self.running:
            self.stop_scheduler()
            self.start_scheduler()
        else:
            time_str = ", ".join([f"{h:02d}:{m:02d}" for h, m in times])
            self.console.print(
                _("执行时间已设置为: {times}").format(times=time_str),
                style="green"
            )
            
    def add_custom_time(self, hour: int, minute: int):
        """添加一个自定义执行时间"""
        if not (0 <= hour <= 23) or not (0 <= minute <= 59):
            raise ValueError(_("时间格式错误：小时应在0-23之间，分钟应在0-59之间"))
            
        if (hour, minute) not in self.schedule_times:
            self.schedule_times.append((hour, minute))
            self.schedule_times.sort()  # 按时间排序
            
            # 如果调度器正在运行，重新启动以应用新时间
            if self.running:
                self.stop_scheduler()
                self.start_scheduler()
            else:
                self.console.print(
                    _("已添加执行时间: {time}").format(time=f"{hour:02d}:{minute:02d}"),
                    style="green"
                )
        else:
            self.console.warning(_("该时间点已存在: {time}").format(time=f"{hour:02d}:{minute:02d}"))
            
    def remove_custom_time(self, hour: int, minute: int):
        """移除一个自定义执行时间"""
        if (hour, minute) in self.schedule_times:
            self.schedule_times.remove((hour, minute))
            
            # 如果调度器正在运行，重新启动以应用新时间
            if self.running:
                self.stop_scheduler()
                if self.schedule_times:  # 如果还有时间点，重新启动
                    self.start_scheduler()
            
            self.console.print(
                _("已移除执行时间: {time}").format(time=f"{hour:02d}:{minute:02d}"),
                style="yellow"
            )
        else:
            self.console.warning(_("该时间点不存在: {time}").format(time=f"{hour:02d}:{minute:02d}"))
            
    def set_custom_time(self, hour: int, minute: int = 0):
        """设置自定义执行时间（保持向后兼容）"""
        self.set_custom_times([(hour, minute)])