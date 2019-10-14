from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path 
from string import Template
import smtplib 
template = Template(Path("template.html").read_text())
message = MIMEMultipart()
message["from"] = "Cameron"
message["to"] = "usrName@domain.com"
message["subject"]= "This is a text"
body = template.substitute({"name": "Cameron"})
#body = template.substitute(name="Cameron")
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("~/Pictures/Image.jpg").read_bytes()))

with smtplib.SMTP(host = "smtp.gmail.com" , port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("usrName@domain.com", "passphrases")
    smtp.send_message(message)
    print("Sent... ")
    
    
    
