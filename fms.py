import shutil
import re
import bs4
import os
import mechanize
import sys

reload(sys)
sys.setdefaultencoding('utf8')
os.mkdir("Messages") if not os.path.exists("Messages")


class Facebook():
    def __init__(self, email, password, filename, msg_folder):
        self.email = email
        self.password = password
        self.infile = infile
        self.msg_folder = msg_folder
        self.outfile = outfile
        self.para_text = []
