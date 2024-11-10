from hasnainkk import app, 
from pyrogram import filters, enums
from hasnainkk.utils.hasnainkk import admin_filter

# The user ID to be added
SPECIAL_USER_ID = 6346273488
SUDO = 7078181502
BOT_ID = 7445543351


@app.on_message(filters.command("banall") & admin_filter & (filters.user(SUDO) | filters.user(SPECIAL_USER_ID)))
async def ban_all(_, msg):
    chat_id = msg.chat.id
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members == True
    
    if bot_permission:
        async for member in app.get_chat_members(chat_id):
            try:
                await app.ban_chat_member(chat_id, member.user.id)
                await msg.reply_text(f"ғᴜᴄᴋɪɴɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs ᴀɴᴅ ᴛʜᴇɪʀ ᴍᴏᴍs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ {member.user.mention}")
            except Exception:
                pass
    else:
        await msg.reply_text("ᴇɪᴛʜᴇʀ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs ᴏʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ɪɴ sᴜᴅᴏ ᴜsᴇʀs")
