#coding: utf-8
import argparse, requests

def banner():
    print('''
\033[1;31m#########################################################   
## \033[1;33m__  __    __                      ___               \033[1;31m##
## \033[1;33m\ \/ /__ / _|_ _ __ _ _ __  ___  / __| __ __ _ _ _  \033[1;31m##
##  \033[1;33m>  <___|  _| '_/ _` | '  \/ -_) \__ \/ _/ _` | ' \ \033[1;31m##
## \033[1;33m/_/\_\  |_| |_| \__,_|_|_|_\___| |___/\__\__,_|_||_|\033[1;31m##
##                                                     ##
##     	\033[1;36mSimple clickjacking scan | By diego tella \033[1;31m     ##
#########################################################\033[1;33m                                                     
                                                                    
    ''')

def verif(headers, url):
    if "x-frame-options" in headers:
        print("\033[1;31m[+] " + url + " contains x-frame-options. Not vulnerable.")
    else:
        print("\033[1;92m[!] Not x-frame-options in " + url + ". Possible vulnerability!")

def ScanURL(site):
    hed = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0", "Accept-Encoding": "gzip, deflate, br", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
    req = requests.get(site, headers=hed)
    headers = req.headers
    verif(headers, site)

def ScanList(lista):
    hed = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0", "Accept-Encoding": "gzip, deflate, br", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
    r = open(lista, 'r')
    for links in r.readlines():
        i = links.rstrip('\n')
        req = requests.get(i, headers=hed)
        headers = req.headers
        verif(headers, i)

banner()
        
parser = argparse.ArgumentParser(description='Simple scan for the X-Frame-Options header to find out if a site is vulnerable to Clickjacking. ')
parser.add_argument('-u', '--url', type=str, help='URL target')
parser.add_argument('-l', '--list', type=str, help='List of sites to scan')
args = parser.parse_args()

if args.url is None and args.list is None:
    parser.error("at least one of --url and --list required")

url = args.url
lista = args.list

if url:
    ScanURL(url)
elif lista:
    ScanList(lista)

