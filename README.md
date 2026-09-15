# VXmachine 🤖

VXmachine is a Python Telegram bot with a modular command and
inline-button system.

## Features

- /start
- /help
- /about
- /id
- /time
- /echo
- /menu
- /features
- Inline buttons
- Error handling
- Environment-variable token
- GitHub-ready structure
- Termux compatible

## Project Structure

VXmachine/
│
├── bot.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

## Installation

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

Enter the folder:

cd VXmachine

Install dependencies:

pip install -r requirements.txt

## Configure Token

Create a file named:

.env

Add:

BOT_TOKEN=YOUR_NEW_BOT_TOKEN

Never upload the .env file to GitHub.

## Run

python bot.py

You should see:

VXmachine Telegram Bot
Bot is starting...

Then open your bot in Telegram and send:

/start

## Commands

/start
/help
/about
/id
/time
/echo Hello
/menu
/features

## Security

Never publish your Telegram bot token.

If a token is exposed, revoke/regenerate it using BotFather
and replace the old token.

## License

For educational and personal development use.
