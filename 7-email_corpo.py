from email.message import EmailMessage
import smtplib
import ssl

# lê a senha de app e remove espaços/quebra de linha
password = open('senha', 'r').read().strip()

from_email = 'xanarckx@gmail.com'
to_email = 'xanarckx@gmail.com'
subject = 'Proposta de Parceria'
body = open('files/corpo.txt', 'r', encoding='utf-8').read()

# 1 - Montando estrutura do e-mail
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject

message.set_content(body)
safe = ssl.create_default_context()

# 2 - Envio de e-mail

with smtplib.SMTP_SSl('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )
    