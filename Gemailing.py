import imaplib
import email
import getpass
import pandas as pd
username =  input("23elia2021@gmail.com")
password = getpass.getpass("QWmamasuper1985")
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username, password)
print(mail.list())
mail.select("inbox")
result, numbers = mail.search(None, '(FROM "s_pasiukevich@lesta.group")')
uids = numbers[0].split()
uids = [id.decode("utf-8") for id in uids ]
result, messages = mail.fetch(','.join(uids) ,'(RFC822)')
body_list =[]
date_list = []
from_list = []
subject_list = []
for _, message in messages[::2]:
  email_message = email.message_from_bytes(message)
  email_subject = email.header.decode_header(email_message['Subject'])[0]
  for part in email_message.walk():
    if part.get_content_type() == "text/plain" :
        body = part.get_payload(decode=True)
        body = body.decode("utf-8")
        body_list.append(body)
    else:
        continue
    if isinstance(email_subject[0],bytes):
      decoded = email_subject.decode(errors="ignore")
      subject_list.append(decoded)
    else:
      subject_list.append(email_subject[0])
  date_list.append(email_message.get('date'))
  fromlist = email_message.get('From')
  fromlist = fromlist.split("<")[0].replace('"', '')
  from_list.append(fromlist)
date_list = pd.to_datetime(date_list)
date_list = [item.isoformat(' ')[:-6]for item in date_list]
data = pd.DataFrame(data={'Date':date_list,'Sender':from_list,'Subject':subject_list, 'Body':body_list})
data.to_csv('emails.csv',index=False)
data = pd.read_csv("\emails.csv")
data.head()
def clean_data(data, column, i):
    data.loc[i, column] = data.loc[i, column].split("\r\n")
    new_string = " ".join(data.loc[i, column])
    new_string = new_string.split("'',")
    data[column][i:i+1] = pd.DataFrame(data = new_string)
    return data
for n in range(len(data)):
    new_data = clean_data(data, column = "Body", i = n)

