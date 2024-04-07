import pandas as pd
import re
logs = open('chat.txt','r',errors='ignore')
chat = logs.read()
dates = re.findall(r'(\d+/\d+/\d+)',chat)
times = re.findall(r'[\d]{1,2}:[\d]{2}:[\d]{2}',chat)
name = re.findall(r'\] [a-zA-Z]{3,25}\s*[a-zA-Z]*:',chat)
name = [x.replace('] ','') for x in name]
name = [x.replace(':','') for x in name]
msg = re.findall(r': .*',chat)
msg = [x.replace(r': ','') for x in msg]