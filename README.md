# Delete Telegram Channel Messages
A script written in Pyrogram framework to mass delete messages from a Telegram channel. Requires a Session String of an admin with Delete Messages permission in the required channel.

## Steps

### 1) Get Session String

Use a bot like <a href="https://t.me/SessionStringGeneratorRobot">@SessionStringGeneratorRobot</a> or run the python file `gen_session_string.py` provided in this repository.

### 2) Fill variables in config.env

A sample `config.env` has been provided. First, you need to fill in all variables.

### 3) Run the script

``` bash
python3 main.py
```

## Libraries Used

- Pyrogram

## Credits

- <a href="https://github.com/dakshy">dakshy</a>