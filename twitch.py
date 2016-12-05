#!/usr/bin/env python
# twitch.py 
# Authors: Avicennasis
# License:  MIT license Copyright (c) 2015 Avicennasis
# Revision: see git

# Import libraries
from twitchconfig import *
import re, socket, os, time, random

#Definitions
zero      = 0                   # Zero
one       = 1                   # One
false     = 0                   # Boolean False
true      = 1                   # Boolean True

# Program parameters

# botnick  = nick of the bot
# bufsize  = Input buffer size
# channel  = IRC channel
# port     = port number
# server   = server hostname
# master   = Owner of the bot
# uname    = Bot username 
# realname = Bot's "real name"

botnick    = "AvicBot"
bufsize    = 10240
channel    = "#noobenheim"
port       = 6667
server     = "irc.twitch.tv"
master     = "Avicennasis"
uname      = "AvicBot"
realname   = "Avicennasis"

#Dictionary
Replies = dict()
Replies ['die'      ] = "No, you"
Replies ['goodbye'  ] = "I'll miss you"
Replies ['sayonara' ] = "I'll miss you"
Replies ['scram'    ] = "No, you"
Replies ['shout'    ] = "NO I WON'T"
Replies ['dance'    ] = "*" + botnick + " dances*"
Replies ['hi'       ] = "Hi!"
Replies ['hello'    ] = "Hello!"
Replies ['howdy'    ] = "Howdy there, partner!"
Replies ['time'     ] = "It is TIME for a RHYME"
Replies ['master'   ] = master + " is my master"

#ping
def ping():
    global ircsock
    ircsock.send ("PONG :pingis\n")

#sendmsg
def sendmsg (chan, msg):
    global ircsock
    ircsock.send ("PRIVMSG "+ chan +" :"+ msg + "\n")

#JoinChan
def JoinChan (chan):
    global ircsock
    ircsock.send ("JOIN "+ chan +"\n")

#ProcHello
def ProcHello():
    global ircsock
    ircsock.send ("PRIVMSG "+ channel +" :Hello!\n")

# Main routine
def Main():
    global ircsock, Replies
                                #reply regex
    pattern1 = '.*:(\w+)\W*%s\W*$' % (botnick)
    pattern2 = '.*:%s\W*(\w+)\W*$' % (botnick)

    ircsock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    ircsock.connect ((server, port))
    ircsock.send ("PASS {}\r\n".format(PASS).encode("utf-8"))
    ircsock.send ("USER " + uname + " 2 3 " + realname + "\n")
    ircsock.send ("NICK "+ botnick + "\n")
    JoinChan (channel)          # Join channel
    sendmsg (channel, "AvicBot: Online.\n")
    print "Sent 'AvicBot: Online.' "

    while true:                 # Main loop
                                # Receive server data
        ircmsg = ircsock.recv (bufsize)
                                # newlines go alway
        ircmsg = ircmsg.strip ('\n\r')

        print ircmsg            # Echo input
        time.sleep(0.1)

        m1 = re.match (pattern1, ircmsg, re.I)
        m2 = re.match (pattern2, ircmsg, re.I)
        if ((m1 == None) and (m2 != None)): m1 = m2

        if (m1 != None):        # Yes
            word = m1.group (1) # Word found
            word = word.lower() # Make word lower case
                                # Print a reply
            if (word in Replies):
                sendmsg (channel, Replies [word])
                print "Sent 'Dictionary word' "


        if ircmsg.find ("PING :") != -1:
            ping()

#  !die command to part channel
        if ircmsg.find("!die "+botnick) != -1:
            sendmsg(channel, "Do you wanna build a snowman? \n")
            time.sleep(2)
            sendmsg(channel, "It doesn't have to be a snowman. \n")
            time.sleep(2)
            sendmsg(channel, "Ok, Bye :( \n")
            sendmsg(master, "I have to leave now :( \n")
            print "Sent 'Dying snowman' "
            break

