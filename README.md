# Multi-channel-SlackBot-invites

To create a bot in Slack, follow these steps:


Log in to your Slack workspace.

Navigate to the Slack API homepage: https://api.slack.com/

Click on the "Create a Slack App" button in the top right corner of the page.

Give your app a name and choose the workspace where you want to install it.

Navigate to the "Bot Users" section of the app dashboard and click on the "Add a Bot User" button. Give your bot a name and click "Add Bot User".

In the "Install App" section of the app dashboard, click on the "Install App" button to install the app in your workspace.

Note down the "Bot User OAuth Access Token" - this is the token you'll use to authenticate your bot.

Finally, navigate to the "Event Subscriptions" section of the app dashboard, and toggle the "Enable Events" switch to "On". Enter the request URL for your bot in the "Request URL" field. This is the URL where your bot will receive events from Slack.

That's it! Your bot is now ready to use. You can start building it by writing a script that uses the Slack API to send and receive messages.



This code is an example of a Python script that adds the same list of email addresses to multiple Slack channels. Here is how the code works:

First, it imports the necessary modules: csv, slack_sdk and re.


The bot prompts the user to enter a list of email addresses separated by commas. This input is assigned to the users variable.


The script then reads the CSV file using the csv.DictReader() method. It loops through each row in the CSV file.


For each row, the script extracts the channel name and adds the list of email addresses (stored in users) to the Slack channel using the client.conversations_invite() method.


The bot prints a message indicating whether the user was successfully added to the channel or whether there was an error.

By using the same list of email addresses for all the rows, the bot reduces the need for the user to repeatedly enter the same list of email addresses for each channel.
