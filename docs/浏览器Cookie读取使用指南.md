# 浏览器Cookie读取使用指南

## 概述

本项目支持从多种浏览器自动读取Cookie，无需手动复制粘贴。这个功能基于 `rookiepy` 库实现，可以大大简化Cookie获取过程。

## 支持的浏览器

### Windows平台
- Chrome
- Chromium
- Opera
- Opera GX
- Edge
- Firefox
- Internet Explorer
- Safari

### macOS平台
- Chrome
- Chromium
- Opera
- Opera GX
- Edge
- Firefox
- Safari

### Linux平台
- Chrome
- Chromium
- Opera
- Firefox

## 使用方法

### 方法一：通过主程序界面

1. 启动主程序 `python main.py`
2. 进入「程序设置」菜单
3. 选择「Cookie设置」
4. 选择「从浏览器读取Cookie」
5. 从列表中选择你要读取的浏览器（如Firefox）
6. 程序会自动读取并保存Cookie

### 方法二：通过终端交互模式

1. 启动终端交互模式
2. 在Cookie相关设置中选择从浏览器读取
3. 选择目标浏览器
4. 系统自动完成读取和保存

## Cookie保存位置

读取到的Cookie会保存在以下位置：

### 配置文件位置
- **主配置文件**: `settings.json`
- **Cookie字段**: 
  - `cookie` - 抖音Cookie
  - `cookie_tiktok` - TikTok Cookie

### 具体保存格式

```json
{
    "cookie": "从浏览器读取的抖音Cookie字符串",
    "cookie_tiktok": "从浏览器读取的TikTok Cookie字符串"
}
```

## 注意事项

### 使用前准备
1. **关闭目标浏览器**: 读取Cookie前必须完全关闭要读取的浏览器
2. **确保登录状态**: 在浏览器中先登录抖音/TikTok账号
3. **权限要求**: 确保程序有读取浏览器数据的权限

### Firefox特殊说明
- Firefox使用独立的Cookie存储机制
- 需要确保Firefox完全关闭（包括后台进程）
- 如果读取失败，可以尝试重启Firefox后重新登录

### 安全提醒
- Cookie包含敏感的登录信息，请妥善保管配置文件
- 不要将包含Cookie的配置文件分享给他人
- 定期更新Cookie以保持有效性

## 故障排除

### 常见问题

1. **读取失败**
   - 确认浏览器已完全关闭
   - 检查是否已登录目标网站
   - 尝试重新登录后再读取

2. **Cookie无效**
   - Cookie可能已过期，需要重新登录
   - 检查网站是否有安全策略更新
   - 尝试清除浏览器缓存后重新登录

3. **权限问题**
   - 在macOS上可能需要授予程序访问权限
   - 在Windows上确保以管理员权限运行（如需要）

### 技术实现

项目使用 `src/tools/browser.py` 中的 `Browser` 类实现浏览器Cookie读取功能：

- **核心库**: `rookiepy`
- **支持格式**: 自动转换为项目所需的Cookie格式
- **错误处理**: 包含完整的异常处理机制
- **平台适配**: 自动检测操作系统并适配相应的浏览器路径

## 更新日志

- 支持主流浏览器的Cookie自动读取
- 跨平台兼容（Windows、macOS、Linux）
- 集成到主程序和终端交互模式
- 提供完整的错误处理和用户提示

---

*最后更新时间: 2024年*