import os
import logging
from datetime import datetime

from dotenv import load_dotenv

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)


# ============================================================
# CONFIGURATION
# ============================================================

load_dotenv()

BOT_TOKEN = os.getenv("8558535921:AAF3LTg-aWyOU3hgA_d2XQL63O7Ttddlx1M")

if not BOT_TOKEN:
    raise RuntimeError(
        "BOT_TOKEN is missing. Put your Telegram bot token "
        "inside the .env file."
    )


BOT_NAME = "VXmachine"


# ============================================================
# LOGGING
# ============================================================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


# ============================================================
# START
# ============================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    first_name = user.first_name if user else "Friend"

    keyboard = [
        [
            InlineKeyboardButton(
                "📚 Features",
                callback_data="features"
            ),
            InlineKeyboardButton(
                "ℹ️ About",
                callback_data="about"
            ),
        ],
        [
            InlineKeyboardButton(
                "🆔 My ID",
                callback_data="my_id"
            ),
            InlineKeyboardButton(
                "🕐 Time",
                callback_data="time"
            ),
        ],
        [
            InlineKeyboardButton(
                "❓ Help",
                callback_data="help"
            ),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    message = (
        f"👋 Hello {first_name}!\n\n"
        f"🤖 Welcome to *{BOT_NAME}*.\n\n"
        "Your simple multi-function Telegram assistant.\n\n"
        "Choose an option below 👇"
    )

    await update.message.reply_text(
        message,
        parse_mode="Markdown",
        reply_markup=reply_markup,
    )


# ============================================================
# HELP
# ============================================================

async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = (
        "🤖 *VXmachine Commands*\n\n"

        "/start — Start the bot\n"
        "/help — Show help\n"
        "/about — About VXmachine\n"
        "/id — Show your Telegram ID\n"
        "/time — Current date & time\n"
        "/echo <text> — Repeat your text\n"
        "/menu — Open main menu\n\n"

        "You can also use the buttons below."
    )

    await update.message.reply_text(
        text,
        parse_mode="Markdown",
    )


# ============================================================
# ABOUT
# ============================================================

async def about_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = (
        "🤖 *VXmachine*\n\n"
        "A Python-based Telegram bot.\n\n"
        "⚡ Fast\n"
        "🧩 Modular\n"
        "🔐 Token protected\n"
        "📱 Termux compatible\n"
        "🐙 GitHub ready\n\n"
        "More features can be added later."
    )

    await update.message.reply_text(
        text,
        parse_mode="Markdown",
    )


# ============================================================
# USER ID
# ============================================================

async def id_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user
    chat = update.effective_chat

    text = (
        "🆔 *Your Telegram Information*\n\n"
        f"User ID: `{user.id}`\n"
        f"Chat ID: `{chat.id}`\n"
        f"Username: @{user.username if user.username else 'Not set'}"
    )

    await update.message.reply_text(
        text,
        parse_mode="Markdown",
    )


# ============================================================
# TIME
# ============================================================

async def time_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    now = datetime.now()

    text = (
        "🕐 *Current Server Time*\n\n"
        f"Date: `{now.strftime('%d-%m-%Y')}`\n"
        f"Time: `{now.strftime('%I:%M:%S %p')}`"
    )

    await update.message.reply_text(
        text,
        parse_mode="Markdown",
    )


# ============================================================
# ECHO
# ============================================================

async def echo_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if not context.args:

        await update.message.reply_text(
            "Usage:\n\n"
            "`/echo Hello VXmachine`",
            parse_mode="Markdown",
        )

        return

    text = " ".join(context.args)

    await update.message.reply_text(
        f"🔁 {text}"
    )


# ============================================================
# MENU
# ============================================================

async def menu_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    keyboard = [
        [
            InlineKeyboardButton(
                "📚 Features",
                callback_data="features"
            )
        ],
        [
            InlineKeyboardButton(
                "ℹ️ About",
                callback_data="about"
            ),
            InlineKeyboardButton(
                "🆔 My ID",
                callback_data="my_id"
            ),
        ],
        [
            InlineKeyboardButton(
                "🕐 Time",
                callback_data="time"
            ),
            InlineKeyboardButton(
                "❓ Help",
                callback_data="help"
            ),
        ],
    ]

    await update.message.reply_text(
        "🤖 *VXmachine Menu*\n\nSelect an option:",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


# ============================================================
# FEATURES
# ============================================================

async def features_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = (
        "📚 *VXmachine Features*\n\n"

        "✅ Start command\n"
        "✅ Help system\n"
        "✅ Inline buttons\n"
        "✅ User ID\n"
        "✅ Date & time\n"
        "✅ Echo command\n"
        "✅ Menu navigation\n"
        "✅ Error handling\n\n"

        "🚀 More modules can be added later."
    )

    await update.message.reply_text(
        text,
        parse_mode="Markdown",
    )


# ============================================================
# BUTTON HANDLER
# ============================================================

async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()

    user = query.from_user

    if query.data == "features":

        text = (
            "📚 *VXmachine Features*\n\n"
            "✅ Commands\n"
            "✅ Inline buttons\n"
            "✅ User information\n"
            "✅ Time system\n"
            "✅ Echo system\n"
            "✅ Modular architecture"
        )

    elif query.data == "about":

        text = (
            "ℹ️ *About VXmachine*\n\n"
            "VXmachine is a Python Telegram bot "
            "designed with a modular structure."
        )

    elif query.data == "my_id":

        text = (
            "🆔 *Your Telegram ID*\n\n"
            f"User ID: `{user.id}`"
        )

    elif query.data == "time":

        now = datetime.now()

        text = (
            "🕐 *Current Time*\n\n"
            f"`{now.strftime('%d-%m-%Y %I:%M:%S %p')}`"
        )

    elif query.data == "help":

        text = (
            "❓ *Help*\n\n"
            "/start\n"
            "/help\n"
            "/about\n"
            "/id\n"
            "/time\n"
            "/echo\n"
            "/menu"
        )

    else:

        text = "Unknown option."

    await query.edit_message_text(
        text,
        parse_mode="Markdown",
    )


# ============================================================
# NORMAL TEXT MESSAGE
# ============================================================

async def text_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    message = update.message.text.strip()

    if not message:
        return

    await update.message.reply_text(
        "👋 I received your message.\n\n"
        "Use /menu to see what I can do."
    )


# ============================================================
# ERROR HANDLER
# ============================================================

async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE
):

    logger.error(
        "Exception while processing update:",
        exc_info=context.error,
    )


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 45)
    print("        VXmachine Telegram Bot")
    print("=" * 45)
    print("Bot is starting...")
    print("Press CTRL+C to stop.")
    print("=" * 45)

    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )

    # Commands
    application.add_handler(
        CommandHandler("start", start)
    )

    application.add_handler(
        CommandHandler("help", help_command)
    )

    application.add_handler(
        CommandHandler("about", about_command)
    )

    application.add_handler(
        CommandHandler("id", id_command)
    )

    application.add_handler(
        CommandHandler("time", time_command)
    )

    application.add_handler(
        CommandHandler("echo", echo_command)
    )

    application.add_handler(
        CommandHandler("menu", menu_command)
    )

    application.add_handler(
        CommandHandler("features", features_command)
    )

    # Inline buttons
    application.add_handler(
        CallbackQueryHandler(button_handler)
    )

    # Normal messages
    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            text_message
        )
    )

    # Error handler
    application.add_error_handler(
        error_handler
    )

    # Start polling
    application.run_polling(
        allowed_updates=Update.ALL_TYPES
    )


if __name__ == "__main__":
    main()
