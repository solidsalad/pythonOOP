import sys
import platform
import subprocess

def addDomains(list):
        answer = ""
        while (answer != "0"):
            answer = input("geef mij een: \"[website/domain], [aantal pings]\": ")
            if (answer != "0"):
                domain = answer.split(", ")
                list.insert(domain)

try:
    domainlist = open("pingTest.JSON", "r")
    action = ""
    while (action != "s"):
        action = input("to view current list, press [V]\nto add domains to list, press [A]\nto use current list, press [S]\n\n")
        if (action == "v"):
             print(domainlist)
        if (action == "a"):
             addDomains(domainlist)     
except:
    domainlist = []
    print("no domains have been listed for testing, please add at least one (answer 0 to stop)")
    addDomains(domainlist)

domainsJSON = open("pingTest.JSON", "w")
domainsJSON.write
#function used for pinging
def myping(host):
    parameter = '-n' if platform.system().lower()=='windows' else '-c'

    command = ['ping', parameter, '1', host]
    response = subprocess.call(command)

    if response == 0:
        return True
    else:
        return False

for    
print(myping("www.google.com"))
html = open("index.html", "w")

