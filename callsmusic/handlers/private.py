from pyrogram import Client
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import Message

from ..helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f'<b> - هلا عيني {message.from_user.mention()}</b>\n\n'
        '**- بوت ميرا , '
        '**بوت تشغيل اغاني او صوتيات في المحادثة الصوتيه والمرئيه**'
        '\n**- هاذي اوامر البوت يا عيني**\n\n'
        '/play - بالرد على الاغنية او المقطع الصوتي للتشغيل\n'
        '/pause - لايقاف الاغنيه بشكل مؤقت\n'
        '/resume - لتشغيل الاغنيه بعد الايقاف المؤقت\n'
        '/skip - لتخطي الاغنية\n'
        '/mute - لكتم البوت في المحادثة الصوتيه\n'
        '/unmute - لرفع الكتم عن البوت\n'
        '/stop - لايقاف جميع الاغاني الشغاله',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        'المطور', url='https://t.me/C1CIC',
                    ),
                    InlineKeyboardButton(
                        'قناة البوت', url='https://t.me/XkkkU',
                    ),
                ],
            ],
        ),
    )
