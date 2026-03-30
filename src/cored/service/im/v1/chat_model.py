# Copyright (c) 2026 Cored Limited
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dataclasses import dataclass

from cored.core.types import BaseModel


# Set typing status (Request)
@dataclass
class CreateTypingReq(BaseModel):
    chat_id: str | None = None  # Chat ID


# Set typing status (Response)
@dataclass
class CreateTypingResp(BaseModel):
    pass


# Clear typing status (Request)
@dataclass
class DeleteTypingReq(BaseModel):
    chat_id: str | None = None  # Chat ID


# Clear typing status (Response)
@dataclass
class DeleteTypingResp(BaseModel):
    pass

