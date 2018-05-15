import smtplib, base64, sys, re, time

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

MAX_TEXT_LENGTH = 160

SmsGateways = [
   'tmomail.net',             # tmobile
   'mms.att.net',             # at&t
   'vtext.com',               # verizon
   'page.nextel.com',         # sprint
   'sms.mycricket.com',       # cricket 
   'vmobl.com',               # virgin mobile US
   'sms.myboostmobile.com'    # boost mobile
]

def LogInSMTPServer( email, password ):
   server = smtplib.SMTP( "smtp.gmail.com", 587 )
   server.starttls()
   server.login( email, password )

   return server

def SendSMS( server, phone, msg_text, attach_file ):

   if len( msg_text ) <= MAX_TEXT_LENGTH:

      # Send to all gateways, since a phone number
      # can only be specific to one carrier.
      for gateway in SmsGateways:
         destination = phone + '@' + gateway

         msg = MIMEMultipart()
         msg.attach( MIMEText(msg_text, 'plain') )

         # Check if valid attachment
         if attach_file != '':
            fp = open( attach_file, 'rb' )
            msg_img = MIMEImage( fp.read() )
            fp.close()

            msg.attach( msg_img )

         server.sendmail( '', destination, msg_text )

   else:
      print 'Message is too long. SMS not sent.'


p = re.compile( '\d{10}' )

# Get destination phone number
phone = raw_input( 'Enter 10 digit phone number: ' )
email = 'bennettdixon16@gmail.com'
password = 'benrocks32'
if p.match( phone ) == None:
   print 'Valid phone not entered!'
   sys.exit(0)

# Get message
msg_text = raw_input( 'Enter message: ' )

# Ask for attachments
attach_file = raw_input( 'Enter attachments: ')

text_num = raw_input ( 'Enter number of times to send message: ')

print '\nLogging into SMTP server..'
smtp_server = LogInSMTPServer( email, password )
x=0
while x < text_num :
   SendSMS( smtp_server, phone, msg_text, attach_file )
   print 'SMS sent to %s' % phone
   time.sleep(2.5)
   x+=1
