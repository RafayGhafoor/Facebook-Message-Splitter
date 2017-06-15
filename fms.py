import bs4
import os
import requests

para_text = []
chat_participants = []


def get_participants():
    '''Gets Users who are participating in the Chat'''
    for participants in soup.findAll("div", {"class": "thread"}):
        if participants not in chat_participants:
            chat_participants.append(participants.children.next().encode("ascii").strip())


def format_messages():
    '''Format Messages'''
    count = 0
    for ps in soup.findAll("p"):
        para_text.append(ps.text.strip())

    for divs in soup.findAll("div", {"class": "message_header"}):
        sender = divs.find("span", {"class": "user"}).text.strip()
        meta_data = divs.find("span", {"class": "meta"}).text.strip()
        print("Sender: \t%s\nDate:    \t%s\nMessage: \t%s\n\n%s\n"\
                        % (sender, meta_data, para_text[count].strip(), "-" * (len(meta_data) + 20)))
        if count == len(para_text):
            print "breaking"
            break
        count += 1


def openfile(filename="test.htm"):
    '''Opens Messages file for reading data.'''
    with open(filename, 'r') as f:
        global soup
        soup = bs4.BeautifulSoup(f, "html.parser")


def get_profile_names(user_id):
    '''Get profile name from userid. For Example:-
    >>> 100004561272818 [INPUT]
    >>> Alan Walker [OUTPUT]
    '''
    pass


    
def uid_pnames(): # UserID to Profile Names
    '''Replace UserIDs with Profile Names'''
    pass


def main():
    openfile()
    format_messages()

main()
