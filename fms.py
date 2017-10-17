import shutil
import re
import bs4
import os
# import mechanize
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

if not os.path.exists("Messages"):
    os.mkdir("Messages")


def pretty_it(html_file="test.htm", outputfile="pretty_test.htm"):
    '''
    Takes the messages file and convert it to pretty HTML
    format using BeautifulSoup method prettify for better readability.
    '''
    with open(html_file, 'r') as f:
        with open(outputfile, 'a') as z:
            soup = bs4.BeautifulSoup(f.read(), 'lxml')
            z.write(soup.prettify())


def get_threads():
    '''
    Get message threads i.e., conversation between two participants and
    returns them as a list.
    '''
    current_participants = []

    for x in soup.findAll('div', {'class': 'thread'}):

        if x.contents[0].strip() not in current_participants:
            current_participants = []
            current_participants.append(x.contents[0].strip())
            print("Chat switched to {}".format(current_participants[0]))

        sender = x.find('span', {'class': 'user'}).text.strip()
        meta = x.find('span', {'class': 'meta'}).text.strip()
        message_lst = x.findAll('p')

        for msg in message_lst:
            print("Sender: {}\nTime Stamp: {}\nMessage: {}\n".format(sender, meta, msg.text))


def extract_messages(participants):
    '''
    Extract messages between the participants, provided.
    '''
    pass
    # soup.find("div", {'class': 'thread'})


def main():
    get_threads()


if __name__ == "__main__":
    with open('test.htm', 'r') as f:
        soup = bs4.BeautifulSoup(f.read(), 'lxml')
    main()
