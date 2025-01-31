import pyrogram

from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from translation import Translation

helpbutton = [[
        InlineKeyboardButton(f'Channel', url="https://t.me/VKPROJECTS"),
        InlineKeyboardButton(f'Support', url="https://t.me/VKP_BOTS")
        ],[
        InlineKeyboardButton(f'🤖 About', callback_data="about")
    ]]

aboutbutton = [[
        InlineKeyboardButton(f'🤔 How To Use', callback_data="help"),
        InlineKeyboardButton(f'Close 🔐', callback_data="close")
    ]]


@Client.on_callback_query()
async def cb_handler(bot, update):

    if update.data == "help":
        await update.answer()
        keyboard = InlineKeyboardMarkup(helpbutton)
        await update.message.edit_text(
            text=Translation.HELP,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return

    elif update.data == "about":
        await update.answer()
        keyboard = InlineKeyboardMarkup(aboutbutton)
        await update.message.edit_text(
            text=Translation.ABOUT,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return

    elif update.data == "close":
        await update.message.delete()
