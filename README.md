
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

Create a .env file and add 
```sh
BOT_TOKEN=<token from the discord developer portal>
```

### No docker version

Create virtual environment.
```sh
python3 -m venv .venv
source .venv/bin/activate
```

Download dependecies.
```sh
python3 -m pip -r requirements.txt
```

Start bot.
```sh
python3 src/main.py
```

After initial installation only do
```sh
source .venv/bin/activate
python3 src/main.py
```

### Docker version

Create docker image.
```sh
docker build . -t discord-bot
```

Run docker container.
```sh
docker run -d --name discord-bot discord-bot:latest
```

After initial installation only do
```sh
docker start discord-bot
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
