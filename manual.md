# TikTokDownloader 配置参数详细说明手册

## 📖 目录
1. [基础配置](#基础配置)
2. [URL配置](#url配置)
3. [文件存储配置](#文件存储配置)
4. [下载配置](#下载配置)
5. [网络配置](#网络配置)
6. [平台配置](#平台配置)
7. [高级配置](#高级配置)
8. [配置示例](#配置示例)
9. [常见问题](#常见问题)

---

## 基础配置

### 🔧 配置文件位置
- **文件路径**: `settings.json`（位于程序根目录）
- **格式**: JSON格式
- **编码**: UTF-8
- **修改后**: 需要重启程序才能生效

---

## URL配置

### 📱 accounts_urls (抖音账号批量下载配置)
**功能**: 配置需要批量下载的抖音账号列表
**类型**: 数组对象
**默认值**: 空配置

```json
"accounts_urls": [
    {
        "mark": "大浩哥",           // 账号标识（自定义名称）
        "url": "https://www.douyin.com/user/MS4wLjABAAAA...",  // 账号主页链接
        "tab": "post",             // 下载类型：post(作品)/like(喜欢)/collect(收藏)
        "earliest": "2024-01-01",  // 最早日期（可选）
        "latest": "2024-12-31",    // 最晚日期（可选，不设置则默认到当前时间为止，包含最新的全部内容）
        "enable": true             // 是否启用此配置
    }
]
```

**参数说明**:
- `mark`: 账号的自定义标识，用于文件命名和区分
- `url`: 抖音账号主页完整链接
- `tab`: 下载内容类型
  - `post`: 下载该账号发布的作品
  - `like`: 下载该账号点赞的作品
  - `collect`: 下载该账号收藏的作品
- `earliest`/`latest`: 时间范围过滤，格式：`YYYY-MM-DD`
- `enable`: 控制是否启用此账号的下载

### 🌍 accounts_urls_tiktok (TikTok账号批量下载配置)
**功能**: 配置需要批量下载的TikTok账号列表
**格式**: 与 `accounts_urls` 相同

### 📂 mix_urls (抖音合集批量下载配置)
**功能**: 配置需要批量下载的抖音合集/话题列表

```json
"mix_urls": [
    {
        "mark": "搞笑合集",        // 合集标识
        "url": "https://www.douyin.com/collection/...",  // 合集链接
        "enable": true            // 是否启用
    }
]
```

### 🌍 mix_urls_tiktok (TikTok合集批量下载配置)
**功能**: 配置需要批量下载的TikTok合集列表
**格式**: 与 `mix_urls` 相同

### 👤 owner_url (当前登录账号信息)
**功能**: 存储当前Cookie对应的账号信息

```json
"owner_url": {
    "mark": "我的账号",         // 账号标识
    "url": "https://www.douyin.com/user/...",  // 账号主页
    "uid": "123456789",        // 用户ID
    "sec_uid": "MS4wLjABAAAA...",  // 安全用户ID
    "nickname": "用户昵称"      // 账号昵称
}
```

---

## 文件存储配置

### 📁 root (根目录路径)
**功能**: 设置文件下载的根目录
**类型**: 字符串
**默认值**: 空（使用程序目录）

```json
"root": "/Users/username/Downloads/TikTok"  // macOS/Linux
"root": "D:\\Downloads\\TikTok"             // Windows
```

**注意事项**:
- 路径必须存在且有写入权限
- Windows系统使用双反斜杠 `\\` 或单正斜杠 `/`
- 留空则使用程序所在目录

### 📂 folder_name (文件夹名称)
**功能**: 设置下载文件的存储文件夹名称
**类型**: 字符串
**默认值**: `"Download"`

```json
"folder_name": "douyin"      // 所有文件存储在 douyin 文件夹内
"folder_name": "我的下载"     // 支持中文名称
```

**⚠️ 重要说明**: `folder_name` 参数**仅在单个作品下载时使用**，批量下载时会被忽略！

### 📁 批量下载文件夹命名规则
**功能**: 批量下载账号作品时，程序会自动生成包含UID和账号名的文件夹
**触发条件**: 使用 `accounts_urls` 或 `mix_urls` 进行批量下载时

#### 🏷️ 账号作品文件夹命名规则
1. **发布作品**: `UID{账号ID}_{账号名}_发布作品`
2. **喜欢作品**: `UID{账号ID}_{账号名}_喜欢作品`
3. **收藏作品**: `UID{账号ID}_{账号名}_收藏作品`

#### 🗂️ 合集作品文件夹命名规则
- **合集作品**: `MID{合集ID}_{合集名}_合集作品`

#### 📝 命名规则说明
- **账号名优先级**: 
  - 如果配置了 `mark` 参数（账号标识），使用 `mark` 作为账号名
  - 如果 `mark` 为空，使用实际的账号昵称
- **自动更新**: 当账号昵称发生变化时，程序会自动识别并更新文件夹名称
- **唯一标识**: UID/MID确保即使账号名相同也不会冲突

#### 🌰 文件夹命名示例
```
批量下载示例目录结构:
/your/root/path/
├── UID123456789_北京日报_发布作品/
│   ├── 2024-01-15-视频-北京日报-新闻标题.mp4
│   └── 2024-01-16-图片-北京日报-图片新闻.jpg
├── UID987654321_四川融媒体快报_发布作品/
│   ├── 2024-01-15-视频-四川融媒体快报-地方新闻.mp4
│   └── 2024-01-16-视频-四川融媒体快报-民生资讯.mp4
├── MID555666777_搞笑合集_合集作品/
│   ├── 2024-01-15-视频-用户A-搞笑视频1.mp4
│   └── 2024-01-16-视频-用户B-搞笑视频2.mp4
└── Data/                              # 数据存储目录
    ├── DetailData.xlsx
    └── UserData.xlsx
```

#### ⚠️ 配置注意事项
- **单个下载**: 使用 `folder_name` 参数设置的文件夹名
- **批量下载**: 忽略 `folder_name`，使用自动生成的文件夹名
- **文件夹唯一性**: 通过UID/MID确保不同账号/合集的文件夹不会重复

### 🏷️ name_format (文件命名格式)
**功能**: 设置下载文件的命名规则
**类型**: 字符串（空格分隔的字段）
**默认值**: `"create_time type nickname desc"`

**可用字段**（共7个）:
- `id`: 作品ID（唯一标识符）
- `desc`: 作品描述/标题
- `create_time`: 发布时间（格式由date_format控制）
- `nickname`: 账号昵称
- `uid`: 账号ID（数字ID）
- `mark`: 账号标识（来自配置文件中的mark字段）
- `type`: 作品类型（视频/图片/图集等）

**示例配置**:
```json
"name_format": "create_time type nickname desc"
// 生成文件名: 2024-01-15 14:30:25-视频-大浩哥-搞笑视频合集.mp4

"name_format": "nickname id desc"
// 生成文件名: 大浩哥-7318394756123456789-搞笑视频合集.mp4

"name_format": "mark create_time type"
// 生成文件名: 大浩哥-2024-01-15 14:30:25-视频.mp4
```

**重要说明**:
- 字段之间用**空格**分隔
- 如果设置了无效字段，程序会自动使用默认值：`["create_time", "type", "nickname", "desc"]`
- 批量下载链接作品时，`mark` 字段会自动替换为 `nickname` 字段
- 所有字段都是可选的，可以任意组合

### 📅 date_format (日期格式)
**功能**: 设置时间字段的显示格式
**类型**: 字符串（Python strftime格式）
**默认值**: `"%Y-%m-%d %H:%M:%S"`

**常用格式**:
```json
"date_format": "%Y-%m-%d %H:%M:%S"    // 2024-01-15 14:30:25
"date_format": "%Y%m%d_%H%M%S"        // 20240115_143025
"date_format": "%Y年%m月%d日"          // 2024年01月15日
"date_format": "%m-%d %H:%M"          // 01-15 14:30
```

**格式代码说明**:
- `%Y`: 四位年份 (2024)
- `%m`: 月份 (01-12)
- `%d`: 日期 (01-31)
- `%H`: 小时 (00-23)
- `%M`: 分钟 (00-59)
- `%S`: 秒钟 (00-59)

### ➖ split (分隔符)
**功能**: 设置文件名中各字段之间的分隔符
**类型**: 字符串
**默认值**: `"-"`

```json
"split": "-"     // 使用短横线: 昵称-时间-描述
"split": "_"     // 使用下划线: 昵称_时间_描述
"split": " "     // 使用空格: 昵称 时间 描述
"split": "."     // 使用点号: 昵称.时间.描述
```

### 📁 folder_mode (文件夹模式)
**功能**: 是否为每个作品创建单独的文件夹
**类型**: 布尔值
**默认值**: `false`

```json
"folder_mode": false  // 所有文件存储在同一目录
"folder_mode": true   // 每个作品创建单独文件夹
```

**效果对比**:
- `false`: 所有文件平铺在下载目录中
- `true`: 每个作品创建以文件名命名的文件夹，文件存储在其中

### 🎵 music (音乐下载)
**功能**: 是否同时下载作品的背景音乐
**类型**: 布尔值
**默认值**: `false`

```json
"music": false   // 不下载音乐
"music": true    // 同时下载音乐文件
```

### ✂️ truncate (文件名长度限制)
**功能**: 限制文件名的最大长度（按字符宽度计算）
**类型**: 整数
**默认值**: `50`
**最小值**: `32`（小于32会使用默认值50）

**字符计算规则**:
- **中文字符**（CJK字符）：占用 **2个单位**
- **英文字符**（ASCII字符）：占用 **1个单位**
- **示例**: "Hello世界" = 5×1 + 2×2 = 9个单位

```json
"truncate": 50   // 文件名最多50个字符单位
"truncate": 100  // 文件名最多100个字符单位  
"truncate": 80   // 文件名最多80个字符单位（如配置示例）
```

**截断处理**:
- 当文件名超过限制时，程序会智能截断
- 截断格式：`开头部分...结尾部分`
- 确保重要信息（开头和结尾）都能保留

**注意事项**:
- 此参数主要影响**下载进度条**中的文件名显示
- 不影响实际的数据存储内容
- 需要考虑操作系统的文件名长度限制（通常为255字节）

### 💾 storage_format (数据存储格式)
**功能**: 设置作品信息的存储格式
**类型**: 字符串
**默认值**: `""` (不存储)

**支持格式**:
```json
"storage_format": ""       // 不存储数据（仅下载媒体文件）
"storage_format": "xlsx"   // Excel格式（推荐，易于查看）
"storage_format": "csv"    // CSV格式（兼容性好）
"storage_format": "sql"    // SQLite数据库格式（支持复杂查询）
```

**重要说明**:
- 当 `storage_format` 为空字符串 `""` 时，程序**不会创建任何数据文件**，只下载视频/图片等媒体文件
- 这是导致 **Data目录为空** 的主要原因
- 修改此参数后需要**重启程序**才能生效

#### 🎯 视频描述的保存方式

**保存位置**: `{root路径}/Data/DetailData.{格式}`

**视频描述存储字段**:
- **desc**: 作品描述（视频标题/文案）
- **text_extra**: 作品话题标签
- **id**: 作品唯一ID
- **create_time**: 发布时间
- **nickname**: 作者昵称
- **uid**: 作者用户ID
- **share_url**: 作品分享链接
- **duration**: 视频时长
- **downloads**: 下载地址
- **digg_count**: 点赞数量
- **comment_count**: 评论数量
- **collect_count**: 收藏数量
- **share_count**: 分享数量
- **play_count**: 播放数量

**查看方式**:
- **Excel格式** (`.xlsx`): 用Excel、WPS等软件打开
- **CSV格式** (`.csv`): 用Excel、记事本等软件打开
- **SQLite格式** (`.db`): 用SQLite浏览器或数据库工具打开

#### ❗ 常见问题解决

**问题**: Data目录为空，没有视频描述等数据
**原因**: `storage_format` 参数未设置或设置为空字符串
**解决方案**:
1. 打开 `settings.json` 配置文件
2. 将 `"storage_format": ""` 修改为 `"storage_format": "xlsx"`
3. 保存文件并重启程序
4. 重新下载后即可在Data目录看到数据文件

### 📊 Data目录说明
**目录位置**: `{root路径}/Data/`
**创建时机**: 程序运行时自动创建
**功能**: 存储程序运行过程中收集的各种数据文件

#### 📁 Data目录的作用
Data目录是程序的**数据持久化存储中心**，用于保存以下类型的数据：

1. **作品详细信息** (`DetailData.*`)
   - **文件名**: `DetailData.db` / `DetailData.xlsx` / `DetailData.csv`
   - **主要内容**: 
     - 作品基本信息：ID、标题描述、发布时间、视频时长
     - 作者信息：昵称、UID、账号签名
     - 互动数据：点赞数、评论数、收藏数、分享数、播放数
     - 媒体信息：下载地址、封面链接、音乐信息
     - 话题标签：相关话题和标签信息
   - **应用场景**: 数据分析、内容管理、批量处理

2. **用户信息数据** (`UserData.*`)
   - **文件名**: `UserData.db` / `UserData.xlsx` / `UserData.csv`
   - **主要内容**: 
     - 基本信息：用户ID、昵称、头像链接
     - 统计数据：粉丝数、关注数、获赞总数
     - 账号信息：个人简介、认证状态、年龄
   - **应用场景**: 用户画像分析、KOL筛选

3. **评论数据** (`CommentData.*`)
   - **文件名**: `CommentData.db` / `CommentData.xlsx` / `CommentData.csv`
   - **主要内容**: 
     - 评论内容：评论文本、评论时间
     - 评论者信息：昵称、UID、头像
     - 互动数据：点赞数、回复数
   - **应用场景**: 舆情分析、用户反馈收集

4. **合集数据** (`MixData.*`)
   - **文件名**: `MixData.db` / `MixData.xlsx` / `MixData.csv`
   - **主要内容**: 合集中的作品信息（格式同DetailData）
   - **应用场景**: 系列内容分析、专题研究

5. **搜索结果数据** (`SearchData.*`)
   - **文件名**: `SearchData.db` / `SearchData.xlsx` / `SearchData.csv`
   - **主要内容**: 
     - 搜索关键词对应的作品信息
     - 相关用户信息
     - 直播间信息
   - **应用场景**: 关键词监控、竞品分析

6. **热榜数据** (`BoardData.*`)
   - **文件名**: `BoardData.db` / `BoardData.xlsx` / `BoardData.csv`
   - **主要内容**: 
     - 热门话题：排名、内容、热度值
     - 时间信息：上榜时间、持续时间
     - 相关数据：浏览数量、视频数量
   - **应用场景**: 热点追踪、趋势分析

#### 🔧 Data目录的创建机制
Data目录由程序中的 `RecordManager` 类自动管理：

```python
# 核心创建逻辑（位于 src/storage/manager.py）
root = parameter.root.joinpath(parameter.CLEANER.filter_name(folder, "Data"))
root.mkdir(exist_ok=True)  # 自动创建Data目录
```

**触发条件**:
- 批量下载作品时
- 获取用户信息时
- 下载评论数据时
- 执行搜索功能时
- 获取热榜数据时
- 任何需要数据记录的操作

#### 📋 数据文件格式说明
根据 `storage_format` 配置，Data目录中的文件格式会有所不同：

- **SQLite格式** (`.db`): 结构化数据库文件，支持复杂查询
- **Excel格式** (`.xlsx`): 可用Excel打开的电子表格
- **CSV格式** (`.csv`): 逗号分隔值文件，兼容性好
- **空值**: 不创建数据文件，仅下载媒体文件

#### ⚠️ 注意事项
1. **配置依赖**: Data目录的创建和数据文件的生成**完全依赖** `storage_format` 参数
   - `storage_format` 为空时：只下载媒体文件，不创建数据文件
   - `storage_format` 有值时：同时下载媒体文件和创建数据文件
2. **自动创建**: Data目录会在程序首次需要存储数据时自动创建
3. **位置固定**: 始终位于配置的 `root` 路径下
4. **权限要求**: 需要对 `root` 路径有写入权限
5. **数据累积**: 数据文件会持续累积，不会自动清理
6. **重启生效**: 修改 `storage_format` 参数后需要重启程序才能生效
7. **备份建议**: 重要数据建议定期备份
8. **格式兼容**: 不同格式的数据文件内容相同，只是存储方式不同

#### 💡 数据文件管理建议
- **推荐格式**: Excel格式 (`.xlsx`) - 易于查看和分析
- **大数据量**: SQLite格式 (`.db`) - 支持复杂查询和索引
- **兼容性**: CSV格式 (`.csv`) - 通用性最好，可导入其他系统
- **定期清理**: 可根据需要删除旧的数据文件，不影响程序运行
- **数据分析**: 可使用Excel、Python pandas、SQL工具等进行数据分析

#### 🗂️ 典型目录结构示例
```
/your/root/path/
├── Data/                          # 数据存储目录
│   ├── DetailData.xlsx           # 作品详细信息
│   ├── UserData.xlsx             # 用户信息
│   ├── CommentData.xlsx          # 评论数据
│   └── SearchData.xlsx           # 搜索结果
├── UID123456_用户名_发布作品/      # 用户作品目录
│   ├── 视频1.mp4
│   └── 视频2.mp4
└── 其他下载文件...
```

---

## 下载配置

### 📥 download (下载开关)
**功能**: 控制是否启用文件下载功能
**类型**: 布尔值
**默认值**: `true`

```json
"download": true   // 启用下载
"download": false  // 仅获取信息，不下载文件
```

### 📏 max_size (文件大小限制)
**功能**: 设置单个文件的最大下载大小（字节）
**类型**: 整数
**默认值**: `0` (无限制)

```json
"max_size": 0           // 无限制
"max_size": 104857600   // 100MB限制 (100 * 1024 * 1024)
"max_size": 52428800    // 50MB限制
```

**计算公式**: `大小(MB) × 1024 × 1024 = 字节数`

### 🔄 chunk (数据块大小)
**功能**: 设置每次从服务器接收的数据块大小
**类型**: 整数
**默认值**: `2097152` (2MB)

```json
"chunk": 2097152   // 2MB (推荐)
"chunk": 1048576   // 1MB (较慢但稳定)
"chunk": 4194304   // 4MB (较快但可能不稳定)
```

### ⏱️ timeout (超时时间)
**功能**: 设置网络请求的超时时间（秒）
**类型**: 整数
**默认值**: `10`

```json
"timeout": 10   // 10秒超时
"timeout": 30   // 30秒超时（网络较慢时）
"timeout": 5    // 5秒超时（网络较快时）
```

### 🔁 max_retry (最大重试次数)
**功能**: 设置下载失败时的最大重试次数
**类型**: 整数
**默认值**: `5`

```json
"max_retry": 5   // 最多重试5次
"max_retry": 3   // 最多重试3次
"max_retry": 10  // 最多重试10次
```

### 📄 max_pages (最大页数限制)
**功能**: 限制批量下载时的最大页数
**类型**: 整数
**默认值**: `0` (无限制)

```json
"max_pages": 0   // 无限制
"max_pages": 10  // 最多下载10页
"max_pages": 50  // 最多下载50页
```

### 🖼️ dynamic_cover / static_cover (封面下载)
**功能**: 控制是否下载作品封面图
**类型**: 布尔值
**默认值**: `false`

```json
"dynamic_cover": false,  // 不下载动态封面
"static_cover": false    // 不下载静态封面

"dynamic_cover": true,   // 下载动态封面
"static_cover": true     // 下载静态封面
```

---

## 网络配置

### 🌐 proxy (抖音代理设置)
**功能**: 设置访问抖音时使用的代理服务器
**类型**: 字符串
**默认值**: `""` (不使用代理)

```json
"proxy": ""                          // 不使用代理
"proxy": "http://127.0.0.1:7890"     // HTTP代理 (Clash)
"proxy": "http://127.0.0.1:10809"    // HTTP代理 (v2rayN)
"proxy": "socks5://127.0.0.1:1080"   // SOCKS5代理
```

### 🌍 proxy_tiktok (TikTok代理设置)
**功能**: 设置访问TikTok时使用的代理服务器
**格式**: 与 `proxy` 相同

### 🔧 twc_tiktok (TikTok特殊参数)
**功能**: TikTok的ttwid参数，一般无需设置
**类型**: 字符串
**默认值**: `""`

---

## 平台配置

### 📱 douyin_platform (抖音平台开关)
**功能**: 控制是否启用抖音平台功能
**类型**: 布尔值
**默认值**: `true`

### 🌍 tiktok_platform (TikTok平台开关)
**功能**: 控制是否启用TikTok平台功能
**类型**: 布尔值
**默认值**: `true`

---

## 高级配置

### 🍪 cookie (抖音Cookie)
**功能**: 存储抖音登录状态的Cookie信息
**类型**: 字符串或对象
**获取方法**: 
1. 浏览器登录抖音
2. 按F12打开开发者工具
3. 在Network标签页找到请求
4. 复制Cookie值

### 🍪 cookie_tiktok (TikTok Cookie)
**功能**: 存储TikTok登录状态的Cookie信息
**格式**: 与抖音Cookie相同

### 🌐 browser_info (抖音浏览器信息)
**功能**: 模拟浏览器环境的详细信息

```json
"browser_info": {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...",
    "pc_libra_divert": "Windows",
    "browser_platform": "Win32",
    "browser_name": "Chrome",
    "browser_version": "136.0.0.0",
    "engine_name": "Blink",
    "engine_version": "136.0.0.0",
    "os_name": "Windows",
    "os_version": "10",
    "webid": ""
}
```

### 🌍 browser_info_tiktok (TikTok浏览器信息)
**功能**: TikTok平台的浏览器环境信息
**格式**: 类似browser_info，但包含更多TikTok特定字段

### ⚡ run_command (启动命令)
**功能**: 设置程序启动时自动执行的命令
**类型**: 字符串
**默认值**: `""`

```json
"run_command": ""        // 手动选择功能
"run_command": "1"       // 自动执行功能1
"run_command": "2 3"     // 依次执行功能2和3
```

### 🎬 ffmpeg (FFmpeg路径)
**功能**: 设置FFmpeg程序的路径（用于直播下载）
**类型**: 字符串
**默认值**: `""`

```json
"ffmpeg": ""                           // 使用系统PATH中的ffmpeg
"ffmpeg": "/usr/local/bin/ffmpeg"      // macOS/Linux完整路径
"ffmpeg": "C:\\ffmpeg\\bin\\ffmpeg.exe" // Windows完整路径
```

### 📺 live_qualities (直播质量)
**功能**: 设置直播下载的画质选择
**类型**: 字符串
**默认值**: `""`

---

## 配置示例

### 🎯 基础使用配置
```json
{
    "root": "/Users/username/Downloads/TikTok",
    "folder_name": "douyin",
    "name_format": "create_time nickname desc",
    "date_format": "%Y-%m-%d %H:%M:%S",
    "split": "-",
    "folder_mode": false,
    "music": false,
    "download": true,
    "cookie": "你的Cookie值"
}
```

### 🚀 高级用户配置
```json
{
    "accounts_urls": [
        {
            "mark": "搞笑博主",
            "url": "https://www.douyin.com/user/MS4wLjABAAAA...",
            "tab": "post",
            "earliest": "2024-01-01",
            "latest": "2024-12-31",
            "enable": true
        }
    ],
    "root": "/Volumes/ExternalDrive/TikTok",
    "folder_name": "downloads",
    "name_format": "mark create_time type desc",
    "date_format": "%Y%m%d_%H%M%S",
    "split": "_",
    "folder_mode": true,
    "music": true,
    "truncate": 80,
    "storage_format": "xlsx",
    "download": true,
    "max_size": 104857600,
    "chunk": 2097152,
    "timeout": 15,
    "max_retry": 3,
    "max_pages": 20,
    "proxy": "http://127.0.0.1:7890",
    "cookie": "你的Cookie值"
}
```

### 🎨 自定义命名配置
```json
{
    "name_format": "nickname id",
    "date_format": "%Y年%m月%d日",
    "split": " ",
    "folder_mode": true,
    "truncate": 60
}
```
**效果**: `大浩哥 7318394756123456789/大浩哥 7318394756123456789.mp4`

---

## 常见问题

### ❓ 配置修改不生效
**解决方案**: 
1. 检查JSON格式是否正确
2. 重启程序
3. 查看控制台错误信息

### ❓ 文件名包含非法字符
**解决方案**: 
- 程序会自动过滤非法字符
- 调整 `truncate` 参数控制长度
- 修改 `split` 参数避免特殊字符

### ❓ 下载速度慢
**解决方案**: 
1. 增大 `chunk` 值 (如4194304)
2. 增加 `timeout` 值
3. 检查网络连接
4. 考虑使用代理

### ❓ 代理设置无效
**解决方案**: 
1. 确认代理服务器正常运行
2. 检查代理地址和端口
3. 尝试不同的代理协议 (http/socks5)

### ❓ Cookie失效
**解决方案**: 
1. 重新获取Cookie
2. 检查账号登录状态
3. 确认Cookie格式正确

### ❓ 如何退出程序
**多种退出方式**: 
1. **主菜单退出**: 在主功能选择菜单中输入 `Q` 或 `q`，然后按回车键
2. **直接按回车**: 在主菜单中直接按回车键（不输入任何内容）
3. **子菜单退出**: 在各个功能的子菜单中输入 `Q` 或 `q` 返回上一级菜单
4. **输入提示退出**: 在要求输入链接的地方，输入 `Q` 或 `q` 退出当前功能
5. **强制退出**: 使用 `Ctrl + C` 强制中断程序（不推荐，可能导致数据丢失）

**推荐退出方式**: 使用 `Q` 或 `q` 命令正常退出，程序会自动清理资源并保存状态

---

## 📝 注意事项

1. **备份配置**: 修改前请备份原配置文件
2. **权限问题**: 确保下载目录有写入权限
3. **网络稳定**: 保持网络连接稳定
4. **合理使用**: 遵守平台使用规则
5. **定期更新**: 关注程序更新和配置变化
6. **配置生效**: 修改配置文件后需要重启程序才能生效

---

## 🔗 相关链接

- [Python strftime文档](https://docs.python.org/zh-cn/3/library/time.html#time.strftime)
- [JSON格式验证工具](https://try8.cn/tool/format/json)
- [项目GitHub地址](https://github.com/JoeanAmier/TikTokDownloader)

---

*最后更新: 2024年1月*