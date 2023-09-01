import requests

def delete_webhook(webhook_url):
    response = requests.delete(webhook_url)
    
    if response.status_code == 204:
        print("Webhook deleted successfully.")
    else:
        print(f"Failed to delete webhook. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    webhook_url = "https://discord.com/api/webhooks/1147182229013930116/jDv7yb04ZlMSki4jEwghnKS6gDYikG8B6SDawYtlJR4r4GdtFxKVj9EVeFAOu-aWtgCf"
    delete_webhook(webhook_url)
