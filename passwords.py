import sys
import time
import random
import string
from datetime import datetime, tzinfo, timedelta

import requests.exceptions
from bs4 import BeautifulSoup
import urllib.request

generators = []

l337_dict = {
    'a': '4',
    'e': '3',
    'i': '1',
    's': '5',
    'z': '2',
    'o': '0',
    't': '7',
    'b': '8',
    'g': '9'
}

no_say_good = [
    "My password is: ",
    "Actually that was my password, but I'll say it again: ",
    "It's pretty cursed: ",
    "lmao can you believe i set it to ",
    "I can't remember, it might be ",
    "All I know is it isn't ",
    "Oh god what if it's ",
    "HOLY FUCK CHECK MY NEW PASSWORD: ",
    "One Two Percent Sign Asterisk ",
    "One fish two fish red fish my password is ",
    "Alexa, add this to my shopping cart: ",
    "Hey Google, set my password to ",
    "As Shakespeare once said, "
    "Knock once if you up; otherwise, say ",
    "My favorite color is ",
    "Bro, are you listening? This is the password, it's not something like ",
    "According to all known laws of aviation, there is no way a bee should be able to ",
    "No one will be able to type my password in because they'll cringe typing the word Tumblr and also ",
    "Actually, it's pronounced "
]

major_arcana = [
    "The Fool",
    "The Magician",
    "The High Priestess",
    "The Empress",
    "The Emperor",
    "The Hierophant",
    "The Lovers",
    "The Chariot",
    "Strength",
    "The Hermit",
    "Wheel of Fortune",
    "Justice",
    "The Hanged Man",
    "Death",
    "Temperance",
    "The Devil",
    "The Tower",
    "The Star",
    "The Moon",
    "The Sun",
    "Judgement",
    "The World"
]

suits = [
    "Wands",
    "Cups",
    "Swords",
    "Coins"
]

ranks = [
    "Ace",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Page",
    "Knight",
    "Queen",
    "King"
]



class Central(tzinfo):

    def utcoffset(self, dt):
        return timedelta(hours=-6) + self.dst(dt)

    def dst(self, dt):
        d = datetime(dt.year, 3, 8)  # 2nd Sunday in March
        self.dston = d + timedelta(days=6-d.weekday())
        d = datetime(dt.year, 11, 1)  # 1st Sunday in Nov
        self.dstoff = d + timedelta(days=6-d.weekday())
        if self.dston <= dt.replace(tzinfo=None) < self.dstoff:
            return timedelta(hours=1)
        else:
            return timedelta(0)

    def tzname(self, dt):
        return 'Central'

EMOJI_RANGES_UNICODE = [
    ('\U0001F300', '\U0001F320'),
    ('\U0001F330', '\U0001F335'),
    ('\U0001F337', '\U0001F37C'),
    ('\U0001F380', '\U0001F393'),
    ('\U0001F3A0', '\U0001F3C4'),
    ('\U0001F3C6', '\U0001F3CA'),
    ('\U0001F3E0', '\U0001F3F0'),
    ('\U0001F400', '\U0001F43E'),
    ('\U0001F440', '\U0001F4F7'),
    ('\U0001F4F9', '\U0001F4FC'),
    ('\U0001F500', '\U0001F53C'),
    ('\U0001F540', '\U0001F543'),
    ('\U0001F550', '\U0001F567'),
    ('\U0001F5FB', '\U0001F5FF'),
    ('\U0001F300', '\U0001F32C'),
    ('\U0001F330', '\U0001F37D'),
    ('\U0001F380', '\U0001F3CE'),
    ('\U0001F3D4', '\U0001F3F7'),
    ('\U0001F400', '\U0001F4FE'),
    ('\U0001F500', '\U0001F54A'),
    ('\U0001F550', '\U0001F579'),
    ('\U0001F57B', '\U0001F5A3'),
    ('\U0001F5A5', '\U0001F5FF'),
    ('\U0001F300', '\U0001F579'),
    ('\U0001F57B', '\U0001F5A3'),
    ('\U0001F5A5', '\U0001F5FF')
]

