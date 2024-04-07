import pandas as pd
import re
#The text file is whatever you exported from your chats
logs = open('chat.txt','r',errors='ignore')
chat = logs.read()
#Regex to compile all the different parts of the message into lists
#Messages typically follow this pattern: [Date, Time] Sender: Message
dates = re.findall(r'(\d+/\d+/\d+)',chat)
times = re.findall(r'[\d]{1,2}:[\d]{2}:[\d]{2}',chat)
name = re.findall(r'\] [a-zA-Z]{3,25}\s*[a-zA-Z]*:',chat)
#Replace method is used to clean up the parts of the regex you dont wanna keep in the actual data
name = [x.replace('] ','') for x in name]
name = [x.replace(':','') for x in name]
msg = re.findall(r': .*',chat)
msg = [x.replace(r': ','') for x in msg]
