#This time write a regex to get only the part of the email before the "@" sign excluding the "@" sign.
#i.e: only mike part from mike@protonmail.com

import re
textToScan = "The advancements in biomarine studies franky@google.com, with the investments necessary and Davos sinatra123@yahoo.com Then The New Yorker article on wind farms..." 

#create Regex
emailRegex = re.compile(r'([a-zA-Z0-9_]+)\@')

#Data scans the string 'textToScan' and stores matched text in it
Data = emailRegex.findall(textToScan)

print(Data)