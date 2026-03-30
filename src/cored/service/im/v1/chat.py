# Copyright (c) 2026 Cored Limited
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import TYPE_CHECKING

from cored.core.types import ApiRequest
from cored.service.im.v1.chat_model import (
    CreateTypingReq,
    CreateTypingResp,
    DeleteTypingReq,
    DeleteTypingResp,
)

if TYPE_CHECKING:
    from cored.core.config import Config


class Chat:
    def __init__(self, config: Config) -> None:
        self._config = config


    async def create_typing(self, req: CreateTypingReq) -> CreateTypingResp:
        """Set typing status
        
        Set the typing status, lasts only 5 seconds, direct messages only
        """
        body = req.to_dict()
        resp = await self._config.api_client.request(ApiRequest(
            method="POST",
            path=f"/oapi/im/v1/chats/{body.get('chat_id', '')}/typing",
            body=body,
            with_app_access_token=True,
        ))
        return CreateTypingResp.from_dict(resp.json())

    async def delete_typing(self, req: DeleteTypingReq) -> DeleteTypingResp:
        """Clear typing status
        
        Direct messages only
        """
        body = req.to_dict()
        resp = await self._config.api_client.request(ApiRequest(
            method="DELETE",
            path=f"/oapi/im/v1/chats/{body.get('chat_id', '')}/typing",
            body=body,
            with_app_access_token=True,
        ))
        return DeleteTypingResp.from_dict(resp.json())
