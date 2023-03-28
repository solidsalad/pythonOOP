import sys
import platform
import subprocess
import json
from rich import print

#function for adding domains to the list to get tested
def editDomains(list, action):
        answer = "0"
        while (answer != ""):
            answer = input(f"type the website you want to {action} (empty enter to stop) [website/domain]: ")
            if (answer != ""):
                domain = answer
                if (action == "add") and (domain not in list):
                    list.append(domain)
                    print(list)
                if (action == "delete"):
                    if (domain in list):
                        list.remove(domain)
                        print(list)
                    else:
                        print(f"cannot find {domain}")
            else:
                 return list

#function used for pinging
def myping(host):
    parameter = '-n' if platform.system().lower()=='windows' else '-c'

    command = ['ping', parameter, "1", host]
    response = subprocess.call(command)

    if response == 0:
        return True
    else:
        return False

#make domainlist
domainlist = []

#try to open JSON file with already entered websites (if the file exists)
try:
    with open("pingTest.JSON", "r") as f:
        domainlist = json.load(f)
except:
     #leave list empty/unchanged if no JSON is found
     domainlist = domainlist

#add optional arguments to list of domains to test
if (len(sys.argv) > 2):
     for arg in sys.argv[2:]:
        if (arg not in domainlist):
            domainlist.append(arg)

#manage mode
if (sys.argv[1] == "manage"):
    #small interface for editing the list
    action = ""
    while (action != "s"):
        action = input("\nto view current list, press [V]\nto add domains to list, press [A]\nto delete domains from list, press [D]\nto save current list, press [S]\n\n")
        if (action == "v"):
            print(domainlist)
        if (action == "a"):
            domainlist = editDomains(domainlist, "add")
        if (action == "d"):
            domainlist = editDomains(domainlist, "delete")
        if (action == "s"):
            with open("pingTest.JSON", "w") as f:
                json.dump(domainlist,f)

#check mode
if (sys.argv[1] == "check"):
    #pinging the domains and saving the result
    success = []
    for domain in domainlist:
        print(myping(domain))
        success.append(myping(domain))
    print("\n")
    #save test result to JSON
    with open("pingResult.JSON", "w") as f:
                json.dump(success,f)
    #save sites to JSON
    with open("pingTest.JSON", "w") as f:
                json.dump(domainlist,f)

    #converting results to strings and adding them to the html
    html = open("index.html", "w")

    #reset html to an empty one
    template = open("template.html","r")
    interface = template.read()
    template.close()
    #converting info to html layout
    liList = []
    for i in range(len(domainlist)):
        if (success[i] == True):
            testRes = "Connection success"
            color = "[green]"
        else:
            testRes = "Connection failed"
            color = "[red]"
        liList.append(f"\n\t\t\t<p>{domainlist[i]}</p>\n\t\t\t<p class=\"{success[i]}\">{testRes}</p>")
        #amount of tabs based on length of address
        tab =  int(3 - float(len(domainlist[i])/15)) * "\t"
        #print results in console
        print(f"{domainlist[i]}{tab}{color}{testRes}")
    print("\n")
    liString = "\n\t\t</li>\n\t\t<li>".join(liList)
    interface = interface.replace('''<ul></ul>''', f"<ul>\n\t\t<li>{liString}\n\t\t</li>\n\t</ul>")
    html.write(f"{interface}")
    html.close()