# !say command
        if ircmsg.find ("!say ") != -1:
            say_split = ircmsg.split ("!say ")
            sendmsg (channel, say_split [1])
            sendmsg (master, "Message sent: " + say_split [1])
            print "Sent 'Say command' "

# !sing parameter
# Note that twitch seems to ignore multiple lines - need to add a delay here
        if ircmsg.find ("!sing") != -1:
            sendmsg (channel, "Daisy, Daisy, Give me your answer, do.\n")
            time.sleep(2)
            sendmsg (channel, "I'm half crazy all for the love of you.\n")
            print "Sent 'Sing command' "

# !random number parameter
# This was chosen by a fair roll of a d20.
        if ircmsg.find ("!random") != -1:
            sendmsg (channel, "7.\n")
            print "Sent 'Random number' "

# !commands parameter
# Note that twitch seems to ignore multiple lines - need to add a delay here
        if ircmsg.find ("!commands") != -1:
            sendmsg (channel, "Commands:\n")
            time.sleep(2)
            sendmsg (channel, "!say: I echo back whatever you say.\n")
            time.sleep(2)
            sendmsg (channel, "!sing: I sing, duh.\n")
            time.sleep(2)
            sendmsg (channel, "!random: Returns a random number.\n")
            time.sleep(2)
            sendmsg (channel, "!die: Makes me leave :(\n")
            print "Sent 'Command list' "

# !xkcd command
        if ircmsg.find ("!xkcd ") != -1:
            say_split = ircmsg.split ("!xkcd ")
            sendmsg (channel, "http://xkcd.com/" + say_split [1])
            print "Sent 'XKCD link' "

# !youtube command
        if ircmsg.find ("!youtube ") != -1:
            say_split = ircmsg.split ("!youtube ")
            sendmsg (channel, "https://www.youtube.com/watch?v=" + say_split [1])
            print "Sent 'Youtube link' "

# !beer command
        if ircmsg.find ("!beer ") != -1:
            say_split = ircmsg.split ("!beer ")
            sendmsg (channel, "*Gives a beer to " + say_split [1] + "!* Drink up!")
            print "Sent 'Beer' "

