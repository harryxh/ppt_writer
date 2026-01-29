#!/bin/bash

# PPT Writer + Presenton 启动脚本
# 在 Codespace 终端中运行此脚本

set -e

echo "🚀 启动 PPT Writer 开发环境..."

# 检查 Docker 是否可用
if ! command -v docker &> /dev/null; then
    echo "⚠️  Docker 未安装，尝试使用本地模式..."
    
    # 检查是否存在 Presenton
    if [ -d "../presenton" ]; then
        echo "📦 检测到 Presenton，跳过安装..."
    else
        echo "📥 克隆 Presenton..."
        cd ..
        git clone https://github.com/presenton/presenton.git
        cd ppt_writer
    fi
    
    echo "✅ 使用本地模式运行"
    echo "💡 请手动配置 API Key 后访问 http://localhost:5000"
else
    echo "🐳 检测到 Docker，使用容器模式..."
    
    # 检查是否已存在容器
    if docker ps -a | grep -q ppt-writer; then
        echo "📦 发现已有容器，检查状态..."
        if docker ps | grep -q ppt-writer; then
            echo "✅ 容器已在运行，访问 http://localhost:5000"
            echo "🔗 公开访问: https://${CODESPACE_NAME}-5000.preview.app.github.dev"
        else
            echo "▶️  启动容器..."
            docker-compose up -d
            echo "✅ 容器已启动，访问 http://localhost:5000"
            echo "🔗 公开访问: https://${CODESPACE_NAME}-5000.preview.app.github.dev"
        fi
    else
        echo "🏗️  首次启动，构建并运行容器..."
        docker-compose up -d --build
        echo "✅ 容器已启动，访问 http://localhost:5000"
        echo "🔗 公开访问: https://${CODESPACE_NAME}-5000.preview.app.github.dev"
    fi
fi

echo ""
echo "📖 使用说明:"
echo "   1. 打开浏览器访问上述链接"
echo "   2. 输入你的 OpenAI API Key"
echo "   3. 输入 PPT 主题并生成"
echo ""
echo "🔗 GitHub: https://github.com/harryxh/ppt_writer"
