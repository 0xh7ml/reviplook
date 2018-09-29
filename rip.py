"""
#Simple reverse ip doman lookup script By D4rk h7ml
#facebook:www.facebok.com/uiddarkhtml/
#website:www.darkerror.net/
#youtube:www.youtube.com/DarkError
#use:python3 reviplook.py

"""
from urllib.request import urlopen as html
site = input("Enter Site Name plz:")

link = ("http://api.hackertarget.com/reverseiplookup/?q="+site)
domain = html(link).read()
file = open("domain.txt","wb")
file.write(domain)
print("[ Successfully done check domain.txt ]")
