import bs4
import os
# import shutil
# import re
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
    msg_lst = []

    for msg in soup.findAll("p"):
        msg_lst.append(msg.text.strip())

    for z in soup.findAll('div', class_='thread'):
        filename = z.contents[0].strip()
        for x in z.findAll("div", class_="message_header"):
            with open(filename + ".txt", "a") as f:
                sender = x.find('span', {'class': 'user'}).text.strip()
                meta = x.find('span', {'class': 'meta'}).text.strip()
                f.write("Sender: {}\nTime Stamp: {}\nMessage: {}\n\n".format(sender, meta, msg_lst[count]))


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
