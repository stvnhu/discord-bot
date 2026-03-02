
## Discord Bot

A discord bot that adds chat commands to a discord server.

## Features

- Can ask ChatGPT questions through discord. ( feature deprecated after gpt-4o-mini was retired )
- Plays youtube audio on voice channel.

## Installation

Clone the git repo.
```sh
git clone https://github.com/stvnhu/discord-bot.git
```

Create virtual environment.
```sh
python3 -m venv .venv
source .venv/bin/activate
```

Download dependecies.
```sh
python3 -m pip -r requirements.txt
```

Create a .env file and add 
```sh
BOT_TOKEN=
```

Start bot.
```sh
python3 src/main.py
```

## Used libraries

- pathlib
- dotenv
- discord.py
- re
- openai
- base64
- io
- yt_dlp
