import requests

bot_token = "7385634728:AAG-twcqVUOFRdqa38G7EAZQlbhN2mO3E8E"
url = f"https://api.telegram.org/bot{bot_token}/getUpdates"

response = requests.get(url)
updates = response.json()

# Если канал добавлен, сообщения будут в списке updates
for update in updates["result"]:
    print(update)
