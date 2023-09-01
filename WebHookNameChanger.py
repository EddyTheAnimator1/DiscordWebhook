# Edit Webhook Name
import requests

def edit_webhook_name(webhook_url, new_name):
    data = {
        "name": new_name
    }
    response = requests.patch(webhook_url, json=data)
    
    if response.status_code == 200:
        print("Webhook name updated successfully.")
    else:
        print(f"Failed to update webhook name. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    webhook_url = "YOUR_WEBHOOK_URL_HERE"
    new_name = "New Webhook Name"
    edit_webhook_name(webhook_url, new_name)
