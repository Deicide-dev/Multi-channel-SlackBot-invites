# Multi-channel-SlackBot-invites


This code is an example of a Python script that adds the same list of email addresses to multiple Slack channels. Here is how the code works:

First, it imports the necessary modules: csv, slack_sdk and re.


The bot prompts the user to enter a list of email addresses separated by commas. This input is assigned to the users variable.


The script then reads the CSV file using the csv.DictReader() method. It loops through each row in the CSV file.


For each row, the script extracts the channel name and adds the list of email addresses (stored in users) to the Slack channel using the client.conversations_invite() method.


The bot prints a message indicating whether the user was successfully added to the channel or whether there was an error.

By using the same list of email addresses for all the rows, the bot reduces the need for the user to repeatedly enter the same list of email addresses for each channel.
