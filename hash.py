from random import choice
from string import ascii_lowercase as letters

email_domain=['yahoo.com','gmail.com','gowti.com']

quotes=["you can do it","no pain no gain","sacrifice your present now to get your future"]

def get_quotes(quote):
    return choice(quotes)

def generate_name(length_of_name):
    return ''.join(choice(letters) for num in range(length_of_name))

def get_domains(email_domains):
    return choice(email_domain)

def generate_email(length_of_name,email_domains,total_mails,quotes):
    with open("hashdata.txt", "w") as to_write:
        for num in range(total_mails):
            key =generate_name(length_of_name)+ "@" +get_domains(email_domains)
            values=get_quotes(quotes)
            to_write.write( key +":" + values +"\n")


generate_email(10,email_domain,10,quotes)
