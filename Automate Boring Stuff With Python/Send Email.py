import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587) #587 is port number
print(type (conn))

conn.ehlo() #called to start connection
conn.starttls() #for starting encryption

conn.login('pkmngospoof123321@gmail.com', 'APPP PASSWORD')

conn.sendmail('pkmngospoof123321@gmail.com', 'dpamecha8@gmail.com', 'Subject: Test...\n\nThis is Test Message. \n\n-Pkmn Go' )
#from, to,

conn.quit()



#
# 
# Have to update with Google's APP password https://support.google.com/mail/answer/185833?hl=en-GB
#
# 
