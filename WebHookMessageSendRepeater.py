import requests
import random
import string

def send_randomized_message(webhook_url, content):
    # Generate a random string of letters and numbers
    random_chars = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
    
    # Add the random string to the content
    randomized_content = f"{content} {random_chars}"
    
    data = {
        "content": randomized_content
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
    send_randomized_message(webhook_url, message_content)
