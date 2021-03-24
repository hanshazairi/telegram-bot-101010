import api
import constants
from telegram.ext import Updater, CommandHandler
from keep_alive import keep_alive

token = constants.token

def start(update, context):
  chat_id = update.effective_chat.id
  context.bot.send_message(chat_id, 'Hi!')

def help(update, context):
  chat_id = update.effective_chat.id
  text = ('/start - Says \'Hi!\'.\n'
  '/help - Shows available commands.\n'
  '/ichooseyou - Returns pokémon sprite.\n'
  '/joke - Tells a joke.')
  context.bot.send_message(chat_id, text)

def ichooseyou(update, context):
  chat_id = update.effective_chat.id
  pokemon = api.get_pokemon('charizard')
  context.bot.send_photo(chat_id, pokemon)

def joke(update, context):
  chat_id = update.effective_chat.id
  joke = api.get_joke()
  context.bot.send_message(chat_id, joke)

def main():
  updater = Updater(token)
  dp = updater.dispatcher
  dp.add_handler(CommandHandler('start', start))
  dp.add_handler(CommandHandler('help', help))
  dp.add_handler(CommandHandler('ichooseyou', ichooseyou))
  dp.add_handler(CommandHandler('joke', joke))
  keep_alive()
  updater.start_polling()
  print('101010 Bot is live.')
  updater.idle()

if __name__ == '__main__':
  main()