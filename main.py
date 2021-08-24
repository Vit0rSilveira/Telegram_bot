from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from telegram.ext.messagequeue import queuedmessage
import dontpad
import os
from dotenv import load_dotenv
import datetime

load_dotenv('ignore/.env')

TOKEN = os.getenv("TOKEN_BOT")
CHAT = os.getenv("CHAT_ID")

guardarDia = 0
quandoMandar = 0

def informacao(update, context):
    s = """Digite /provas para ver as datas das provas.
Digite /trabalhos para ver as datas dos trabalhos.
Digite /runCodes para ver a data de entrega do run codes"""
    update.message.reply_text(s)


def informacaoAulas(update, context):
    messageId = update.message.message_id
    chatId = update.message.chat_id
    mensagem = dontpad.read("informacaoAulasBCC021")
    context.bot.sendMessage(chat_id = chatId, text = mensagem, reply_to_message_id = messageId)

    if chatId == int(CHAT):
        mensagem = "Para editar clique [aqui](http://dontpad.com/informacaoAulasBCC021)"
        context.bot.sendMessage(chat_id = chatId, text = mensagem, parse_mode = "MarkdownV2")


def addProvas(update, context):
    messageId = update.message.message_id
    chatId = update.message.chat_id
    mensagem = dontpad.read("provasBCC021")
    context.bot.sendMessage(chat_id = chatId, text = mensagem, reply_to_message_id = messageId)

    if chatId == int(CHAT):
        mensagem = "Para editar clique [aqui](http://dontpad.com/provasBCC021)"
        context.bot.sendMessage(chat_id = chatId, text = mensagem, parse_mode = "MarkdownV2")


def addTrabalhos(update, context):
    messageId = update.message.message_id
    chatId = update.message.chat_id
    mensagem = dontpad.read("trabalhosBCC021")
    context.bot.sendMessage(chat_id = chatId, text = mensagem, reply_to_message_id = messageId)

    if chatId == int(CHAT):
        mensagem = "Para editar clique [aqui](http://dontpad.com/trabalhosBCC021)"
        context.bot.sendMessage(chat_id = chatId, text = mensagem, parse_mode = "MarkdownV2")


def addExercicios(update, context):
    messageId = update.message.message_id
    chatId = update.message.chat_id
    mensagem = dontpad.read("exerciciosBCC021")
    context.bot.sendMessage(chat_id = chatId, text = mensagem, reply_to_message_id = messageId)

    if chatId == int(CHAT):
        mensagem = "Para editar clique [aqui](http://dontpad.com/exerciciosBCC021)"
        context.bot.sendMessage(chat_id = chatId, text = mensagem, parse_mode = "MarkdownV2")



def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO
    )

    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("info", informacao))
    dp.add_handler(CommandHandler("aulas", informacaoAulas))
    dp.add_handler(CommandHandler("provas", addProvas))
    dp.add_handler(CommandHandler("trabalhos", addTrabalhos))
    dp.add_handler(CommandHandler("runcodes", addExercicios))

    updater.start_polling()
    logging.info("=== Bot running! ===")
    updater.idle()
    logging.info("=== Bot shutting down! ===")

if __name__ == "__main__":
    main()