import random
import string
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
    "No one will be able to type my password in because they'll cringe typing the word Tumblr and also "
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

# Make your password more difficult to communicate
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

# List comprehension in one line because I am a sadist
def pass16():
    return ''.join([str(random.randrange(10)) for i in range(20)])
generators.append(pass16)

# Memory locations are basically random, right?
def pass17():
    temp = 1
    return id(temp)
generators.append(pass17)

#
def pass18():
    return None
generators.append(pass18)

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

# Outsource the labor to a different website!
def pass50(length):
    resp = requests.get('http://www.random.org/passwords/?num=1&len=' + str(length) + '&format=html&rnd=new')
    if resp.status_code == 200:
        ind = resp.text.find("Here are your random passwords")
        nextind = resp.text.find("<li>", ind)
        return resp.text[nextind+4:nextind+4+length]
    else:
        return "Fuck the Internet isn't loading guess your password will have to be " + pass1()
generators.append(lambda: pass50(20))

# Runs everything because we have ultimate power
def master():
    for g in generators:
        print(g())

master()
