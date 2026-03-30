# Copyright (c) 2026 Cored Limited
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dataclasses import dataclass

from cored.core.types import BaseModel


# Send a message (Request)
@dataclass
class SendMessageReq(BaseModel):
    message_type: str | None = None  # Message type
    message_content: MessageContent | None = None  # Message content
    chat_id: str | None = None  # Chat ID
    reply_message_id: str | None = None  # ID of the message being replied to


# Send a message (Response)
@dataclass
class SendMessageResp(BaseModel):
    message_id: str | None = None  # Message ID


# Get a message (Request)
@dataclass
class GetMessageReq(BaseModel):
    message_id: str | None = None  # Message ID


# Get a message (Response)
@dataclass
class GetMessageResp(BaseModel):
    message: Message | None = None  # Message


# Recall a message (Request)
@dataclass
class RecallMessageReq(BaseModel):
    message_id: str | None = None  # Message ID


# Recall a message (Response)
@dataclass
class RecallMessageResp(BaseModel):
    pass


# Mark message as read (Request)
@dataclass
class ReadMessageReq(BaseModel):
    message_id: str | None = None  # Message ID


# Mark message as read (Response)
@dataclass
class ReadMessageResp(BaseModel):
    pass


# Message content
@dataclass
class MessageContent(BaseModel):
    text: MessageText | None = None  # Text message
    image: MessageImage | None = None  # Image message
    sticker: MessageSticker | None = None  # Sticker message
    video: MessageVideo | None = None  # Video message
    audio: MessageAudio | None = None  # Audio message
    file: MessageFile | None = None  # File message
    user_card: MessageUserCard | None = None  # User card message
    group_card: MessageGroupCard | None = None  # Group card message
    group_announcement: MessageGroupAnnouncement | None = None  # Group announcement
    card: MessageCard | None = None  # Card message


# Text message
@dataclass
class MessageText(BaseModel):
    content: str | None = None  # Content
    attachment_list: list[MessageTextAttachment] | None = None  # Attachment list, referenced in content as {{attach:id}}
    mention_user_list: list[MessageTextMentionUser] | None = None  # Mentioned user list, referenced in content as {{mention:user_id}}. Use user_id "all" to mention everyone
    emoji_list: list[MessageTextEmoji] | None = None  # Emoji list, referenced in content as {{emoji:emoji_id}}


# Attachment
@dataclass
class MessageTextAttachment(BaseModel):
    attachment_id: str | None = None  # Attachment ID, referenced in content as {{id}}, defined by the client
    attachment_type: str | None = None  # Attachment type
    attachment_content: MessageTextAttachmentContent | None = None  # Attachment content


# Attachment content
@dataclass
class MessageTextAttachmentContent(BaseModel):
    image: FileImage | None = None  # Image


# Image file
@dataclass
class FileImage(BaseModel):
    image: File | None = None  # Image, max width/height 1024
    image_width: int | None = None  # Image width
    image_height: int | None = None  # Image height
    image_origin: File | None = None  # Original image
    image_origin_width: int | None = None  # Original image width
    image_origin_height: int | None = None  # Original image height
    image_thumb_bytes: bytes | None = None  # Thumbnail data, max width/height 40
    image_thumb_mime: str | None = None  # Thumbnail MIME type
    image_dominant_color: str | None = None  # Dominant color of the image, in #ffffff format


# File
@dataclass
class File(BaseModel):
    file_id: str | None = None  # File ID
    file_mime: str | None = None  # File MIME type
    file_size: int | None = None  # File size
    file_encryption: Encryption | None = None  # File encryption


# Encryption
@dataclass
class Encryption(BaseModel):
    encryption_algorithm: str | None = None  # Encryption algorithm
    encryption_key: bytes | None = None  # Encryption key
    encrypted_size: int | None = None  # Encrypted size


# Mentioned user
@dataclass
class MessageTextMentionUser(BaseModel):
    user_id: UserId | None = None  # User ID
    user_name: str | None = None  # Username at the time of mention
    is_in_chat: bool | None = None  # Whether the user was in the chat at the time


# User ID
@dataclass
class UserId(BaseModel):
    user_id: str | None = None  # User ID in the platform. The same user has the same user_id across all apps
    union_user_id: str | None = None  # User ID within the same app group. The same user has the same union_user_id across different apps in the same group
    open_user_id: str | None = None  # User ID within an app. The same user has different open_user_id values in different apps


