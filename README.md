# Facebook-Message-Splitter

Parses facebook data messages and splits them individually by chat participants into a text file.

# Usage:

You will first need to download facebook backup data from your Account > Settings. After downloading facebook data, extract it and move this script to the extracted folder and run.

>>> python fms.py

# How it works:

It reads the html file and obtains the sender name, message sent/received date and message and writes these to a new file. It obtains the user ids from facebook using mechanize to send the login data and then retrieves the user profile name by using requests and bs4 for parsing html. The messages are splitted according to the chat participants.

# Example:

[ ] http://i.imgur.com/PNcPIjg.png

will be converted to:

Sender: 	ABC
Date:    	Sunday, 18 December 2020 at 10:25 XYZ
Message: 	XYZ

------------------------------------------------------------
Sender: 	XYZ
Date:    	Sunday, 18 December 2020 at 10:25 XYZ
Message: 	ABC

------------------------------------------------------------

# TODO:

- [ ] Parse date.
- [ ] Creating a nice HTML page for messages.
- [ ] Ability to search links inside messages.
- [ ] Average response time from specific users
