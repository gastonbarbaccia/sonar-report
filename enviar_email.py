import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import os
 

class email():

    def enviar_email_reporte():
        dt = datetime.now()
        fecha_hora = (dt.strftime('%d%m%Y'))

        ano = (dt.strftime('%Y'))
        mes = (dt.strftime('%m'))
        dia = (dt.strftime('%d'))


        sender_email = "sysvulnerability@gmail.com"
        receiver_email = "gastonbarbaccia@hotmail.com"

        message = MIMEMultipart()

        message["From"] = "reportes_sonarqube@supervielle.com.ar"
        message['To'] = receiver_email
        message['Subject'] = "Reporte de vulnerabilidades de Sonarqube - "+dia+mes+ano

        file = "ReporteSonar"+dia+mes+ano+".zip"
        attachment = open(file,'rb')

        obj = MIMEBase('application','octet-stream')

        obj.set_payload((attachment).read())
        encoders.encode_base64(obj)
        obj.add_header('Content-Disposition',"attachment; filename= "+file)

        message.attach(obj)

        my_message = message.as_string()
        email_session = smtplib.SMTP('smtp.gmail.com',587)
        email_session.starttls()
        email_session.login(sender_email,'ns2b7bfqbf')

        email_session.sendmail(sender_email,receiver_email,my_message)
        email_session.quit()
        print("Su email ha sido enviado")
