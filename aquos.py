import socket

# Change these to match your TV's configuration
tv_ip = "10.0.0.10"
user = "admin"
password = "admin"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((tv_ip, 10002))

# Log in to the TV
s.send(user + "\r" + password + "\r")
# Receive the prompts (will be "Login:\r\nPassword:")
s.recv(1024)


# Mute (toggle)
s.send("MUTE0   \r")
s.recv(1024)

#POWer OFF
s.send("POWR0   \r")
s.recv(1024)

#POWer ON
s.send("POWR1   \r")
s.recv(1024)

# POwer Command
#he Power On command accepted.When the power is in standby mode, commands #also go to waiting statusand so power consumption is just about the same as #usual. With thecommands in waiting status, the Center Icon Illumination on #the front of theTV lights up
s.send("RSPW2   \r")
s.recv(1024)



#?
#RSPW2
s.send("RSPW2   \r")
s.recv(1024)

#Toggle
s.send("TVD   \r")
s.recv(1024)


#Volume to 1
s.send("VOLM1   \r")
s.recv(1024)

s.send("WIDE9   \r")
s.recv(1024)

#MUTE
s.send("MUTE0   \r")
s.recv(1024)

#Kanal hoch
s.send("CHUP1   \r")
s.recv(1024)

#Kanal hoch
s.send("CHDW1   \r")
s.recv(1024)


#Offtimer - OFF
s.send("OFTM0   \r")
s.recv(1024)


#Offtimer - 30min
s.send("OFTM1   \r")
s.recv(1024)


#Offtimer - 60min
s.send("OFTM2   \r")
s.recv(1024)


#Offtimer - 90min
s.send("OFTM3   \r")
s.recv(1024)

#Offtimer - 120min
s.send("OFTM4   \r")
s.recv(1024)

#Switch back to TV
s.send("TVD0   \r")
s.recv(1024)


# geht??
s.send("WIDE4   \r")
s.recv(1024)

s.send("WIDE7   \r")
read=s.recv(1024)
IF read:
print "NOT OK"
else
	print "OK"



