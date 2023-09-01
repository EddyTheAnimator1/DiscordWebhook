# Edit Webhook Avatar
import requests

def edit_webhook_avatar(webhook_url, new_avatar_url):
    data = {
        "avatar_url": new_avatar_url
    }
    response = requests.patch(webhook_url, json=data)
    
    if response.status_code == 200:
        print("Webhook avatar updated successfully.")
    else:
        print(f"Failed to update webhook avatar. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    webhook_url = "YOUR_WEBHOOK_URL_HERE"
    new_avatar_url = "URL_TO_NEW_AVATAR_IMAGE"
    edit_webhook_avatar(webhook_url, new_avatar_url)
