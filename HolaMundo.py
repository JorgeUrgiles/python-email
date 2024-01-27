import smtplib
from email.message import EmailMessage

email_sender = "jorge.urgiles19@gmail.com"
password = "xmxr ufoh lyng fqzl"
email_reciver = "jorge.urgilesc@gmail.com"

subject = "Mensaje prueba"
body = """Este mensaje es un email de prueba con fines educativos"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_reciver
em["Subject"] = subject
em.set_content(body)

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()  # Iniciar el cifrado TLS
    smtp.login(email_sender, password)
    smtp.send_message(em)