import logging
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,CallbackContext,Dispatcher
from telegram import Update,Bot 
from flask import Flask,request


#Setting up Logging here
logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',level = logging.INFO)
logger = logging.getLogger(__name__) #Creating a logger object

#Token for telegram bot generated from BotFather
TOKEN = "5436065265:AAEc-K_d4oo_VyXZn_Ay-N46hsuLV5py-58"

#Creating a flask object
app = Flask(__name__)

@app.route(f'/{TOKEN}',methods=['GET','POST'])
def webhook():
	update =Update.de_json(request.get_json(),bot)
	dp.process_update(update)
	return "ok"

def start(update:Update,context:CallbackContext):
	context.bot.send_message(chat_id=update.message.chat_id,text="HELLO!!!!!")

def _help(update:Update,context:CallbackContext):
	context.bot.send_message(chat_id=update.message.chat_id,text="This is the help section")

def echo_text(update:Update,context:CallbackContext):
	context.bot.send_message(chat_id=update.message.chat_id,text=update.message.text)

def error(bot,update):
	logger.error("Update'%s' caused error '%s' ",update,update.error)

bot = Bot(TOKEN)
bot.set_webhook("https://4322-118-200-111-244.ap.ngrok.io/"+TOKEN)
#Creating a dispatcher object from a bot
dp = Dispatcher(bot,None)

dp.add_handler(CommandHandler("start",start))
dp.add_handler(CommandHandler("help",_help))
dp.add_handler((MessageHandler(Filters.text,echo_text)))
dp.add_error_handler(error)

	

if __name__ == '__main__':
	app.run(port=8443)
