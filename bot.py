import csv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import re

# Replace with your bot's token
client = WebClient(token="YOUR_BOT_TOKEN")

# Regular expression pattern for matching email addresses
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Read the CSV file
with open("channels.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    # Prompt the user for a comma-separated list of email addresses to add to all channels
    users = input("Enter comma-separated list of email addresses to add to all channels: ").split(",")
    # Loop through each row in the CSV file
    for row in reader:
        channel = row["Channel Name"]
        # Add each user to the channel
        for user in users:
            if re.match(email_pattern, user.strip()):
                try:
                    response = client.conversations_invite(channel=channel, users=[user.strip()])
                    print("User added to channel:", response["channel"]["name"])
                except SlackApiError as e:
                    print("Error adding user to channel:", e)
            else:
                print("Invalid email address:", user.strip())