import telebot
from telebot import types
import re
import utils

# Telegram Bot API token
TOKEN = 'your_token_here'

# Create a new bot instance
bot = telebot.TeleBot(TOKEN)

# A dictionary to store registered users' data
users = {}

# A dictionary to store datewise transaction and food data
dates_data = {}


# Handler for /start command
@bot.message_handler(commands=['start'])
def start_handler(message):
    # Check if user is already registered
    if message.from_user.id in users:
        bot.send_message(message.chat.id, "You are already registered!")
    else:
        # Add user to the users dictionary with default data
        users[message.chat.id] = utils.register("bot_user", "bot_pass")["id"]
        bot.send_message(message.chat.id, "Welcome to NevskiyioBot!")


# Handler for text messages
@bot.message_handler(func=lambda message: True)
def text_handler(message):
    # Check if user is registered
    if message.from_user.id not in users:
        bot.send_message(message.chat.id, "Please register first using /start command.")
    else:
        user_data = users[message.from_user.id]
        # Get user's current registration status
        if not user_data['name']:
            user_data['name'] = message.text
            bot.send_message(message.chat.id, "Please enter your age:")
        elif not user_data['age']:
            user_data['age'] = message.text
            bot.send_message(message.chat.id, "Please enter your height in cm:")
        elif not user_data['height']:
            user_data['height'] = message.text
            bot.send_message(message.chat.id, "Please enter your weight in kg:")
        elif not user_data['weight']:
            user_data['weight'] = message.text
            # Registration complete, show the main menu
            show_main_menu(message)


# Function to show the main menu
def show_main_menu(message):
    # Create the main menu keyboard
    keyboard = types.InlineKeyboardMarkup()
    training_button = types.InlineKeyboardButton(text="Add Training to Date", callback_data="add_training")
    food_button = types.InlineKeyboardButton(text="Add Food to Date", callback_data="add_food")
    transaction_button = types.InlineKeyboardButton(text="Get Transactions for Date", callback_data="get_transaction")
    food_data_button = types.InlineKeyboardButton(text="Get Food Data for Date", callback_data="get_food_data")
    keyboard.add(training_button, food_button)
    keyboard.add(transaction_button, food_data_button)
    bot.send_message(message.chat.id, "Please select an option from the menu:", reply_markup=keyboard)


# Callback handler for main menu buttons
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "add_training":
        add_training_handler(call.message)
    elif call.data == "add_food":
        add_food_handler(call.message)
    elif call.data == "get_transaction":
        get_transaction_handler(call.message)
    elif call.data == "get_food_data":
        get_food_data_handler(call.message)


# Handler for adding training data
def add_training_handler(message):
    # Ask user for the date
    bot.send_message(message.chat.id, "Please enter the date for training data (dd-mm-yyyy):")
    bot.register_next_step_handler(message, add_training_date)


def add_training_date(message):
    date = message.text
    # Check if the date is valid
    if re.match(date, r"..\...\....."):
        dates_data[message.chat.id] = date
        bot.send_message(message.chat.id, "Please enter the name and duration of train (train - duration):")
        bot.register_next_step_handler(message, add_train)


def add_train(message):
    train = message.text
    if train:
        utils.add_train(users[message.chat.id], train, dates_data[message.chat.id])
    bot.send_message(message.chat.id, "train added succesfully")


def add_food_handler(message):
    # Ask user for the date
    bot.send_message(message.chat.id, "Please enter the date for food (dd-mm-yyyy):")
    bot.register_next_step_handler(message, add_food_date)


def add_food_date(message):
    date = message.text
    # Check if the date is valid
    if re.match(date, r"..\...\....."):
        dates_data[message.chat.id] = date
        bot.send_message(message.chat.id, "Please enter the name and b, j, u, kkal (name - b, j, u, kkal):")
        bot.register_next_step_handler(message, add_food)


def add_food(message):
    food = message.text
    if food:
        utils.add_train(users[message.chat.id], food, dates_data[message.chat.id])
    bot.send_message(message.chat.id, "food added succesfully")


def get_transaction_handler(message):
    bot.send_message(message.chat.id, "Please enter the date for training data (dd-mm-yyyy):")
    bot.register_next_step_handler(message, transaction)

def transaction(message):
    date = message.text

    if re.match(date, r"..\...\....."):
        bot.send_message(message.chat.id, utils.get_trains(message.chat.id, date))


def get_food_data_handler(message):
    bot.send_message(message.chat.id, "Please enter the date for food (dd-mm-yyyy):")
    bot.register_next_step_handler(message, get_food)

def get_food(message):
    date = message.text

    if re.match(date, r"..\...\....."):
        bot.send_message(message.chat.id, utils.get_food(message.chat.id, date))

