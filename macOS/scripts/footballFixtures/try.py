import bs4, requests, sys
from bs4 import BeautifulSoup

#---------------------------------------
toPrintAll = 0
specific = 0
toSearch = ""

#---------------------------------------
args = sys.argv
    
if ("-l" in args):
    toPrintAll = 1
if "-g" in args:
    curr = args.index("-g")
    try:
        toSearch = args[curr+1].lower()
        specific = 1
    except:
        specific = 0

#---------------------------------------
toIgnore1 = ['football', '<', '>'] #matches the whole string
toIgnore2 = ['<', '>'] #matches it anywhere in the string
toShowLeague = ['uefa', 'champions', 'premier league', 'english', 'spanish', 'la liga','italian serie a', 'american', 'mls']
toRemoveLeague = ['women', 'scottish', 'southern']

#----------------------------------------
def checkValid(x):
    
    x = x.lower().lstrip(" ").rstrip(" ")

    if x in toIgnore1:
        return 0
    
    for i in toIgnore2:
        if x.find(i) != -1:
            return 0

    return 1

def checkValidLeague(x):
    
    x = x.lower().lstrip(" ").rstrip(" ")
    
    if (toPrintAll):
        return 1
    if (specific):
        if x.find(toSearch) != -1:
            return 1
        return 0

    for i in toRemoveLeague:
        if x.find(i) != -1:
            return 0;
    for i in toShowLeague:
        if x.find(i) != -1:
            return 1

    return 0

#---------------------------------------
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#---------------------------------------

try:
    page = requests.get("https://www.skysports.com/football-fixtures")
except:
    print("No internet connection!")
    quit()

soup = BeautifulSoup(page.text, "html.parser")
fullCode = soup.prettify()
allLines = fullCode.split("\n")

#---------------------------------------
substring = "swap-text--bp30"
substring2 = "fixres__header3"
flag = 0
flag2 = 0
thres = 4
thres2 = 4
currLeague = ''
currLeagueCount = 0
nPrinted = 0
nonew = 0 

#---------------------------------------
print()
for i in allLines:
    
    if (flag2 > 0):

        flag2 += 1

        if flag2 == 2:
            currLeague = i.lstrip(" ").rstrip(" ")
            currLeagueCount = 0
            # print()
        if (flag2 == thres2):
            flag2 = 0

    if i.find(substring2) != -1:
        flag2 = 1

    if (flag > 0):
        # print(i)
        flag += 1
        
        if flag == 3:
            
            if (checkValid(i) and checkValidLeague(currLeague)):
                if (nPrinted % 2 == 0):
                    
                    if (currLeagueCount == 0):
                        
                        if (not nonew):
                            print("🏆 "+ color.BOLD + currLeague + color.END)
                            nonew = 1
                        else:
                            print("\n🏆 "+ color.BOLD + currLeague + color.END)

                    print("\t⚽ "+ color.BLUE + i.rstrip("\n").lstrip(" ") + color.END + color.BOLD + " vs " + color.END, end = '')
                    
                    currLeagueCount += 1
                else:
                    print(color.RED + i.lstrip(" ") + color.END)

                nPrinted += 1

        if (flag == thres):
            flag = 0
    if i.find(substring) != -1:
        # print(i)
        flag = 1
print()

#---------------------------------------
