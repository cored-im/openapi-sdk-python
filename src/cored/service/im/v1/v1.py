# Copyright (c) 2026 Cored Limited
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cored.core.config import Config

from cored.service.im.v1.chat import Chat
from cored.service.im.v1.message import Message


class V1:
    def __init__(self, config: Config) -> None:
        self.chat = Chat(config)
        self.message = Message(config)
