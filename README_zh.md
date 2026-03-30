# Cored IM OpenAPI SDK - Python

[![PyPI version](https://img.shields.io/pypi/v/cored-sdk.svg)](https://pypi.org/project/cored-sdk/)
[![CI](https://github.com/cored-im/openapi-sdk-python/actions/workflows/ci.yaml/badge.svg)](https://github.com/cored-im/openapi-sdk-python/actions/workflows/ci.yaml)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/github/license/cored-im/openapi-sdk-python)](LICENSE)

[English](README.md) | 中文

Cored 是一个安全、可自托管的团队协作平台，集成了即时通讯、组织架构、音视频会议和文件存储等功能。

本项目是Cored服务端的 Python SDK，用于通过 OpenAPI 与Cored服务端进行交互。使用前需要先自行部署Cored服务端，部署教程请参考[快速部署文档](https://coredim.com/docs/admin/install/quick-install)。

## 安装

```bash
pip install cored-sdk
```

## 快速开始

```python
import asyncio
from cored import CoredClient, SendMessageReq, MessageContent, MessageText, MessageType_TEXT

async def main():
    client = await CoredClient.create(
        "https://your-backend-url.com",
        "your-app-id",
        "your-app-secret",
    )

    # 可选：预热可提前获取访问凭证和同步服务端时间，减少首次调用的延迟
    await client.preheat()

    # 调用 API
    resp = await client.im.message.send_message(SendMessageReq(
        chat_id="chat-id",
        message_type=MessageType_TEXT,
        message_content=MessageContent(text=MessageText(content="Cored 新版本发布！")),
    ))
    print(resp.message_id)

    # 使用完毕后关闭
    await client.close()

asyncio.run(main())
```

## 客户端配置

`CoredClient.create()` 支持通过关键字参数配置客户端行为：

```python
from cored import CoredClient, LogLevel

client = await CoredClient.create(
    "https://your-backend-url.com",
    "your-app-id",
    "your-app-secret",
    log_level=LogLevel.DEBUG,         # 日志级别（默认: INFO）
    request_timeout=30.0,             # 请求超时秒数（默认: 60.0）
    enable_encryption=False,          # 启用请求加密（默认: True）
)
```

## 事件订阅

通过 WebSocket 接收实时事件推送：

```python
from cored import EventMessageReceive

def on_message(event: EventMessageReceive):
    print("收到消息:", event.body)

client.im.message.event.on_message_receive(on_message)

# 取消订阅
client.im.message.event.off_message_receive(on_message)
```

## 上下文管理器

支持 `async with` 语法自动关闭客户端：

```python
async with await CoredClient.create(...) as client:
    resp = await client.im.message.send_message(SendMessageReq(...))
```

## 环境要求

- **Python** 3.9+

## 相关链接

- [官网](https://cored.im/)

## 许可证

[Apache-2.0 License](LICENSE)
