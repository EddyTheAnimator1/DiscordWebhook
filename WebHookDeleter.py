import requests

def delete_webhook(webhook_url):
    response = requests.delete(webhook_url)
    
    if response.status_code == 204:
        print("Webhook deleted successfully.")
    else:
        print(f"Failed to delete webhook. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    webhook_url = "YOUR_WEBHOOK_URL_HERE"
    delete_webhook(webhook_url)
