from pyfiglet import figlet_format
import ip_address
from faker import Faker
from shodan import Shodan
from pprint import pprint
import json
import requests
import re
import sys

def banner(x):
        #Banner/Logo at the beginning
        ascii_banner = figlet_format(x)
        print(ascii_banner)
        
def FakeIP():
    #Generate Random IP
    faker = Faker()
    ip_addr = faker.ipv4()  
    print("Random Ip >>> "+ip_addr)

def jsreq(g):
    #JSON Request for Ip Ifo
    _ = requests.get(f"http://ip-api.com/json/{g}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query")
    x = _.json()
    return x

def validate(v):
    #Validate if IP is true or not
    if numbers := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$",v):
        for i in range(1,5):
                if int(numbers.group(i)) > 255 or int(numbers.group(i)) < 0 :
                    return False
        print("Valid IP")
    else:
        return False


def main():
    banner("IP CREEPER")
    print('By Rahul "Rocks75" Gonal')
    print("Only for fair means :)")
    print("0. View my IP")
    print("1. IP Lookup (with the Shodan option)")
    print("2. Get a Random IP address")
    print("\n")
    print("Use Ctrl+c to exit at any stage")
    print("\n")

    while True:
        try:
            Inpt = input("Please select your action >>> ")
            Inpt  = Inpt.lower()

            if "0" == Inpt:
                Usr =  ip_address.get()
                print("Your IP Address >>>",Usr)
                continue

            elif "1" == Inpt:
                IP = input("Enter the IP address or domain address >>> ")
                if validate(IP) == False:
                    print("Invalid IPv4")
                    break
                print("+++++++++++++++++++")
                print("    Base Results   ")
                print("+++++++++++++++++++")
                pprint(jsreq(IP))
                while True:
                    choice = input("Do you want to do a Shodan lookup? (y/n) >>> ")
                    if "y" in choice.lower():
                        print("To continue enter your API key below or get one from https://developer.shodan.io/api/requirements")
                        print("You need to create an account for the key, if it still doesn't work try resetting the key at https://account.shodan.io/")
                        UserApp = str(input("Please enter your Shodan API Key >>> "))
                        print("To exit, press Ctrl+c")
                        api = Shodan(UserApp)
                        ipinfo = api.host(f'{IP}')
                        print("+++++++++++++++++++")
                        print("Results from Shodan")
                        print("+++++++++++++++++++")
                        pprint(ipinfo)
                        break
                        
                        
                    if "n" in choice.lower():
                        break 

            elif "2" or "random "== Inpt:
                FakeIP()
                continue

        except (EOFError,KeyboardInterrupt):
                break

if __name__ == "__main__":
     main()