@dataclass
class MessageTextEmoji(BaseModel):
    emoji_id: str | None = None  # Emoji ID
    emoji_name: str | None = None  # Emoji name at the time


# Image message
@dataclass
class MessageImage(BaseModel):
    image: FileImage | None = None  # Image


# Sticker message
@dataclass
class MessageSticker(BaseModel):
    sticker: Sticker | None = None  # Sticker


# Sticker
@dataclass
class Sticker(BaseModel):
    sticker_id: str | None = None  # Sticker ID
    sticker_name: str | None = None  # Sticker name
    sticker_name_i18n: dict[str, str] | None = None  # Sticker internationalized name
    sticker_image: FileImage | None = None  # Sticker image


# Video message
@dataclass
class MessageVideo(BaseModel):
    video: FileVideo | None = None  # Video


# Video file
@dataclass
class FileVideo(BaseModel):
    video: File | None = None  # Video
    video_width: int | None = None  # Video width
    video_height: int | None = None  # Video height
    video_duration: float | None = None  # Video duration
    video_preview: FileImage | None = None  # Video preview image


# Audio message
@dataclass
class MessageAudio(BaseModel):
    audio: FileAudio | None = None  # Audio


# Audio file
@dataclass
class FileAudio(BaseModel):
    audio: File | None = None  # Audio
    audio_duration: float | None = None  # Audio duration


# File message
@dataclass
class MessageFile(BaseModel):
    file: File | None = None  # File
    filename: str | None = None  # Filename


# User card message
@dataclass
class MessageUserCard(BaseModel):
    user_id: UserId | None = None  # User ID


# Group card message
@dataclass
class MessageGroupCard(BaseModel):
    chat_id: str | None = None  # Chat ID


# Group announcement
@dataclass
class MessageGroupAnnouncement(BaseModel):
    message_text: MessageText | None = None  # Announcement content


# Card message
@dataclass
class MessageCard(BaseModel):
    schema: str | None = None  # Card schema version
    v1: MessageCardV1 | None = None  # V1


# V1
@dataclass
class MessageCardV1(BaseModel):
    header: MessageCardV1Header | None = None  # Card header
    body: MessageCardV1Body | None = None  # Card body
    footer: MessageCardV1Footer | None = None  # Card footer


# Card header
@dataclass
class MessageCardV1Header(BaseModel):
    title: str | None = None  # Title text
    title_i18n: dict[str, str] | None = None  # Internationalized title text
    template: str | None = None  # Title color template


# Card body
@dataclass
class MessageCardV1Body(BaseModel):
    message_text: MessageText | None = None  # Card body text message
    message_text_i18n: dict[str, MessageText] | None = None  # Internationalized card body text message


# Card footer
@dataclass
class MessageCardV1Footer(BaseModel):
    button_list: list[MessageCardV1Button] | None = None  # Button list
    button_align: str | None = None  # Button alignment


# Card button
@dataclass
class MessageCardV1Button(BaseModel):
    button_text: str | None = None  # Button text
    button_text_i18n: dict[str, str] | None = None  # Internationalized button text
    template: str | None = None  # Button style template, values: default, primary, danger, primary_text, danger_text, primary_filled, danger_filled
    link: MessageCardV1ButtonLink | None = None  # Button link


# Link
@dataclass
class MessageCardV1ButtonLink(BaseModel):
    url: str | None = None  # Default URL
    android_url: str | None = None  # Android URL
    ios_url: str | None = None  # iOS URL
    pc_url: str | None = None  # Desktop URL


# Message
@dataclass
class Message(BaseModel):
    message_id: str | None = None  # Message ID
    message_type: str | None = None  # Message type
    message_status: str | None = None  # Message status
    message_content: MessageContent | None = None  # Message content
    message_created_at: int | None = None  # Message creation time (milliseconds)
    chat_id: str | None = None  # Chat ID
    chat_seq_id: int | None = None  # Server-generated monotonically increasing ID at the chat level, used for ordering within a chat
    sender_id: UserId | None = None  # Sender ID
    reply: MessagePropReply | None = None  # Reply properties


# Message reply properties
@dataclass
class MessagePropReply(BaseModel):
    reply_message_id: str | None = None  # ID of the message being replied to


# Message received
@dataclass
class EventMessageReceiveBody(BaseModel):
    message: Message | None = None  # Message

