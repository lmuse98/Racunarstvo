import smtplib

client = smtplib.SMTP('localhost',1025)

fromaddr = 'lucasmuse98@gmail.com'
toaddrs = 'lucasmuse98@gmail.com'
msg = 'Hello'

client.sendmail(fromaddr, toaddrs, msg)
client.quit()