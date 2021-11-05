from pyrogram import Client
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import Message

from ..helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f'<b> - هلا عيني {message.from_user.mention()}!</b>\n\n'
        'I am Calls Music bot, '
        'I let you play music in group calls.'
        '\n\nThe commands I currently support are:\n\n'
        '/play - بالرد على الاغنية او المقطع الصوتي للتشغيل\n'
        '/pause - لايقاف الاغنيه بشكل مؤقت\n'
        '/resume - لتشغيل الاغنيه بعد الايقاف المؤقت\n'
        '/skip - لتخطي الاغنية\n'
        '/mute - mute the userbot\n'
        '/unmute - unmute the userbot\n'
        '/stop - clear the queue and remove the userbot from the call',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        '🔈 Channel', url='https://t.me/callsmusic',
                    ),
                    InlineKeyboardButton(
                        'Group 💬', url='https://t.me/callsmusicchat',
                    ),
                ],
            ],
        ),
    )
