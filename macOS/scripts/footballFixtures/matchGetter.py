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
toShowLeague = ['uefa', 'champions', 'europa','premier league', 'english', 'spanish', 'la liga','italian serie a', 'american', 'mls', 'bundesliga']
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
def convertTime(time):

    #for IST: add 4.5 hrs
    #for DXB: add 3 hrs
    
    values = time.split(":")
    hrs = int(values[0])
    mins = int(values[1])
    
    if (mins + 30 >= 60):
        hrs += 1

    hrs = str((hrs+4)%24)
    mins = str((mins+30)%60)
    
    if (hrs == '0'):
        hrs = '00'
    if (mins == '0'):
        mins = '00'

    return str(hrs)+':'+str(mins)

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

flag3 = 0
savedTime = ''

flag4 = 0
savedScore1 = ''
savedScore2 = ''

#---------------------------------------
print()
for i in allLines:
    
    if flag4 > 0:
        flag4 += 1
        
        if savedScore1:
            savedScore2 += i.lstrip(" ").rstrip(" ")
        else:
            savedScore1 += i.lstrip(" ").rstrip(" ")
        
        if flag4 == 2:
            flag4 = 0


    if i.find("matches__teamscores-side") != -1:
        flag4 = 1

    if flag3 > 0:

        flag3 += 1

        if flag3 == 2:
            savedTime = convertTime(i.lstrip(" ").rstrip(" "))
            flag3 = 0

    if i.find("matches__date") != -1:
        flag3 = 1

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


                    # if (savedScore1 and savedScore2):
                        # print ("\t\t  " + color.BLUE + savedScore1 + color.END + color.BOLD + " - " + color.END + color.RED + savedScore2 + color.END)
                        # savedScore1 = ""
                        # savedScore2 = ""

                    if (savedTime):
                        print("\t\t⏱  " + color.YELLOW + savedTime + color.END)
                        savedTime = ''

                    if (savedScore1 and savedScore2):
                        print ("\t\t" + color.BLUE + savedScore1 + color.END + color.BOLD + " - " + color.END + color.RED + savedScore2 + color.END)
                        savedScore1 = ""
                        savedScore2 = ""
                    # if (savedScore1 and savedScore2):
                        # print ("\2t🔴  " + savedScore1 + " - " + savedScore2  + " 🔵")
                        # savedScore1 = ""
                        # savedScore2 = ""
                nPrinted += 1
                savedTime = ''
                savedScore1 = ''
                savedScore2 = ''

        if (flag == thres):
            flag = 0
    if i.find(substring) != -1:
        # print(i)
        flag = 1
print()

#---------------------------------------
