from email.message import EmailMessage
import smtplib
import ssl

# lê a senha de app e remove espaços/quebra de linha
password = open('senha', 'r').read().strip()

from_email = 'xanarckx@gmail.com'
to_email = 'xanarckx@gmail.com'
subject = 'Curso Python'

body = '''
A melhor forma de prever o futuro é criá-lo.
Aprendendo a linguagem Python.
'''

# 1 - Estruturando a mensagem
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject
message.set_content(body)

safe = ssl.create_default_context()

# 2 - Envio de e-mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.send_message(message)

print('E-mail enviado com sucesso!')