NINTENDO_BUTTONS = [
    "UP",
    "DOWN",
    "LEFT",
    "RIGHT",
    "A",
    "B",
    "X",
    "Y",
    "R",
    "ZR",
    "L",
    "ZL",
    "C",
    "Z",
    "START",
    "SELECT",
    "+",
    "-",
    "LSTICK",
    "RSTICK"
]

PERSONAL_QUESTIONS = [
    "What is your name?",
    "What is your quest?",
    "What was the name of your first pet?",
    "What is your mother's maiden name?",
    "What was the name of your first-grade teacher?",
    "What is your dream car model?",
    "What is your street number?",
    "What is your favorite color?",
    "What is your least favorite color?",
    "Who is your favorite Backyardigan?",
    "What are the last 4 digits of your SSN?",
    "What are the digits of your credit card number? Don't forget those three wacky digits on the back!",
    "What is your favorite use for dijon mustard?",
    "In a perfect world, how many bagles would you own?",
    "How many fingers am I holding up?",
    "Who is your favorite philosopher from 1266 A.D. to 1738? A.D.?",
    "How many times have you wanted to meet Earnest Hemmingway?",
    "On what day did you first realize that the Baskin Robins logo has a 31 in it?",
    "What is your most embarrassing secret? Don't be shy :)",
    "What is your 4chan username?",
    "How many l's are in your favorite novel?",
    "What is the cash price of unleaded gasoline per gallon at your nearest station?",
    'How would you rate your pain on a 0 to 10 scale, where zero means "no pain," and 10 means "the worst possible pain."',
    "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
    "How do you get your weed? Hook a brother up...",
    "Please rate how attractive you find the following letter: s",
    "Please rate how attractive you find me ~uwu✿:",
    "What happened to Amelia Earhart?",
    "Why are you so sure that the Earth is round?",
    "How ~shrexy~ do you feel on a day-to-day basis? 😉",
    "Describe an example of your leadership experience in which you have positively influenced others, helped resolve disputes or contributed to group efforts over time."
]

# Pure and simple, can't be cracked
# Very soon, you will be hacked
def pass1():
    return "password"
generators.append(pass1)

# 100 passwords you should use (number 17 will shock you)
def pass2():
    with open("password_suggestions.txt", 'r') as pwd_file:
        options = pwd_file.read().splitlines()
        return options[random.randrange(len(options))]
generators.append(pass2)

# This is actually quality guys
def pass3(length, allowSpecial, allowSpaces):
    options = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    if allowSpecial:
        options = options + list("!#$%&()*+,-:<=>?@[]^_`{|}~")
    if allowSpaces:
        options = options + [' ']
    to_return = ""
    for i in range(0, length):
        to_return += options[random.randrange(len(options))]
    return to_return
generators.append(lambda: pass3(20, True, False))

# L337 SP34K for 3p1c G4m3rz 0nly
def pass4():
    original = pass2()
    l337_password = []
    for i in range(len(original)):
        if original[i] in l337_dict:
            l337_password.append(l337_dict[original[i]])
        else:
            l337_password.append(original[i])
    return ''.join(l337_password)
generators.append(pass4)

# PIN stands for Pasta In Nigeria
def pass5():
    output = ""
    for i in range(4):
        output += str(random.randrange(10))
    return output
generators.append(pass5)

# coect hons batry stappel
# but with more populr sellings :)
# thes is wat the ppl wnt !!
def pass6(num_words, spaces):
    with open("bad_spelling.txt", 'r') as pwd_file:
        options = pwd_file.read().splitlines()
        output = ""
        for i in range(num_words):
            output += options[random.randrange(len(options))]
            if spaces and i < num_words - 1:
                output += " "
        return output
generators.append(lambda: pass6(4, True))

# Correct horse battery staple but you have to specify the words
def pass7(*words):
    output = ""
    for word in words:
        output += word
    return output
generators.append(lambda: pass7("one", "two", "three", "four", "i", "declare", "a", "thumb", "war"))

