# Octobot, a Discord bot that does things

Everybody loves Octobot!

### ⚙️ Commands & Options

#### `/flip`

Flips Octo from Angry to Happy and back, displaying a happy or angry octopus image. (Requires the Server Octopus role and permissions to edit it!)

#### `/tiktok [url]`

Downloads and reposts tiktok URLs!

### 🐳 Docker-way to quick start

The bot needs `bot` and `applications.commands` discord permissions and (obviously) to be joined to the server. First, edit your `.env` file, add in your discord token, guild IDs corresponding to the servers it should listen in, and a logdir:

```bash
TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 
LOGDIR=logs
GUILD_IDS=1234567890123,98765432123456
```

Then Build it:

```bash
docker-compose build
```

And Run it:

 ```bash
docker-compose up
```


