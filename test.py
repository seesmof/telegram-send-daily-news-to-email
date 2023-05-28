import telethon
TOKEN = "6055667715:AAGlgPKBJftI_Cks1m8n9n_rSpqhN5bXrzg"
CHANNEL_ID = "@mindua"
APP_ID = "29709258"
APP_HASH = "545b92e022b3885152a76625cd74c9d5"
TO_LOOK_FOR = "#фотодня"


# Create a Telegram client object
client = telethon.TelegramClient(
    'my_bot', api_id=APP_ID, api_hash=APP_HASH)

# Connect to the Telegram servers
client.connect()

# Get the channel ID
channel_id = CHANNEL_ID

# Start monitoring the channel for messages with the specific string
while True:
    # Get the latest messages from the channel
    messages = client.get_messages(channel_id)

    # For each message, check if it contains the specific string
    for message in messages:
        if message.text == TO_LOOK_FOR:
            # If the message contains the specific string, forward it to your account
            client.forward_messages(message.chat_id, message.id)

# Keep monitoring the channel for messages
