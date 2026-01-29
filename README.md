# PPT Writer - 集成 Presenton

本项目集成了 [Presenton](https://github.com/presenton/presenton) AI 演示文稿生成器。

## 快速开始

### 方式一：GitHub Codespace（推荐）

1. 在 GitHub 仓库页面点击 **"Code"** → **"Create codespace on main"**
2. 等待环境自动搭建（约2-3分钟）
3. 在终端运行启动脚本：
   ```bash
   ./start.sh
   ```
4. 点击终端显示的链接访问服务

### 方式二：本地 Docker

```bash
# 克隆并启动
git clone https://github.com/harryxh/ppt_writer.git
cd ppt_writer
cp .env.example .env
# 编辑 .env 添加你的 API Key
docker-compose up -d
# 访问 http://localhost:5000
```

## 功能

- 🎯 输入主题，自动生成结构化 PPT
- 🌐 支持网页内容采集
- 📄 支持文档上传
- 🎨 多主题模板
- 💾 导出 PPTX/PDF

## API 使用

```bash
curl -X POST http://localhost:5000/api/v1/ppt/presentation/generate \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Introduction to Machine Learning",
    "n_slides": 10,
    "language": "Chinese",
    "template": "modern"
  }'
```

## 配置

在 `.env` 文件中配置：

| 变量 | 说明 |
|------|------|
| OPENAI_API_KEY | OpenAI API Key |
| LLM | 模型提供商 (openai/google/anthropic/ollama) |
| IMAGE_PROVIDER | 图片生成器 |
| template | 默认模板 |

## 公开访问

在 Codespace 中，服务会自动通过 HTTPS 公开访问：
- 格式：`https://{codespace-name}-5000.preview.app.github.dev`
