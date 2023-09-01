import requests

def send_webhook_message(webhook_url, content):
    data = {
        "content": content
    }
    response = requests.post(webhook_url, json=data)
    
    if response.status_code == 204:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    webhook_url = "YOUR_WEBHOOK_URL_HERE"
    message_content = "Hello from the webhook!"
    send_webhook_message(webhook_url, message_content)
