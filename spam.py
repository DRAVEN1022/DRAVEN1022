import requests
import json
from colorama import Fore

def send_message(webhookurl, content, times):
    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        'content': content,
    }

    for  in range(times):
        response = requests.post(webhook_url, headers=headers, data=json.dumps(data))

        if response.statuscode == 204:
            print(f"{Fore.GREEN}[ .gg/nuker-x  ] {  + 1 } Message  {message_content}  sent successfully!")
        else:
            print(f"{Fore.RED}[ .gg/nuker-x ] Failed to send message. Status code: {response.status_code}")

if name == "main":
    webhook_url = input("ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴡᴇʙʜᴏᴏᴋ ʟɪɴᴋ : ")
    message_content = input("ᴇɴᴛᴇʀ ᴍᴇꜱꜱᴀɢᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ꜱᴇɴᴅ : ")
    message_count = int(input("ᴇɴᴛᴇʀ ɴᴜᴍʙᴇʀ ᴏꜰ ᴍᴇꜱꜱᴀɢᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ꜱᴇɴᴅ : "))

    send_message(webhook_url, message_content, message_count)
