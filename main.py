import requests
from bs4 import BeautifulSoup

YallaShoutWebsiteUrl = "https://shotz.yalla-shoot-tv.live/matches-today/ "

ReqestGet = requests.get(YallaShoutWebsiteUrl)

soup = BeautifulSoup(ReqestGet.text, 'html.parser')


def GetTeamsName():
  TeamNames = list()
  
  GetTeamsName = soup.find_all("div",{"class":"team-name"})
  for div in GetTeamsName:
      TeamNames.append(div.text)
      print(div)
  for names in TeamNames :
      print(names)
      with open("TeamNames.txt","a+",encoding="utf-8") as f:
           if f.writable() == True:
            TransferData = f.write(names+"\n") 
           else:
            print("the file is not writable")

def Score():
    GetScore = soup.find_all("div",{"class":"result"})
    Scores = list()
    for score in GetScore:
        Scores.append(score.text)
    print(Scores)
    
def started():
    datelive = soup.find_all("div",{"class":"date live"})
    dateend= soup.find_all("div",{"class":"date end"})
    datenotstarted_ =  soup.find_all("div",{"class":"not-start"})
    
    startedList = list()
    endList = list()
    datenotstartedlist = list()
    
    for notstarted in datenotstarted_:
        print(notstarted.text)
    for dateends in dateend:
        print(dateends.text)
    for started in datelive:
        print(started.text)
        
        
    