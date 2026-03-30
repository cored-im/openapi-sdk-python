# Copyright (c) 2026 Cored Limited
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cored.core.config import Config

from cored.service.im.v1 import V1 as V1


class Service:
    def __init__(self, config: Config) -> None:
        self.v1 = V1(config)
        self.chat = self.v1.chat
        self.message = self.v1.message