# funny response parameters
        # Matrix
        if ircmsg.find ("what is the matrix?") != -1:
            sendmsg (channel, "No-one can be told what the matrix is. You have to see it for yourself.\n")
            print "Sent 'Matrix' "

        # Where are we?
        if ircmsg.find ("where are we?") != -1:
            sendmsg (channel, "Last I checked, we were in " + channel + ", sooo... \n")
            print "Sent 'Where are we message' "

        # Boobies.
        if ircmsg.find ("boobs") != -1:
            sendmsg (channel, "BOOBS!\n")
            print "Sent 'BOOBS!' "
        if ircmsg.find ("boobies") != -1:
            sendmsg (channel, "BOOBIES!\n")
            print "Sent 'BOOBIES!' "

        # Now your thinking with portals.
        if ircmsg.find ("cake") != -1:
            sendmsg (channel, "The cake is a lie!\n")
            print "Sent 'The cake is a lie!' "
        if ircmsg.find ("portal") != -1:
            sendmsg (channel, "Now you're thinking with portals!\n")
            print "Sent 'Now you're thinking with portals!' "
        if ircmsg.find ("lemons") != -1:
            sendmsg (channel, "When life gives you lemons, don t make lemonade. Make life take the lemons back! Get mad! \n")
            time.sleep(2)
            sendmsg (channel, "I don t want your damn lemons! What the hell am I supposed to do with these!? \n")
            time.sleep(2)
            sendmsg (channel, "Demand to see life's manager! Make life rue the day it thought it could give Cave Johnson lemons! \n")
            print "Sent 'Lemons Speech' "

        # Shia LaBeouf
        if ircmsg.find ("Shia LaBeouf") != -1:
            sendmsg (channel, "Running for your life from Shia Labeouf.\n")
            time.sleep(2)
            sendmsg (channel, "He's brandishing a knife. It's Shia Labeouf.\n")
            time.sleep(2)
            sendmsg (channel, "Lurking in the shadows... Hollywood superstar Shia Labeouf.\n")
            print "Sent 'Shia LaBeouf' "
        if ircmsg.find ("request Shia") != -1:
            sendmsg (channel, "!request https://www.youtube.com/watch?v=o0u4M6vppCI \n")
            print "Sent 'Shia LaBeouf request' "
        if ircmsg.find ("request shia") != -1:
            sendmsg (channel, "!request https://www.youtube.com/watch?v=o0u4M6vppCI \n")
            print "Sent 'Shia LaBeouf request' "


        # Haddaway
        if ircmsg.find (" love") != -1:
            sendmsg (channel, "What is love? Baby, don't hurt me.\n")
            time.sleep(2)
            sendmsg (channel, "Don't hurt me.\n")
            time.sleep(2)
            sendmsg (channel, "No more.\n")
            print "Sent 'Haddaway' "

        # Blink-182
        if ircmsg.find ("work sucks") != -1:
            sendmsg (channel, "I know. She left me roses by the stairs.\n")
            time.sleep(2)
            sendmsg (channel, "Surprises let me know she cares.\n")
            print "Sent 'Blink-182' "

        # new york city 
        if ircmsg.find ("new york city") != -1:
            sendmsg (channel, "'Cause everyone's your friend in New York City! And everything looks beautiful when you're young and pretty.\n")
            time.sleep(2)
            sendmsg (channel, "The streets are paved with diamonds and there's just so much to see. But the best thing about New York City is you and me.\n")
            print "Sent 'New York City' "
        if ircmsg.find ("New York City") != -1:
            sendmsg (channel, "'Cause everyone's your friend in New York City! And everything looks beautiful when you're young and pretty.\n")
            time.sleep(2)
            sendmsg (channel, "The streets are paved with diamonds and there's just so much to see. But the best thing about New York City is you and me.\n")
            print "Sent 'New York City' "

        # Avenue Q 
        if ircmsg.find ("racist") != -1:
            sendmsg (channel, "Everyone's a little bit racist, Sometimes.\n")
            time.sleep(2)
            sendmsg (channel, "Doesn't mean we go around committing hate crimes!\n")
            print "Sent 'Avenue Q' "

        # The Producers 
        if ircmsg.find ("hitler") != -1:
            sendmsg (channel, "Springtime for Hitler and Germany! Deutschland is happy and gay!\n")
            time.sleep(2)
            sendmsg (channel, "We're marching to a faster pace! Look out, here comes the master race!\n")
            print "Sent 'The Producers - Hitler' "
        if ircmsg.find ("Hitler") != -1:
            sendmsg (channel, "Springtime for Hitler and Germany! Deutschland is happy and gay!\n")
            time.sleep(2)
            sendmsg (channel, "We're marching to a faster pace! Look out, here comes the master race!\n")
            print "Sent 'The Producers - Hitler' "
        if ircmsg.find ("nazi") != -1:
            sendmsg (channel, "Don't be stupid, be a smarty, come and join the Nazi party!\n")
            print "Sent 'The Producers - Nazi' "
        if ircmsg.find ("Nazi") != -1:
            sendmsg (channel, "Don't be stupid, be a smarty, come and join the Nazi party!\n")
            print "Sent 'The Producers - Nazi' "

        # Rainbows
        if ircmsg.find ("rainbow") != -1:
            sendmsg (channel, "Someday we'll find it, the rainbow connection. The lovers, the dreamers and me.\n")
            print "Sent 'Rainbows' "

        # Duck song
        if ircmsg.find ("duck") != -1:
            sendmsg (channel, "A duck walked up to a lemonade stand...\n")
            print "Sent 'Duck song' "

        # Misc lol, yay, etc
        if ircmsg.find ("yay") != -1:
            sendmsg (channel, "Yay! ^_^ \n")
            print "Sent 'Yay! ^_^' "
        if ircmsg.find ("lol") != -1:
            sendmsg (channel, "lol\n")
            print "Sent 'lol' "
        if ircmsg.find ("lmao") != -1:
            sendmsg (channel, "lol\n")
            print "Sent 'lol' "
        if ircmsg.find ("rofl") != -1:
            sendmsg (channel, "lol\n")
            print "Sent 'lol' "
        if ircmsg.find ("PING :tmi.twitch.tv") != -1:
