# AvicBotTwitch

A fun, interactive Twitch IRC chat bot written in Python. Originally created in 2015, completely rewritten for Python 3.10+ in 2026.

## Features

- 🤖 **Chat Commands** - Respond to `!say`, `!sing`, `!random`, `!commands`, and more
- 🎬 **Movie Quotes** - Matrix references and other classic movie responses
- 🎮 **Game References** - Portal game easter eggs ("The cake is a lie!")
- 🎵 **Song Triggers** - Responds with lyrics when keywords are detected
- 🎭 **Musical Theater** - Full Major-General song and other musical references
- 🔗 **Link Commands** - Quick links to XKCD comics and YouTube videos
- 🍺 **Fun Commands** - Give virtual beers to chat members
- 📢 **Echo Feature** - Repeat messages with the `!say` command

## Requirements

- Python 3.10 or higher
- A Twitch account for the bot
- OAuth token from [Twitch TMI](https://twitchapps.com/tmi/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Avicennasis/AvicBotTwitch.git
   cd AvicBotTwitch
   ```

2. Configure your OAuth token in `twitchconfig.py`:
   ```python
   PASS = "oauth:your_token_here"
   ```

3. Update bot settings in `twitch.py` (optional):
   - `BotConfig.NICK` - Bot's display name
   - `BotConfig.CHANNEL` - Channel to join (include #)
   - `BotConfig.MASTER` - Your username

## Usage

Run the bot:
```bash
python twitch.py
```

The bot will connect to Twitch IRC and join the configured channel automatically.

## Commands

| Command | Description |
|---------|-------------|
| `!say <text>` | Echo text back to chat |
| `!sing` | Sing "Daisy Bell" |
| `!random` | Returns a random number |
| `!commands` | List all commands |
| `!xkcd <num>` | Link to XKCD comic |
| `!youtube <id>` | Link to YouTube video |
| `!beer <user>` | Give a beer to someone |
| `!die <botname>` | Shut down the bot |

## Trigger Words

The bot responds to various keywords in chat, including:
- Portal references: `cake`, `portal`, `lemons`
- Movies: `matrix`
- Music: `rainbow`, `duck`, `shiny`
- Chat expressions: `lol`, `yay`, `crazy`
- And many more!

## Project Structure

```
AvicBotTwitch/
├── twitch.py        # Main bot script
├── twitchconfig.py  # Configuration (OAuth token)
├── README.md        # This file
├── LICENSE          # MIT License
└── .gitignore       # Git ignore rules
```

## License

MIT License

Copyright (c) 2026 Léon "Avic" Simmons

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Credits

**Author:** Léon "Avic" Simmons ([@Avicennasis](https://github.com/Avicennasis))

Originally created in 2015, modernized for Python 3.10+ in 2026.
