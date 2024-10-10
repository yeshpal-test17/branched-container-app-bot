from dotenv import load_dotenv
import os
from pyrogram import Client, filters, idle
import logging
from flask_app import app
import threading


# Load environment variables from .env file
load_dotenv()

# Get the RELEASE_TAG from environment variables
RELEASE_TAG = os.getenv('RELEASE_TAG', 'Unknown')

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

STAGE = os.getenv("STAGE")
PORT = 8080 if STAGE == "prod" else 800  # Use different ports based on the stage

#MAIN_MENU_TEXT = os.getenv("main_menu_text")

def init_bot():
    return Client(
    "yeshpal_bot",
    bot_token=BOT_TOKEN, 
    api_id=API_ID,
    api_hash=API_HASH
)

# Initialize the bot instance
bot = init_bot()


# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Add a stream handler to write logs to the console
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

logging.info("Starting bot.py")
logger.info("Starting bot.py")

# Start command
@bot.on_message(filters.command("start") & filters.private)
def start_command(client, message):
    user_id = message.chat.id
    #bot.send_message(user_id, f" Hello and Welcome to my bot !!!  {user_id} NON STAGED MESSAGE NEW DEPLOYMENT stage variable {STAGE} ")
    logger.info(f'Start button has been clicked by the user NEW DEPLOYMENT  {user_id} stage variable {STAGE} and Port {PORT}')
    if STAGE == "dev":
        bot.send_message(user_id, f" Hello and Welcome to my bot !!! Port {PORT} and RELEASE tag {RELEASE_TAG} and stage {STAGE} ")
        
    if STAGE == "prod":
        bot.send_message(user_id, f" Hello and Welcome to my bot  !!!  {user_id} and port {PORT} and stage {STAGE}")



if __name__ == "__main__":
    logger.info("Flask client started")
    # Start the Flask app in a separate thread
    flask_thread = threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': PORT})
    flask_thread.start()
    
    logger.info("Telegram bot started")
    # Run the Telegram bot
    bot.start()
    logger.info("Bot started, now running idle")
    idle()