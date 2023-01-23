"""Import Libraries"""
import imaplib
import email
import getpass
import pandas as pd

"""
Desired Email address is entered as a string
Then login to the email server
"""
username =  input("barsik2gtii@yandex.ru ")
password = getpass.getpass("QWghbynth17 ")
mail = imap.yandex.ru('barsik3gtii@yandex.ru')
"""Checking the mailboxes and selecting one"""
print(mail.list())
mail.select("INBOX")
"""Searching for emails in the mailbox"""
result, numbers = mail.search(None, '(FROM "promoby@info.lamoda.ru")')
uids1 = numbers[0].split()
uids = [id.decode("utf-8") for id in uids1 ]
"""Fetching the desired content"""
result, messages = mail.fetch(','.join(uids) ,'(RFC822)')
body_list =[]
date_list = []
from_list = []
subject_list = []
for _, message in messages[::2]:
  email_message = email.message_from_bytes(message)
  email_subject = email.header.decode_header(email_message['Subject'])[0]
  for part in email_message.walk():
    print(part.get_content_type())
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        body = body.decode("utf-8")
        body_list.append(body)
    else:
        continue
    if isinstance(email_subject[0],bytes):
      decoded = email_subject[0].decode(errors="ignore")
      subject_list.append(decoded)
    else:
      subject_list.append(email_subject[0])
  date_list.append(email_message.get('date'))
  fromlist = email_message.get('From')
  fromlist = fromlist.split("<")[0].replace('"', '')
  from_list.append(fromlist)

  date_list = pd.to_datetime(date_list)
  date_list = [item.isoformat(' ')[:-6] for item in date_list]
  print(len(subject_text))
  print(len(from_list))
  print(len(date_list))
  print(len(body_list))
  data = pd.DataFrame(data={'Date': date_list, 'Sender': from_list, 'Subject': subject_list, 'Body': body_list})
  data.to_csv('emails.csv', index=False)
  data.head()


  def clean_data(data, column, i):
      data.loc[i, column] = data.loc[i, column].split("\r\n")
      new_string = " ".join(data.loc[i, column])
      new_string = new_string.split("'',")
      data[column][i:i + 1] = pd.DataFrame(data=new_string)
      return data


  for n in range(len(data)):
      new_data = clean_data(data, "Body", n)

new_data.head()