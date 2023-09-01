# Remove the # on Time and interval_seconds if you want to wait a little before sending another message

# Also the reason for inport random is because of raid protection. So lets say your message is 'Hi' then it will add 'Hi (RandomNumbersAndStringsHere)'

import requests
import random
import string
#import time

def send_randomized_message(webhook_url, content):
    random_chars = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
    randomized_content = f"{content} {random_chars}"
    
    data = {
        "content": randomized_content
    }
    response = requests.post(webhook_url, json=data)
    
    if response.status_code == 204:
        print(f"Message sent successfully: {randomized_content}")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    webhook_url = "YOUR_WEBHOOK_URL_HERE"
    message_content = "Hello from the webhook!"
    #interval_seconds = 5  # Adjust the interval as needed (e.g., 5 seconds)
    
    while True:
        send_randomized_message(webhook_url, message_content)
        time.sleep(interval_seconds)
