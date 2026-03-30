# Copyright (c) 2026 Cored Limited
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import TYPE_CHECKING

from cored.core.types import ApiRequest
from cored.service.im.v1.message_model import (
    SendMessageReq,
    SendMessageResp,
    GetMessageReq,
    GetMessageResp,
    RecallMessageReq,
    RecallMessageResp,
    ReadMessageReq,
    ReadMessageResp,
)
from cored.service.im.v1.message_event import MessageEvent

if TYPE_CHECKING:
    from cored.core.config import Config


class Message:
    def __init__(self, config: Config) -> None:
        self._config = config
        self.event = MessageEvent(config)


    async def send_message(self, req: SendMessageReq) -> SendMessageResp:
        """Send a message"""
        body = req.to_dict()
        resp = await self._config.api_client.request(ApiRequest(
            method="POST",
            path="/oapi/im/v1/messages",
            body=body,
            with_app_access_token=True,
            with_web_socket=True,
        ))
        return SendMessageResp.from_dict(resp.json())

    async def get_message(self, req: GetMessageReq) -> GetMessageResp:
        """Get a message"""
        body = req.to_dict()
        resp = await self._config.api_client.request(ApiRequest(
            method="GET",
            path=f"/oapi/im/v1/messages/{body.get('message_id', '')}",
            body=body,
            with_app_access_token=True,
        ))
        return GetMessageResp.from_dict(resp.json())

    async def recall_message(self, req: RecallMessageReq) -> RecallMessageResp:
        """Recall a message"""
        body = req.to_dict()
        resp = await self._config.api_client.request(ApiRequest(
            method="POST",
            path=f"/oapi/im/v1/messages/{body.get('message_id', '')}/recall",
            body=body,
            with_app_access_token=True,
        ))
        return RecallMessageResp.from_dict(resp.json())

    async def read_message(self, req: ReadMessageReq) -> ReadMessageResp:
        """Mark message as read"""
        body = req.to_dict()
        resp = await self._config.api_client.request(ApiRequest(
            method="POST",
            path=f"/oapi/im/v1/messages/{body.get('message_id', '')}/read",
            body=body,
            with_app_access_token=True,
        ))
        return ReadMessageResp.from_dict(resp.json())
