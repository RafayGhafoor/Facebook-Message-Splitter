import re
import bs4
import os
import mechanize
import sys

os.chdir("/home/rafay/Downloads/facebook-RafayGhafoor/html/")
reload(sys)
sys.setdefaultencoding('utf8')
para_text = []
chat_participants = []


def get_participants():
    '''Gets Users who are participating in the chat.'''
    for participants in soup.findAll("div", {"class": "thread"}):
        if participants not in chat_participants:
            chat_participants.append(participants.children.next().encode("ascii").strip())


def format_messages():
    '''Formats messages nicely.'''
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


def get_ids(filename):
    '''Gets userid from the provided file.'''
    with open("split_messages.txt", "r") as f:
    	lst = []
    	for line in f:
            s = re.search(r'\d{15}', line)
            if s:
                if s.group() not in lst and s.group()[0] == '1' and s.group()[1:5] == '0000':
                    lst.append(s.group())
        return lst


def get_profile_names(user_ids):
    '''Get profile name from userid. For Example:-
    >>> 100004561272818 [INPUT]
    >>> Alan Walker [OUTPUT]
    '''
    id_profile = {}
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
    br['pass'] = 'pwd'
    res = br.submit()
    print "Successfully Logged in!\n"
    for i, ids in enumerate(user_ids):
        url = "https://facebook.com/" + ids
        soup = bs4.BeautifulSoup(br.open(url).read(), 'html.parser')
        id_profile[ids] = soup.find("title").text.encode('ascii', 'ignore')
        print "%s --> %s" % (ids, id_profile[ids])
        with open("testfile.txt", 'a') as z:
            for k,v in id_profile.iteritems():
                z.write("%s: %s\n" % (k, v))

                
def uid_pnames(filename, uid_pnames):	    # UserID to Profile Names
    '''Replace UserIDs with Profile Names'''
    with open(filename, 'r') as f:
        with open(("new" + filename), 'a') as z:
            for i, line in enumerate(f, 1):
                for uid, pnames in uid_pnames.iteritems():
                    if uid in line:
                        line = line.replace(uid + "@facebook.com", pnames)
                z.write(line)

def main():
     openfile()
     format_messages()
     ids_lst = get_ids("filename")
     name = get_profile_names(ids_lst)
     uid_pnames("split_messages.txt", name)
     for k,v in name.iteritems():
        print "ID: %s --> %s" % (k, v)

main()
