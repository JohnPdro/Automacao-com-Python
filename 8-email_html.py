from email.message import EmailMessage
import smtplib
import ssl
import mimetypes

# lê a senha de app e remove espaços/quebra de linha
password = open('senha', 'r').read().strip()

from_email = 'xanarckx@gmail.com'
to_email = 'xanarckx@gmail.com'
subject = 'Proposta de Parceria Customizada'
body = open('files/index.html.txt', 'r', encoding='utf-8').read()

# 1 - Montando estrutura do e-mail
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject

message.set_content(body, subtype='html')
safe = ssl.create_default_context()

# 2 - Adicionar anexo

anexo = 'files/corpo.txt'
print(mimetypes.guess_type(anexo)[0])
mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split('/')
with open(anexo, 'rb') as a :
    message.add_attachment(
        a.read(),
        maintype = mime_type,
        subtype = mime_subtype,
        filename = anexo
    )
    
# 3 - Envio de e-mail

with smtplib.SMTP_SSl('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )