#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
定时下载启动脚本
直接启动定时下载功能，无需手动交互
"""

import asyncio
import sys
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from src.application.TikTokDownloader import TikTokDownloader


async def main():
    """启动定时下载器"""
    async with TikTokDownloader() as app:
        try:
            # 检查免责声明
            if not await app.disclaimer():
                print("未接受免责声明，程序退出。")
                return
            
            # 初始化配置和设置
            app.check_config()
            await app.check_settings(restart=False)
            
            # 启动定时下载器
            if app.scheduler:
                print("正在启动定时下载任务...")
                app.scheduler.start_scheduler()
                
                # 显示定时任务状态
                status = app.scheduler.get_status()
                print(status)
                print("\n按 Ctrl+C 停止定时任务")
                
                # 保持程序运行
                try:
                    while app.scheduler.running:
                        await asyncio.sleep(60)  # 每分钟检查一次
                        # 可以在这里添加状态检查或日志输出
                        
                except KeyboardInterrupt:
                    print("\n正在停止定时任务...")
                    app.scheduler.stop_scheduler()
                    print("定时任务已停止。")
            else:
                print("定时下载器初始化失败！")
                
        except Exception as e:
            print(f"启动失败: {e}")
            import traceback
            traceback.print_exc()
            if app.scheduler and app.scheduler.running:
                app.scheduler.stop_scheduler()


if __name__ == "__main__":
    asyncio.run(main())