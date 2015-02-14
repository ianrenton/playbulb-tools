# Python script to set a Playbulb LED colour based on the state of
# an IMAP mailbox.
# by Ian Renton
# https://github.com/ianrenton/playbulb-tools
# Watch it in action: https://vimeo.com/119624218

# Inspired by https://pdominique.wordpress.com/2015/01/02/hacking-playbulb-candles/
# Requires a computer with a Bluetooth 4.0 Low Energy compatible device
# and the hcitool/gattool utilities installed. (Install the bluez package.)
# Info on undocumented gattool non-interactive mode from:
# http://www.humbug.in/2014/using-gatttool-manualnon-interactive-mode-read-ble-devices/
# Tested on Linux, YMMV on Mac/Win.

import getpass, imaplib, os, time

#### Config ####

# Your IMAP server config
SERVER = 'imap.gmail.com'
PORT = 993
USER = 'yourusername'
PASSWORD = 'yourpassword'

# Your Playbulb address (obtained with 'sudo hcitool lescan')
PLAYBULB_ADDRESS = '01:23:45:67:89:01'

# Check every n seconds (300 = 5 mins)
CHECK_INTERVAL = 300

#### Code below ####
while True:
  M = imaplib.IMAP4_SSL(SERVER, PORT)
  M.login(USER, PASSWORD)
  M.select()
  unreadCount = len(M.search(None, 'UnSeen')[1][0].split())
  print str(unreadCount) + ' unread emails'
  
  if unreadCount == 0:
    # No unread, set to solid red
    os.system('gatttool -b ' + PLAYBULB_ADDRESS + ' --char-write -a 0x0016 -n 00FF0000')
  else:
    # Some unread, set to green and flash
    os.system('gatttool -b ' + PLAYBULB_ADDRESS + ' --char-write -a 0x0014 -n 0000FF0000001F00')
  time.sleep(CHECK_INTERVAL)
  
  M.close()
  M.logout()
