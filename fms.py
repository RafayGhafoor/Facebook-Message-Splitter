import bs4
import os
import shutil
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
    format using BeautifulSoup prettify method for better readability.
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
    count = 0

    # Gets 'p' tags (messages i.e., sent) and store them in the list.
    for msg in soup.findAll("p"):
        msg_lst.append(msg.text.strip())

    for z in soup.findAll('div', class_='thread'):
        # contains chat participants name i.e., Person 1, Person 2
        filename = z.contents[0].replace(',', ' -').strip()
        for x in z.findAll("div", class_="message_header"):
            if len(filename.split('-')) < 3:  # If the conversation is not between a group
                # We create a filename of format "Person 1 - Person 2.txt"
                with open(filename + ".txt", "a") as f:
                    # Contains sender messages
                    sender = x.find('span', {'class': 'user'}).text.strip()
                    # Contains time stamp
                    time_stamp = x.find('span', {'class': 'meta'}).text.strip()
                    f.write("Sender: {}\nTime Stamp: {}\nMessage: {}\n\n".format(sender, time_stamp, msg_lst[count]))
                    count += 1

    # Move the splitted messages to Messages folder
    for i in [i for i in os.listdir('.') if i.endswith(".txt")]:
        shutil.move(i, "Message")


def main():
    get_threads()

if __name__ == "__main__":
    with open('talha_pretty.htm', 'r') as f:
        soup = bs4.BeautifulSoup(f.read(), 'lxml')
    main()
