# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
textfile = "./template.html"
with open(textfile, "r") as fp:
    # Create a text/plain message
    html = fp.read()

msg = MIMEText(html, "html")
msg["Subject"] = "Subject example"
msg["From"] = "python@mail.com"
msg["To"] = "gigi.becali@yahoo.com"


s = smtplib.SMTP("localhost", port=2025)
s.sendmail("python@mail.com", "gigi.becali@yahoo.com", msg.as_string())
s.quit()
