<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b5cdbb1 (More fixes in the kang module)
import os
from PIL import Image
import math
<<<<<<< HEAD
=======
from PIL import Image
>>>>>>> d17dba5 (Rewrite of the kang (stickers) module.)
=======
>>>>>>> 1c982b5 (Small fixes to the kang module)

from pyrogram import Client, raw
from pyrogram.file_id import FileId

STICKER_DIMENSIONS = (512, 512)


<<<<<<< HEAD
<<<<<<< HEAD
async def resize_file_to_sticker_size(file_path: str) -> str:
=======
async def resize_file_to_sticker_size(file_path: str):
>>>>>>> d17dba5 (Rewrite of the kang (stickers) module.)
=======
async def resize_file_to_sticker_size(file_path: str) -> str:
>>>>>>> a413f94 (Small fix regarding file formats in the kang module)
    im = Image.open(file_path)
    if (im.width, im.height) < STICKER_DIMENSIONS:
        size1 = im.width
        size2 = im.height
        if im.width > im.height:
            scale = STICKER_DIMENSIONS[0]/size1
            size1new = STICKER_DIMENSIONS[0]
            size2new = size2 * scale
        else:
            scale = STICKER_DIMENSIONS[1]/size2
            size1new = size1 * scale
            size2new = STICKER_DIMENSIONS[1]
        size1new = math.floor(size1new)
        size2new = math.floor(size2new)
        sizenew = (size1new, size2new)
        im = im.resize(sizenew)
    else:
        im.thumbnail(STICKER_DIMENSIONS)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a413f94 (Small fix regarding file formats in the kang module)
    try:
        os.remove(file_path)
        file_path = f"{file_path}.png"
        return file_path
    finally:
        im.save(file_path)
<<<<<<< HEAD


async def upload_document(client: Client, file_path: str, chat_id: int) -> raw.base.InputDocument:
    media = await client.send(
        raw.functions.messages.UploadMedia(
            peer=await client.resolve_peer(chat_id),
            media=raw.types.InputMediaUploadedDocument(
                mime_type=client.guess_mime_type(
                    file_path) or "application/zip",
                file=await client.save_file(file_path),
                attributes=[
                    raw.types.DocumentAttributeFilename(
                        file_name=os.path.basename(file_path)
                    )
                ]
            )
        )
    )
    return raw.types.InputDocument(id=media.document.id, access_hash=media.document.access_hash, file_reference=media.document.file_reference)


async def get_document_from_file_id(file_id: str) -> raw.base.InputDocument:
    decoded = FileId.decode(file_id)
    return raw.types.InputDocument(id=decoded.media_id, access_hash=decoded.access_hash, file_reference=decoded.file_reference)
=======
    im.save(file_path, "PNG")
=======
>>>>>>> a413f94 (Small fix regarding file formats in the kang module)

async def upload_document(client: Client, file_path: str, chat_id: int) -> raw.base.InputDocument:
    media = await client.send(
        raw.functions.messages.UploadMedia(
            peer=await client.resolve_peer(chat_id),
            media=raw.types.InputMediaUploadedDocument(
                mime_type=client.guess_mime_type(file_path) or "application/zip",
                file=await client.save_file(file_path),
                attributes=[
                    raw.types.DocumentAttributeFilename(
                        file_name=os.path.basename(file_path)
                    )
                ]
            )
        )
    )
    return raw.types.InputDocument(id=media.document.id, access_hash=media.document.access_hash, file_reference=media.document.file_reference)

async def get_document_from_file_id(file_id: str) -> raw.base.InputDocument:
    decoded = FileId.decode(file_id)
    return raw.types.InputDocument(id=decoded.media_id, access_hash=decoded.access_hash, file_reference=decoded.file_reference)
>>>>>>> d17dba5 (Rewrite of the kang (stickers) module.)
