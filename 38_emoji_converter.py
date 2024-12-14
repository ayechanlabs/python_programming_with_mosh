text_to_emoji = {
    ":)": "😊",
    ":(": "😔"
}

message = input("> ")

msg_list = message.split(" ")

emoji_msg = ""
for item in msg_list:
    emoji_msg += text_to_emoji.get(item, item) + " "

print(emoji_msg)
