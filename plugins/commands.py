import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import pyrogram
from config import Config 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from translation import Translation
from Tools.Download import download

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="⚙️ Help", callback_data="help"),
        InlineKeyboardButton(text="🤖 About", callback_data="about"),
        ],[
        InlineKeyboardButton(text="Close 🔐", callback_data="close")
        ]]
    )

HTART_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="🤖 About", callback_data="about"),
        InlineKeyboardButton(text="Close 🔐", callback_data="close")
        ]]
    )

ATART_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Report Bugs 🐞", url="t.me/VKP_BOTS"),
        ]]
    )

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await c.send_message(chat_id=m.chat.id,
                         text=Translation.START.format(m.from_user.first_name, Config.USER_NAME),
                         reply_to_message_id=m.message_id,
                         reply_markup=START_BUTTONS)
    logger.info(f"{m.from_user.first_name} used start command")



@Client.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    await c.send_message(chat_id=m.chat.id,
                         text=Translation.HELP,
                         reply_to_message_id=m.message_id,
                         reply_markup=HTART_BUTTONS,
                         parse_mode="markdown")


@Client.on_message(filters.private & filters.command(["about"]))
async def about(bot, update):
    await c.send_message(chat_id=m.chat.id,
                         text=Translation.ABOUT,
                         disable_web_page_preview=True,
                         reply_to_message_id=m.message_id,
                         reply_markup=ATART_BUTTONS,
                         parse_mode="markdown")

@Client.on_message(filters.private & filters.command(["convtovideo"]))
async def video(bot, update):
    if Config.BOT_PWD:
      if (m.from_user.id not in Config.LOGGED_USER) & (m.from_user.id not in Config.AUTH_USERS):
          await m.reply_text(text=Translation.NOT_LOGGED_TEXT, quote=True)
          return
      else:
          pass
  if m.from_user.id in Config.BANNED_USER:
      await c.send_message(chat_id=m.chat.id, text=Translation.BANNED_TEXT)
      return
  if m.from_user.id not in Config.BANNED_USER:
      if m.reply_to_message is not None:
          await download(c, m)
      else:
          await c.send_message(chat_id=m.chat.id, text=Translation.REPLY_TEXT)

@Client.on_message(filters.private & filters.command(["convtofile"]))
async def file(bot, update):
    if Config.BOT_PWD:
      if (m.from_user.id not in Config.LOGGED_USER) & (m.from_user.id not in Config.AUTH_USERS):
          await m.reply_text(text=Translation.NOT_LOGGED_TEXT, quote=True)
          return
      else:
          pass
  if m.from_user.id in Config.BANNED_USER:
      await c.send_message(chat_id=m.chat.id, text=Translation.BANNED_TEXT)
  if m.from_user.id not in Config.BANNED_USER:
    if m.reply_to_message is not None:
      await download(c, m)
    else:
       await c.send_message(chat_id=m.chat.id, text=Translation.REPLY_TEXT)

@Client.on_message(filters.private & filters.command(["login"]))
async def login(bot, update):
    if Config.BOT_PWD:
        if (len(m.command) >= 2) & (m.from_user.id not in Config.LOGGED_USER) & (m.from_user.id not in Config.AUTH_USERS):
            _, password = m.text.split(" ", 1)
            if str(password) == str(Config.BOT_PWD):
                await c.send_message(chat_id=m.chat.id,
                                     text=Translation.SUCESS_LOGIN,
                                     disable_web_page_preview=True,
                                     reply_to_message_id=m.message_id,
                                     parse_mode="markdown")
                return Config.LOGGED_USER.append(m.from_user.id)
            if str(password) != str(Config.BOT_PWD):
                await c.send_message(chat_id=m.chat.id,
                                     text=Translation.WRONG_PWD,
                                     disable_web_page_preview=True,
                                     reply_to_message_id=m.message_id,
                                     parse_mode="markdown")

        if (len(m.command) < 2) & (m.from_user.id not in Config.LOGGED_USER) & (m.from_user.id not in Config.AUTH_USERS):
            await c.send_message(chat_id=m.chat.id,
                                 text="Use this command for login to this bot. Semd the passwordin the format 👉`/login Bot password`.",
                                 disable_web_page_preview=True,
                                 reply_to_message_id=m.message_id,
                                 parse_mode="markdown")

        if (m.from_user.id in Config.LOGGED_USER)|(m.from_user.id in Config.AUTH_USERS):
            await c.send_message(chat_id=m.chat.id,
                                 text=Translation.EXISTING_USER,
                                 disable_web_page_preview=True,
                                 reply_to_message_id=m.message_id,
                                 parse_mode="markdown")
