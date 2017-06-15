import bs4
import os
import mechanize
import sys

reload(sys)  
sys.setdefaultencoding('utf8')

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
    url = "https://facebook.com/" + user_id
    '''Get profile name from userid. For Example:-
    >>> 100004561272818 [INPUT]
    >>> Alan Walker [OUTPUT]
    '''
    br = mechanize.Browser()
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0')]
    br.open('https://www.facebook.com/')
    br.select_form(nr=0)
    br['email'] = 'email'
    br['pass'] = 'passwd'
    res = br.submit()
    print "Successfully Logged in!\n"
    soup = bs4.BeautifulSoup(br.open(url).read(), 'html.parser')
    return soup.find("title").text.encode('ascii', 'ignore')


def uid_pnames():	    # UserID to Profile Names
    '''Replace UserIDs with Profile Names'''
    pass


def main():
    # openfile()
    # format_messages()
    name = get_profile_names("100004528276712")
    print "%r" % name

main()
