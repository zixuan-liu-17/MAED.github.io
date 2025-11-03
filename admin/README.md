# Decap CMS 管理后台使用指南

## 访问管理后台

推送代码后，访问：`https://zixuan-liu-17.github.io/MAED.github.io/admin/`

## 设置步骤

### 选项 1: 使用 Netlify（推荐，最简单）

1. 去 [Netlify](https://netlify.com) 注册账号
2. 点击 "Add new site" → "Import an existing project"
3. 选择你的 GitHub 仓库
4. 构建设置保持默认（Jekyll）
5. 点击 "Deploy site"
6. 部署后，访问 `你的网站.netlify.app/admin/` 即可使用管理后台

**优点：**
- 完全免费
- 自动配置 OAuth
- 支持预览功能
- 更快的访问速度

### 选项 2: GitHub Pages + GitHub 直接编辑

如果不想使用 Netlify，可以：
1. 登录 GitHub
2. 访问仓库
3. 点击文件旁边的铅笔图标编辑
4. 保存更改

### 选项 3: 配置 OAuth（高级）

需要自己设置 OAuth 服务器或使用第三方服务如 [Decap CMS OAuth](https://github.com/vencax/netlify-cms-github-oauth-provider)

## 可编辑的内容

管理后台可以编辑以下内容：

### 页面（Pages）
- About Page - 关于页面
- Application Page - 应用页面
- Dataset Page - 数据集页面
- Get Involved Page - 参与页面
- Learning Capacity Page - 学习能力页面

### 博客文章（Blog Posts）
- 可以创建、编辑、删除博客文章

## 使用方法

1. 访问管理后台
2. 使用 GitHub 账号登录
3. 选择要编辑的页面
4. 编辑内容（支持 Markdown 和富文本编辑器）
5. 点击 "Save" 保存
6. 点击 "Publish" 发布更改

## 注意事项

- 所有更改会自动创建 Git commit
- 可以使用 "Editorial Workflow" 功能来审核更改
- 支持上传图片到 `/assets/img/` 目录
- 支持 Markdown 预览

## 推荐方案

**最简单的方式：** 使用 Netlify 部署网站，自动获得完整的 CMS 功能。

Netlify 会：
- 自动配置 OAuth
- 提供更快的访问速度
- 支持表单提交
- 提供 SSL 证书
- 完全免费（对于小型网站）