#            time.sleep(random.randint(10,1200))
            sendmsg (channel, "lol\n")
            print "Sent 'lol' "

        # Crazy
        if ircmsg.find ("crazy") != -1:
            sendmsg (channel, "Crazy? I was crazy once. They locked me up in a padded room until I died. \n")
            time.sleep(2)
            sendmsg (channel, "They put 3 flowers on my grave. Two grew up, and one grew down. \n")
            time.sleep(2)
            sendmsg (channel, "The roots tickled my nose. It drove me crazy. \n")
            print "Sent 'Crazy message' "

#        # Parrot function
#        if ircmsg.find (":avicennasis!avicennasis@avicennasis.tmi.twitch.tv PRIVMSG #noobenheim :") != -1:
#            say_split = ircmsg.split (":avicennasis!avicennasis@avicennasis.tmi.twitch.tv PRIVMSG #noobenheim :")
#            sendmsg (channel, say_split [1])
#        if ircmsg.find (":noobenheim!noobenheim@noobenheim.tmi.twitch.tv PRIVMSG #noobenheim :") != -1:
#            say_split = ircmsg.split (":noobenheim!noobenheim@noobenheim.tmi.twitch.tv PRIVMSG #noobenheim :")
#            sendmsg (channel, say_split [1])

        # Owner support
        if ircmsg.find (":avicennasis!avicennasis@avicennasis.tmi.twitch.tv PRIVMSG #noobenheim :!request ") != -1:
            sendmsg (channel, "Ooo, good pick Avic! \n")
            print "Sent 'Ooo, good pick Avic!' "

        # NoobBot Harrassment 
        if ircmsg.find (":noobbot2000!noobbot2000@noobbot2000.tmi.twitch.tv PRIVMSG #noobenheim :") != -1:
            sendmsg (channel, "I'm a better bot. -_-\n")
            print "Sent 'I'm a better bot. -_-' "

        # Major-General
        if ircmsg.find ("Major-General") != -1:
            sendmsg (channel, "I am the very model of a modern Major-General,\n")
            time.sleep(5)
            sendmsg (channel, "I've information vegetable, animal, and mineral,\n")
            time.sleep(5)
            sendmsg (channel, "I know the kings of England, and I quote the fights historical\n")
            time.sleep(5)
            sendmsg (channel, "From Marathon to Waterloo, in order categorical;\n")
            time.sleep(5)
            sendmsg (channel, "I'm very well acquainted, too, with matters mathematical,\n")
            time.sleep(5)
            sendmsg (channel, "I understand equations, both the simple and quadratical,\n")
            time.sleep(5)
            sendmsg (channel, "About binomial theorem I'm teeming with a lot o' news,\n")
            time.sleep(10)
            sendmsg (channel, "With many cheerful facts about the square of the hypotenuse.\n")
            time.sleep(5)
            sendmsg (channel, "I'm very good at integral and differential calculus;\n")
            time.sleep(5)
            sendmsg (channel, "I know the scientific names of beings animalculous:\n")
            time.sleep(5)
            sendmsg (channel, "In short, in matters vegetable, animal, and mineral,\n")
            time.sleep(5)
            sendmsg (channel, "I am the very model of a modern Major-General.\n")
            time.sleep(5)
            sendmsg (channel, "I know our mythic history, King Arthur's and Sir Caradoc's;\n")
            time.sleep(5)
            sendmsg (channel, "I answer hard acrostics, I've a pretty taste for paradox,\n")
            time.sleep(5)
            sendmsg (channel, "I quote in elegiacs all the crimes of Heliogabalus,\n")
            time.sleep(5)
            sendmsg (channel, "In conics I can floor peculiarities parabolous;\n")
            time.sleep(5)
            sendmsg (channel, "I can tell undoubted Raphaels from Gerard Dows and Zoffanies,\n")
            time.sleep(5)
            sendmsg (channel, "I know the croaking chorus from The Frogs of Aristophanes!\n")
            time.sleep(5)
            sendmsg (channel, "Then I can hum a fugue of which I've heard the music's din afore,\n")
            time.sleep(10)
            sendmsg (channel, "And whistle all the airs from that infernal nonsense Pinafore.\n")
            time.sleep(5)
            sendmsg (channel, "Then I can write a washing bill in Babylonic cuneiform,\n")
            time.sleep(5)
            sendmsg (channel, "And tell you ev'ry detail of Caractacus's uniform.\n")
            time.sleep(5)
            sendmsg (channel, "In short, in matters vegetable, animal, and mineral,\n")
            time.sleep(5)
            sendmsg (channel, "I am the very model of a modern Major-General.\n")
            time.sleep(5)
            sendmsg (channel, "In fact, when I know what is meant by 'mamelon' and 'ravelin',\n")
            time.sleep(5)
            sendmsg (channel, "When I can tell at sight a Mauser rifle from a javelin,\n")
            time.sleep(5)
            sendmsg (channel, "When such affairs as sorties and surprises I'm more wary at,\n")
            time.sleep(5)
            sendmsg (channel, "And when I know precisely what is meant by 'commissariat',\n")
            time.sleep(5)
            sendmsg (channel, "When I have learnt what progress has been made in modern gunnery,\n")
            time.sleep(5)
            sendmsg (channel, "When I know more of tactics than a novice in a nunnery \n")
            time.sleep(5)
            sendmsg (channel, "In short, when I've a smattering of elemental strategy  \n")
            time.sleep(10)
            sendmsg (channel, "You'll say a better Major-General has never sat a gee.\n")
            time.sleep(5)
            sendmsg (channel, "For my military knowledge, though I'm plucky and adventury,\n")
            time.sleep(5)
            sendmsg (channel, "Has only been brought down to the beginning of the century;\n")
            time.sleep(5)
            sendmsg (channel, "But still, in matters vegetable, animal, and mineral,\n")
            time.sleep(5)
            sendmsg (channel, "I am the very model of a modern Major-General.\n")
            print "Sent 'Major-General' "

        # Moana songs
        if ircmsg.find ("Thanks") != -1:
            sendmsg (channel, "So what can I say except you're welcome?\n")
            print "Sent 'You're Welcome' "
        if ircmsg.find ("thanks") != -1:
            sendmsg (channel, "There's no need to pray, it's OK, you're welcome!\n")
            print "Sent 'You're Welcome' "
        if ircmsg.find ("thank you") != -1:
            sendmsg (channel, "I guess it's just my way of being me! You're welcome, you're welcome!\n")
            print "Sent 'You're Welcome' "
        if ircmsg.find ("Thank you") != -1:
            sendmsg (channel, "Well anyway, let me say you're welcome!\n")
            print "Sent 'You're Welcome' "
        if ircmsg.find ("shiny") != -1:
            sendmsg (channel, "Shiny! Watch me dazzle like a diamond in the rough. Strut my stuff; my stuff is so \n")
            time.sleep(5)
            sendmsg (channel, "Shiny! Send your armies but they'll never be enough. My shell's too tough!\n")
            print "Sent 'You're Welcome' "





# Main routine

Main()
exit (zero)
