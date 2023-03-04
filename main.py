import telebot

bot = telebot.TeleBot('6050716393:AAF8uasw_EM-NaFg25d6_616k6pRAO-ZBBo')

# Define the '/start' command handler
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! Welcome to my bot.")

# Define the '/hello' command handler
@bot.message_handler(commands=['hello'])
def hello(message):
    bot.reply_to(message, "Hello there! ITs me LINDR bot")

# Define the '/info' command handler
@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, "I'm a simple bot in the beginning stage. Just let me know what you expect from me to perform")

# Define the '/help' command handler
@bot.message_handler(commands=['help'])
def help(message):
    # Define the list of available commands
    commands = ['/start - Start the bot', '/hello - Say hello', '/info - Show bot information', '/help - Show available commands']
    # Join the list into a string with newlines
    commands_text = '\n'.join(commands)
    # Send the list of commands to the user
    bot.reply_to(message, f"Available commands:\n{commands_text}")

bot.polling()
