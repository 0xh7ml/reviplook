from urllib.request import urlopen as html
print('''
   ____  _ ____    _              _
  |  _ \(_)  _ \  | |_ ___   ___ | |
  | |_) | | |_) | | __/ _ \ / _ \| |
  |  _ <| |  __/  | || (_) | (_) | |
  |_| \_\_|_|      \__\___/ \___/|_|
''')
print("\033[32;1mReverse Ip lookup Tool by D4rk h7ml\033[0m")
site = input("Enter Site Name plz:")
link = ("http://api.hackertarget.com/reverseiplookup/?q="+site)
domain = html(link).read().decode('utf-8')
print("\u001b[32;1msites==>\n\u001b[32;0m"+domain)
print("[ Successfully done ]")
