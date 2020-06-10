import smtplib

email_address=('lucasmuse98@gmail.com')
email_password=('xxxxxxxxxx')

with smtplib.SMTP('smtp.gmail.com',587)as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    smtp.login(email_address,email_password)
    
    predmet='test za profesora'
    body='Pozdrav ovo je  test'
    
    Message=f'predmet:{predmet}\n\n{body}'
    
    smtp.sendmail(email_address, email_address ,Message)
    
    