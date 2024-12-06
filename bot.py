from dotenv import load_dotenv
import os
from pyrogram import Client, filters, idle
import logging
from flask_app import app
import threading

# Load environment variables from .env file
load_dotenv()

# Get the environment variables
RELEASE_TAG = os.getenv('RELEASE_TAG', 'Unknown')
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
STAGE = os.getenv("STAGE", "dev")
PORT = 3001 if STAGE == "prod" else 8080
#PORT = 8080

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

# Start command
@bot.on_message(filters.command("start") & filters.private)
def start_command(client, message):
    user_id = message.chat.id
    logger.info(f'Start command received from user {user_id}')
    logger.info(f'Environment: STAGE={STAGE}, PORT={PORT}, RELEASE_TAG={RELEASE_TAG}')
    
    response_message = f"Hello and Welcome to my bot! 🤖\n\n"
    response_message += f"Environment: {STAGE}\n"
    response_message += f"Release: {RELEASE_TAG}\n"
    response_message += f"Port: {PORT}"
    
    logger.info(f'Sending response: {response_message}')
    bot.send_message(user_id, response_message)

if __name__ == "__main__":
    logger.info("Starting bot application")
    logger.info(f"Configuration: STAGE={STAGE}, PORT={PORT}, RELEASE_TAG={RELEASE_TAG}")
    
    # Start the Flask app in a separate thread
    flask_thread = threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': PORT})
    flask_thread.start()
    logger.info(f"Flask app started on port {PORT}")
    
    # Run the Telegram bot
    logger.info("Starting Telegram bot")
    bot.start()
    logger.info(f"Bot started successfully. Version: {RELEASE_TAG}")
    idle()