# Helps you generate your very own password!!!
def pass8():
    return "def pass1():\n\treturn \"password\"\n\tgenerators.append(pass1)"
generators.append(pass8)

# Makes your password more difficult to communicate
def pass9():
    return "Your new password is \"" + no_say_good[random.randrange(len(no_say_good))] + pass3(20, False, False) + "\""
generators.append(pass9)

# It's recursive AND bad
def pass10(phrase, depth):
    if depth > 0:
        phrase += pass10(phrase, depth - 1)
    return phrase
generators.append(lambda: pass10("ps", 10))

# Let's use currying! This will definitely be more secure
def pass11():
    def generate():
        def last_char():
            def alpha():
                my_options = list(string.ascii_lowercase)
                return my_options[random.randrange(len(my_options))]
            def ALPHA():
                my_options = list(string.ascii_uppercase)
                return my_options[random.randrange(len(my_options))]
            def digit():
                return str(random.randrange(10))
            def symbol():
                my_options = list("!#$%&()*+,-:<=>?@[]^_`{|}~")
                return my_options[random.randrange(len(my_options))]
            my_options = [alpha, ALPHA, digit, symbol]
            return my_options[random.randrange(len(my_options))]
        def a(char1):
            def b(char2):
                def c(char3):
                    def d(char4):
                        def e(char5):
                            def f(char6):
                                def g(char7):
                                    def h(char8):
                                        def i(char9):
                                            def j(char10):
                                                def k(char11):
                                                    def l(char12):
                                                        def m(char13):
                                                            def n(char14):
                                                                def o(char15):
                                                                    def p(char16):
                                                                        return char1() + char2() + char3() + char4() + \
                                                                                char5() + char6() + char7() + char8() + \
                                                                                char9() + char10() + char11() + char12() + \
                                                                                char13() + char14() + char15() + char16()
                                                                    return lambda: p(last_char())
                                                                return lambda: o(last_char())
                                                            return lambda: n(last_char())
                                                        return lambda: m(last_char())
                                                    return lambda: l(last_char())
                                                return lambda: k(last_char())
                                            return lambda: j(last_char())
                                        return lambda: i(last_char())
                                    return lambda: h(last_char())
                                return lambda: g(last_char())
                            return lambda: f(last_char())
                        return lambda: e(last_char())
                    return lambda: d(last_char())
                return lambda: c(last_char())
            return lambda: b(last_char())
        return lambda: a(last_char())
    return generate()()()()()()()()()()()()()()()()()
generators.append(pass11)

# Scams you out of your money but a different amount each time
def pass12():
    cost = str(random.randrange(1000000,10000000))
    return "You've won a free password! It's " + cost + ". To claim it, send $" + cost + " to hello@danieldeanda.tech"
generators.append(pass12)

# This one is the unlucky number so we generate a password but you don't get to see it
# (for security purposes)
def pass13(length):
    password = pass3(length, True, False)
    output = "Password: "
    for char in password:
        output += "*"
    return output
generators.append(lambda: pass13(20))

# Mad Libs make for great passwords I'm sure
def pass14():
    noun = input("Alright, I need a plural noun: ")
    adjective = input("Next, I need an adjective: ")
    gerund = input("Finally, I need a verb ending in 'ing': ")
    return "Poggers! Your password is: \"" + noun + " look " + adjective + " when I'm " + gerund + "\""
generators.append(pass14)

# If you shout at your computer it will let you in faster
def pass15():
    return pass2().upper()
generators.append(pass15)

# List comprehension in one "line" because I am a sadist
def pass16():
    return ''.join(
                    [
                        (   list(string.ascii_lowercase) + \
                            list(string.ascii_lowercase) + \
                            [str(j) for j in range(10)] \
                        )[random.randrange(26+26+10)] for i in range(20) \
                    ]
                  )
generators.append(pass16)

# Memory locations are basically random, right?
def pass17():
    temp = 1
    return id(temp)
generators.append(pass17)

# The password contains instructions to celebrate your birthday and our failing democracy
def pass18(num_dudes):
    output = ""
    for i in range(num_dudes):
        output += "heckin vote dude "
    return output
