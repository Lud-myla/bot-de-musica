import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎧 Bot conectado!\n\n"
        "Estou acordado. Agora vamos me transformar em um player de música."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 Comandos disponíveis:\n\n"
        "/start - Iniciar o bot\n"
        "/help - Mostrar ajuda"
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot iniciado!")
    app.run_polling()


if __name__ == "__main__":
    main()
