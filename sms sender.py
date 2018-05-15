import smtplib
verizon_gateway = 'vtext.com'
at_gateway = 'mms.att.net'
tmobile_gateway = 'tmomail.net'
sprint_gateway = 'page.nextel.com'
gmail_address = ""
gmail_password = ""
msg = ""

def sendMessage (number, provider, message) :
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.startls()
    if gmail_address:
        server.login(gmail_address, gmail_password)
    else:
        gmail_address = raw_input("Enter Gmail Login")
        gmail_password = raw_input("Enter Gmail password")
        server.login(gmail_address, gmail_password)
    server.sendmail(gmail_address, number+'@'+provider, message)

x = 0
y = 0
while y < 1
    print "Welcome to MessageSender, valid gateway inputs are: verizon, att, tmobile, or sprint"
    if msg:
        continue
    else:
        msg = raw_input("Enter Message to send")
    nmbr = raw_input("Enter number to send message to")
    while x < 1 :
        prvd = raw_input("Enter provider:")
        prvd = prvd.lower()
        if prvd == 'verizon' :
            carrier = verizon_gateway
            x = 1
        elif prvd == 'att' :
            carrier = at_gateway
            x = 1
        elif prvd == 'tmobile' :
            carrier = tmobile_gateway
            x = 1
        elif prvd == 'sprint' :
            carrier = sprint_gateway
            x = 1
        else :
            print "Invalid Carrier"
    sendMessage(nmbr, carrier, msg)
    print "Sent message"
    breakornobreak = raw_input("Enter another message to send another, or press enter to EXIT...")
    if breakornobreak :
        y = 0
    else :
        y = 1
