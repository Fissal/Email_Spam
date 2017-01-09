
import sys, feedparser, winsound
#Here, we import modules needed for this program
newEmail=""
USERNAME="fissalalsharef@gmail.com"
PASSWORD="feasal12354568+"
PROTO="https://"
SERVER="mail.google.com"
PATH="/gmail/feed/atom"
#We assign variables with values. Fill in your username and password
def mail():
    '''['entries'][0]['title']
    '''
    email = int(feedparser.parse(
        PROTO + USERNAME + ":" + PASSWORD + "@" + SERVER + PATH)['entries'])

    if email > 0:
        newEmail = 1
    else:
        newEmail = 0

    if newEmail==1:
         winsound.Beep(440, 500)
         winsound.Beep(370, 500)
         winsound.Beep(392, 500)
    return email

mail()

# # #
# # #
# # #
# # # from feeds import *
# # # from BeautifulSoup import BeautifulSoup
# # # import urllib
# # # link = mail()
# # # r = urllib.urlopen(link)
# # # x = r.read()
# # # print x
# # # # s = BeautifulSoup(x)
# # # # c = s.getText()
# # # # b = getwords(c)
# # # # print b
# # #
# # #
# # # # print(b)
# # #
# # #
# # #
# # #
# # #
# # #
# #
# # # import imaplib
# # # import email
# # # mail = imaplib.IMAP4_SSL('imap.gmail.com')
# # # # imaplib module implements connection based on IMAPv4 protocol
# # # mail.login('fissalalsharef', 'feasal12354568+')
# # # mail.list() # Lists all labels in GMail
# # # mail.select('inbox') # Connected to inbox.
# # #
# # # result, data = mail.uid('search', None, "ALL")
# # # print "sdsd"
# # # # search and return uids instead
# # # i = len(data[0].split()) # data[0] is a space separate string
# # # for x in range(i):
# # #  latest_email_uid = data[0].split()[x] # unique ids wrt label selected
# # #  result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
# # #  # fetch the email body (RFC822) for the given ID
# # #  raw_email = email_data[0][1]
# #
# # #  #continue inside the same for loop as above
# # # raw_email_string = raw_email.decode('utf-8')
# # # # converts byte literal to string removing b''
# # # email_message = email.message_from_string(raw_email_string)
# # # # this will loop through all the available multiparts in mail
# # # for part in email_message.walk():
# # #  if part.get_content_type() == "text/plain": # ignore attachments/html
# # #   body = part.get_payload(decode=True)
# # #   save_string = str("D:Dumpgmailemail_" + str(x) + ".eml")
# # #   # location on disk
# # #   myfile = open(save_string, 'a')
# # #   myfile.write(body.decode('utf-8'))
# # #   # body is again a byte literal
# # #   myfile.close()
# # #  else:
# # #   continue
# #
#
#
# import imaplib
# import email
#
#
# mail = imaplib.IMAP4_SSL('imap.gmail.com')
# (retcode, capabilities) = mail.login('engr212project.test@gmail.com ','project4test')
# mail.list()
# mail.select('inbox')
#
# n = 0
#
# (retcode, messages) = mail.search(None, '(UNSEEN)')
# if retcode == 'OK':
#     for num in messages[0].split():
#         print 'Processing '
#         n = n+1
#         typ, data = mail.fetch(num, '(RFC822)')
#         for response_part in data:
#             if isinstance(response_part, tuple):
#                 original = email.message_from_string(data[0][1])
#                 print original['From']
#                 print original['Subject']
#                 # print original
#                 typ, data = mail.store(num, '+FLAGS', '\\Seen')
#
# print n
#
# import email


# from email.Header import decode_header
# import email
# from base64 import b64decode
# import sys
# from email.Parser import Parser as EmailParser
# from email.utils import parseaddr
#
# from StringIO import StringIO

# class NotSupportedMailFormat(Exception):
#     pass
#
# def parse_attachment(message_part):
#     content_disposition = message_part.get("Content-Disposition", None)
#     if content_disposition:
#         dispositions = content_disposition.strip().split(";")
#         if bool(content_disposition and dispositions[0].lower() == "attachment"):
#
#             file_data = message_part.get_payload(decode=True)
#             attachment = StringIO(file_data)
#             attachment.content_type = message_part.get_content_type()
#             attachment.size = len(file_data)
#             attachment.name = None
#             attachment.create_date = None
#             attachment.mod_date = None
#             attachment.read_date = None
#
#             for param in dispositions[1:]:
#                 name,value = param.split("=")
#                 name = name.lower()
#
#                 if name == "filename":
#                     attachment.name = value
#                 elif name == "create-date":
#                     attachment.create_date = value  #TODO: datetime
#                 elif name == "modification-date":
#                     attachment.mod_date = value #TODO: datetime
#                 elif name == "read-date":
#                     attachment.read_date = value #TODO: datetime
#             return attachment
#
#     return None
#
# def parse(content):
#
#     p = EmailParser()
#     msgobj = p.parse(content)
#     if msgobj['Subject'] is not None:
#         decodefrag = decode_header(msgobj['Subject'])
#         subj_fragments = []
#         for s , enc in decodefrag:
#             if enc:
#                 s = unicode(s , enc).encode('utf8','replace')
#             subj_fragments.append(s)
#         subject = ''.join(subj_fragments)
#     else:
#         subject = None
#
#     attachments = []
#     body = None
#     html = None
#     for part in msgobj.walk():
#         attachment = parse_attachment(part)
#         if attachment:
#             attachments.append(attachment)
#         elif part.get_content_type() == "text/plain":
#             if body is None:
#                 body = ""
#             body += unicode(
#                 part.get_payload(decode=True),
#                 part.get_content_charset(),
#                 'replace'
#             ).encode('utf8','replace')
#         elif part.get_content_type() == "text/html":
#             if html is None:
#                 html = ""
#             html += unicode(
#                 part.get_payload(decode=True),
#                 part.get_content_charset(),
#                 'replace'
#             ).encode('utf8','replace')
#     return {
#         'subject' : subject,
#         'body' : body,
#         'html' : html,
#         'from' : parseaddr(msgobj.get('From'))[1],
#         'to' : parseaddr(msgobj.get('To'))[1],
#         'attachments': attachments,
#     }


