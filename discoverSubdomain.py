#!usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from optparse import OptionParser
import sys
from termcolor import colored

class Subdomain():
    def __init__(self):
        self.about()
        self.script_desc()

    def arguman_al(self):
        parse = OptionParser(description=self.description,epilog=self.kullanim,prog=self.program)
        parse.add_option("-d", "--domain", dest="domain", help="Hedef domain adresi")
        (options, arguments) = parse.parse_args()
        if not options.domain:
            parse.error("[-] Lutfen bir domain belirtin,daha fazla bilgi icin --help kullanın.")
        return options

    def request(self,url):
        try:
            if "http://" in url   or "https://" in url:
                return requests.get(url)
            else:
                return requests.get("http://"+url)
        except requests.exceptions.ConnectionError:
            pass
        except requests.exceptions.InvalidURL:
            pass
        except UnicodeError:
            pass


    def discover(self,domain):
        print(colored('[+] Hedef Domain:' + domain, 'green'))
        with open("subdomain.txt", "r") as subdomainlist:
            for line in subdomainlist:
                word = line.strip()
                url = word + "." + domain
                response = self.request(url)
                if response:
                    print(colored("[+] Keşfedilen subdomain --> ","blue")+ url)



    def script_desc(self):
        self.program="discoverSubdomain"
        self.kullanim="""Ornek Kullanim1: python .\discoverSubdomain.py -domain google.com 
        \n\n\n\n\n 
        Ornek Kullanim2: python .\discoverSubdomain.py -d google.com """
        if sys.version_info[0] >= 3:
            self.description = "Hedef domain adresinin subdomainlerini keşfeden  python scripti"
        else:
            self.description = unicode("Hedef domain adresinin subdomainlerini keşfeden  python scripti", "utf8")
            self.kullanim = unicode(self.kullanim,"utf8")


    def about(self):
        print(colored("#  ____        _       ____                        _       ", "green"))
        print(colored("#/ ___| _   _| |__   |  _ \  ___  _ __ ___   __ _(_)_ __  ", "green"))
        print(colored("#\___ \| | | | '_ \  | | | |/ _ \| '_ ` _ \ / _` | | '_ \ ", "green"))
        print(colored("# ___) | |_| | |_) | | |_| | (_) | | | | | | (_| | | | | |", "green"))
        print(colored("#|____/ \__,_|_.__/  |____/ \___/|_| |_| |_|\__,_|_|_| |_|", "green"))
        print(colored("# author      :","green")+"Mustafa Dalga")
        print(colored("# linkedin    :","green")+"https://www.linkedin.com/in/mustafadalga")
        print(colored("# github      :","green")+"https://github.com/mustafadalga")
        print(colored("# title       :","green")+"discoverSubdomain.py")
        print(colored("# description :","green")+"Hedef domain adresinin subdomainlerini keşfeden  python scripti")
        print(colored("# date        :","green")+"30.05.2019")
        print(colored("# version     :","green")+"1.0")
        print("#==============================================================================")

    def keyboardinterrupt_message(self):
        print("[-] CTRL+C basıldı. Uygulamadan çıkılıyor...")
        print("[-] Uygulamadan çıkış yapıldı!")

try:
    subdomain=Subdomain()
    options=subdomain.arguman_al()
    subdomain.discover(options.domain)
except KeyboardInterrupt:
    subdomain.keyboardinterrupt_message()