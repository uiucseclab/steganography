import smtplib
import getpass
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

def sendEmail(dest_image):
	personal_email = raw_input("Would you like to send the email from \
your personal account or a generic account?\nEnter 1 for personal \
account or 2 for generic account.\n")
	if personal_email == "1":
		email_domain = raw_input("Enter your email domain: (1) Gmail (2) Outlook (3) Yahoo (4) Hotmail (5) Mail\n")
		email_domain = int(email_domain)
		if email_domain == 1:
			server = smtplib.SMTP('smtp.gmail.com', 587)
		elif email_domain == 2:
			server = smtplib.SMTP('smtp-mail.outlook.com', 587)
		elif email_domain == 3:
			server = smtplib.SMTP('smtp.mail.yahoo.com', 465)
		elif email_domain == 4:
			server = smtplib.SMTP('smtp.live.com', 25)
		elif email_domain == 5:
			server = smtplib.SMTP('smtp.mail.com', 587)
		else:
			raise Exception("Invalid domain input.")

		email_address = raw_input("What is your email address?\n")
		email_password = getpass.getpass("Password:")
	elif personal_email == "2":
		email_address = "steganography@mail.com"
		email_password = "securitylab"
		server = smtplib.SMTP('smtp.mail.com', 587)
	else:
		raise Exception("Invalid input. The options were either 1 or 2 but you entered: " + personal_email)

	server.ehlo()
	server.starttls()
	server.login(email_address, email_password)



	recipient_address = raw_input("What is the recipient's email address?\n")
	subject = raw_input("Enter the subject of the email.\n")
	text = raw_input("Enter the body of the message.\n")
	msg = MIMEMultipart()
	msg['From'] = email_address
	msg['To'] = recipient_address
	msg['Date'] = formatdate(localtime=True)
	msg['Subject'] = subject
	msg.attach(MIMEText(text))

	f = open(dest_image, "rb")
	part = MIMEApplication(
		f.read(),
		Name=basename(dest_image)
	)
	part['Content-Disposition'] = 'attachment; filename="%s"' % basename(dest_image)
	msg.attach(part)
	server.sendmail(email_address, recipient_address, msg.as_string())
	print "Email sent from " + email_address + " to " + \
recipient_address + " with " + dest_image + " attached to the email."
	server.close()