generators.append(lambda: pass18(num_dudes=5))

# Tarot cards are probably secure
def pass19():
    card = random.randrange(78)
    if card < 22:
        return major_arcana[card]
    else:
        return ranks[(card - 22) % 14] + " of " + suits[(card - 22) // 14]
generators.append(pass19)

# To remember your password you must unsolve a Junior Jumble
def pass20(word):
    output = ""
    options = list(word)
    while len(options) > 0:
        output += options.pop(random.randrange(len(options)))
    return output
generators.append(lambda: pass20("Junior Jumble"))

# How to not be drunk for Jesus: the password maker (but only in MN)
def pass21(is_sacramental, is_jesus):
    current = datetime.now(tz=Central())
    if is_jesus:
        return "the wine was inside you the whole time :)"
    if is_sacramental:
        return "Alright ya little rascal your password is " + pass3(20, True, False)
    # 6 stands for Sunday
    elif current.weekday() == 6 and current.hour > 2 and current.hour < 12 or \
         current.weekday() != 6 and current.hour > 2 and current.hour < 8:
        return "It is too holy for password generation"
    else:
        return pass3(20, True, False)
generators.append(lambda: pass21(False, False))

# For Taylor Swift fans: generates passwords using the lyrics to "22"
def pass22(num_words, spaces):
    with open("twenty_two_lyrics.txt", 'r') as lyrics_file:
        options = lyrics_file.read().split()
        output = ""
        for i in range(num_words):
            output += options[random.randrange(len(options))]
            if spaces and i < num_words - 1:
                output += " "
        return output
generators.append(lambda: pass22(4, True))

# EMOJIS! ARE! PASSWORDS! :weary:
def pass23():
    my_dict = {}
    sum = 0
    for tup in EMOJI_RANGES_UNICODE: # 'tup dude
        sum += 1 + ord(tup[1]) - ord(tup[0])
        my_dict[sum] = tup
    def gen_emoji():
        my_emoji = random.randrange(sum)
        prev_key = 0
        for key in my_dict.keys():
            if my_emoji <= key:
                return chr(ord(my_dict[key][0]) + my_emoji - prev_key)
            else:
                prev_key = key
    output = ""
    for i in range(20):
        output += gen_emoji()
    return output
generators.append(pass23)

# A password generated by a password generator using password generators
def pass24(num_words, spaces):
    with open("passwords.py", 'r') as me:
        options = me.read().split()
        output = ""
        for i in range(num_words):
            output += options[random.randrange(len(options))]
            if spaces and i < num_words - 1:
                output += " "
        return output
generators.append(lambda: pass24(4, False))

# Generates a PIN but very slowly
def pass25():
    num = random.randrange(9000)
    output = 1000
    while num > 0:
        output += 1
        num -= 1
    return output
generators.append(pass25)

# Hashes your password because a hash is basically a password
def pass26(password):
    output = 0
    for i in range(len(password)):
        output += pow(2, i) * ord(password[i])
    return str(output)
generators.append(lambda: pass26(pass3(20, True, False)))

# long passwords are more secure
# "Passwords must be fewer than 64 characters long? No fuk u"
def pass27():
    password = ["password"] * 50
    return ''.join(password)
generators.append(pass27)

# They use math in cryptography so why not here
# Sums are complicated, hold my beer
def pass28():
    password = 0
    now = str(time.time())
    for c in now:
        if c != '.':
            password += int(c)
    return password
generators.append(pass28)

# 123456 and 12345678 are popular passwords - but why stop there?
def pass29(max=10):
    password = [str(x) for x in range(1,max+1)]
    return ''.join(password)
generators.append(lambda: pass29(20))

# Generates a password using secret techniques from Olive Garden
def pass30():
    before = time.time()
    x = input("Tell me when to stop adding parmesan to your password by pressing [enter]... ")
    after = time.time()
    return after - before
generators.append(pass30)

# Konami used this so its probably secure
def pass31(length=10):
    password = [NINTENDO_BUTTONS[random.randrange(len(NINTENDO_BUTTONS))] for x in range(length)]
    return " ".join(password)
generators.append(pass31)

# security questions are secure for a reason - why not use it for your password?
def pass32():
    password = []
    for i in range(3):
        password.append(input(PERSONAL_QUESTIONS[random.randrange(len(PERSONAL_QUESTIONS))] + ' '))
    return ''.join(password)
generators.append(pass32)

# Is your computer requiring you change your password every 90 days? Try this trick!
def pass33(prev_password):
    last_digit = prev_password[-1]
    if last_digit.isdigit():
        return prev_password[:-1] + str(int(last_digit) + 1)
    else:
        return prev_password + "1"
generators.append(lambda: pass33("password5"))

# The suspense is killing me
def pass34():
    print("You're so close to getting a brand new password!")
    time.sleep(4)
    print("Isn't it exciting?!")
    time.sleep(4)
    print("We're almost ready to make it...")
    time.sleep(4)
    print("Adding the finishing touches...")
    time.sleep(4)
    print("You can almost taste it!")
    time.sleep(4)
    print("Here comes the garnish!")
    time.sleep(4)
    print("Let's just take in the moment, shall we?")
    time.sleep(4)
    print("Okay. Deep breaths. Drumroll, please!")
    time.sleep(4)
    print("*drumroll sounds*")
    time.sleep(4)
    return pass1()
generators.append(pass34)

# Now the random has become the randee
def pass35():
    info = random.getstate()
    return info[1][random.randrange(len(info[1]))]
generators.append(pass35)

# Multi-factor authentication (INTEGERS ONLY YOU DOOFUS)
def pass36(num):
    if not isinstance(num, int):
        return None
    now = 2
    is_prime = True
    while now <= num/2:
        if num % now == 0:
            is_prime = False
            break
        now += 1
    if is_prime:
        return "Multi-factor authentication failed; the input was single-factor"
    else:
        return "Input confirmed to be multi-factor"
generators.append(lambda: pass36(1))

# Kids are always on their instagraphs and snatchpats, maybe we can relate to them through photos?
def pass37(filename):
    password = []
    with open(filename, "rb") as file:
        for i in range(12):
            byte = file.read(1)
            int_byte = int.from_bytes(byte, byteorder=sys.byteorder, signed=False)
            hex_str = hex(int_byte)[2:].zfill(2)
            char1 = int(hex_str[0],16) % (127-33) + 33
            char2 = int(hex_str[1],16) % (127-33) + 33
            password.append(chr(char1))
            password.append(chr(char2))
    return ''.join(password)
generators.append(lambda: pass37("important_password_source.png"))

# Makes your very own alphabet song as a password
def pass38():
    alphabet = list(string.ascii_lowercase)
    random.shuffle(alphabet)
    return ''.join(alphabet)
generators.append(pass38)

# Generates passwords that show you just how confusing programming can be
def pass39(num_pairs):
    password = ''
    l_left = r_left = num_pairs
    while l_left > 0 or r_left > 0:
        choice = random.randint(0, 1)
        if choice == 0:
            if l_left > 0:
                password += '{'
                l_left -= 1
            else:
                password += '}'
                r_left -= 1
        else:
            if r_left > 0 and l_left < r_left:
                password += '}'
                r_left -= 1
            else:
                password += '{'
                l_left -= 1
    return password
generators.append(lambda: pass39(10))

#
def pass40():
    pass

# Generates a password by generating a password
def pass49():
    generator = generators[random.randrange(len(generators))]
    return generator()

# Outsource the labor to a different website!
def pass50(length):
    resp = requests.get('http://www.random.org/passwords/?num=1&len=' + str(length) + '&format=html&rnd=new')
    if resp.status_code == 200:
        ind = resp.text.find("Here are your random passwords")
        nextind = resp.text.find("<li>", ind)
        return resp.text[nextind+4:nextind+4+length]
    else:
        return "Fuck the Internet isn't loading guess your password will have to be \"" + pass1() + "\""
generators.append(lambda: pass50(20))

# Runs everything because we have ultimate power
def master():
    for g in generators:
        print(g())

master()
