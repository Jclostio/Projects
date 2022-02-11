from io import BytesIO
from PIL import Image
import requests
import json
import time

def auth():
    url = "https://api.aniapi.com/v1/auth/me"
    headers={'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjkzNyIsIm5iZiI6MTY0MTc2Nzg2NSwiZXhwIjoxNjQ0MzU5ODY1LCJpYXQiOjE2NDE3Njc4NjV9.6WZdpwL1uwdciPxcITYl8eXixU_HKIBEy0dphtm5zlc'}
    resp = requests.get(url,headers=headers)
    return resp.status_code

def getJsonText():
    genreString = ""
    userGenre = input("What Genre(s) do you like?: ")
    genreList = userGenre.split(", ")
    for genre in genreList:
        if(genreString == ""):
            genreString = genreString + genre
        else:
            genreString = genreString + "," + genre

    mainUrl = "https://api.aniapi.com/v1/anime?genres=" + genreString
    resp = requests.get(mainUrl).text
    jsonText = json.loads(resp)
    return jsonText

def showImage(jsonText, num):
    i = 0
    for key in jsonText:
        if(i == num-1):
            coverImage = key["cover_image"]
            response = requests.get(coverImage)
            img = Image.open(BytesIO(response.content))
            img.show()
            break
        else:
            i += 1
            continue


def printRecs(jsonText, rand, numOfRecs):
    userLang = input("Would you like the titles in Japanese (j) or English? (e): ")
    print("\nHere are " + numOfRecs + " recommendations:\n")
    i = 0
    incrementer = 1
    try:
        if(rand):
            jsonText = jsonText["data"]
        else:
            jsonText = jsonText["data"]["documents"]
        for key in jsonText:
            AllTitles = key["titles"]
            if(userLang == 'j'):
                print("(" + str(incrementer) + ") " + AllTitles['jp'])
            else: 
                print("(" + str(incrementer) + ") " + AllTitles['en'])
            i += 1
            incrementer += 1
            if(i == 10):
                userCont = input("Would you like another 10 recommendations? (y/n): ")
                if(userCont == 'y'):
                    i = 0
                    continue
                else:
                    break
    except TypeError:
        print("Looks like that genre doesn't exist...\n")
        
    userImage = input("Would you like to see the cover image for one of the animes? ((anime number)/n): ")
    if(userImage == 'n'):
        return
    else:
        showImage(jsonText, int(userImage))
        return



def getRandomAnime():
    rand = True
    userNum = input("How many random anime recommendations do you want?: ")
    url = "https://api.aniapi.com/v1/random/anime/" + userNum
    resp = requests.get(url).text
    jsonText = json.loads(resp)
    printRecs(jsonText, rand, userNum)


if __name__ == "__main__":
    if auth() == 200:
        print("Authorization Complete\n")
    
    flag = True
    while(flag):
        print("Welcome to Anime Recommendations!\n")
        print("(1) Genre")
        print("(2) List genres")
        print("(3) Get random anime")
        print("(4) Exit\n\n")
        userInput = input("Choose an option above: ")
        time.sleep(0.8)
        if(userInput == '1'):
            jsonText = getJsonText()
            printRecs(jsonText, False, "10")
        elif(userInput == '2'):
            print(["Action","Adventure","Comedy","Drama","Ecchi","Fantasy","Horror","Mahou Shoujo","Mecha","Music","Mystery","Psychological","Romance","Sci-Fi","Slice Of Life","Sports","Supernatural","Thriller","Anti-Hero","Ensemble Cast","Female Protagonist","Male Protagonist","Office Lady","Primarily Adult Cast","Primarily Child Cast","Primarily Female Cast","Primarily Male Cast","Villainess","Age Regression","Agender","Aliens","Amnesia","Artificial Intelligence","Asexual","Butler","Centaur","Chimera","Chuunibyou","Cosplay","Crossdressing","Delinquents","Demons","Detective","Dinosaurs","Dissociative Identities","Dragons","Dullahan","Elf","Ghost","Goblin","Gods","Gyaru","Hikikomori","Idol","Kemonomimi","Kuudere","Maids","Mermaid","Monster Girl","Nekomimi","Ninja","Nudity","Nun","Oiran","Ojou-Sama","Pirates","Robots","Samurai","Shrine Maiden","Skeleton","Succubus","Tanned Skin","Teacher","Tsundere","Twins","Vampire","Vikings","Werewolf","Witch","Yandere","Zombie","Josei","Kids","Seinen","Shoujo","Shounen","Bar","Circus","College","Dungeon","Foreign","Language Barrier","Outdoor","Rural","School","School Club","Urban","Work","Achronological Order","Anachronism","Dystopian","Historical","Time Skip","Afterlife","Alternate Universe","Augmented Reality","Post-Apocalyptic","Space","Urban Fantasy","Virtual World","4-Koma","Achromatic","Advertisement","Anthology","CGI","Episodic","Flash","Full CGI","Full Color","No Dialogue","POV","Puppetry","Rotoscoping","Stop Motion","Archery","Battle Royale","Espionage","Fugitive","Guns","Martial Arts","Swordplay","Acting","Calligraphy","Classic Literature","Drawing","Fashion","Food","Photography","Rakugo","Writing","Band","Dancing","Musical","Parody","Satire","Slapstick","Surreal Comedy","Bullying","Coming Of Age","Conspiracy","Rehabilitation","Revenge","Tragedy","Body Swapping","Cultivation","Fairy Tale","Henshin","Isekai","Kaiju","Magic","Mythology","Shapeshifting","Steampunk","Super Power","Superhero","Wuxia","Youkai","Video Games","Card Battle","Go","Karuta","Mahjong","Poker","Shogi","Airsoft","American Football","Athletics","Badminton","Baseball","Basketball","Boxing","Cheerleading","Cycling","Fishing","Fitness","Football","Golf","Ice Skating","Lacrosse","Rugby","Scuba Diving","Skateboarding","Surfing","Swimming","Table Tennis","Tennis","Volleyball","Wrestling","Animals","Astronomy","Autobiographical","Biographical","Body Horror","Cannibalism","Chibi","Cosmic Horror","Crime","Crossover","Death Game","Denpa","Drugs","Economics","Educational","Environmental","Ero Guro","Gambling","Gender Bending","Gore","LGBTQ+ Themes","Lost Civilization","Medicine","Memory Manipulation","Meta","Noir","Otaku Culture","Pandemic","Philosophy","Politics","Reincarnation","Slavery","Software Development","Survival","Terrorism","War","Assassins","Cult","Firefighters","Gangs","Mafia","Military","Police","Triads","Yakuza","Aviation","Cars","Mopeds","Motorcycles","Ships","Tanks","Trains","Age Gap","Bisexual","Boys' Love","Harem","Love Triangle","Reverse Harem","Teens' Love","Yuri","Cyberpunk","Space Opera","Time Manipulation","Tokusatsu","Real Robot","Super Robot","Cute Girls Doing Cute Things","Family Life","Iyashikei"])
        elif(userInput == '3'):
            getRandomAnime()
        elif(userInput == '4'):
            flag = False
        
