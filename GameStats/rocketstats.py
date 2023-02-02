from calendar import week
import datetime as DT
import requests

class Stats():

    def __init__(self, region, mode, tier):
        self.region = region
        self.mode = mode
        self.tier = tier
    
    def setplayerTag(self, playerTag):
        self.playerTag = playerTag

    def getPlayer(self, playerTag):
        params = {"country" : self.region, "tag" : playerTag}
        response = requests.get("https://zsr.octane.gg/players", params=params)
        playerId = 0
        for key in response.json()['players']:
            if(key['tag'] == playerTag):
                print("Found " + key['tag'])
                playerId = key['_id']
                break
        if(playerId == 0):
            print("Couldn't find " + playerTag)
        return playerId

    # Tourny ID
    def getIdofLatestTourny(self):
        today = DT.date.today()
        after = today - DT.timedelta(days=7)
        url = 'https://zsr.octane.gg/events'
        params = {"before" : str(today), "after" : after, "region" : self.region, "mode" : self.mode, "tier" : self.tier}
        response = requests.get(url, params=params)
        i = 10
        while(response.json()['events'] == []):
            after = today - DT.timedelta(days=7+i)
            params = {"before" : str(today), "after" : after, "region" : self.region, "mode" : self.mode, "tier" : self.tier}
            response = requests.get(url, params=params)
            i += 10
            if(i >= 1000):
                print("Couldn't find a tournament..")
                return 0
        for key in response.json()['events']:
            return key['_id'], key['name']
        

    def getTopPlayersFromTourny(self, numPlayers, criteria, criteria2):
        id, name = self.getIdofLatestTourny()
        url = 'https://zsr.octane.gg/matches'
        params = {"event" : id}
        players = {}
        response = requests.get(url, params=params)
        for firstKey in response.json()['matches']:
            try:
                numGames = len(firstKey['games'])
            except KeyError:
                if(firstKey['blue']['winner'] == True): # Handles DQ
                    numGames = firstKey['blue']['score']
                else:
                    numGames = firstKey['orange']['score']
            try:
                playersInBlueMatch = firstKey['blue']['players']
                playersInOrangeMatch = firstKey['orange']['players'] # Again, handles case when no key 'players'
            except KeyError:
                continue
            for secondKey in playersInBlueMatch:
                if(secondKey['player']['tag'] in players):
                    players[secondKey['player']['tag']] += (secondKey['stats'][criteria][criteria2])/numGames
                    players[secondKey['player']['tag']] /= 2
                else:
                    players[secondKey['player']['tag']] = (secondKey['stats'][criteria][criteria2])/numGames
            for secondKey in playersInOrangeMatch:
                if(secondKey['player']['tag'] in players):
                    players[secondKey['player']['tag']] += (secondKey['stats'][criteria][criteria2])/numGames
                    players[secondKey['player']['tag']] /= 2
                else:
                    players[secondKey['player']['tag']] = (secondKey['stats'][criteria][criteria2])/numGames

        sortedPlayers = dict(sorted(players.items(), key=lambda item: item[1], reverse=True)) # Sort dictionary
        sortedPlayers = list(sortedPlayers.items())[:int(numPlayers)] # Get top N results
        sortedPlayers = [''.join(str(tups)) for tups in sortedPlayers]
        sortedPlayers = ' '.join(sortedPlayers)
        print(name)
        return sortedPlayers
            
    def interfaceForTopPlayers(self):
        flag = True
        while(flag):
            howManyPlayers = input("List how many players?: ")
            criteria = input("core, boost, demo, movement or quit?: ")
            if criteria == 'quit':
                flag = False
                break
            if criteria == 'core':
                criteriaForStats = {1:'shots', 2:'goals', 3:'saves', 4:'assists', 5:'score', 6:'shootingPercentage'}
                print(criteriaForStats)
                index = input("Select which stat (1-N): ")
                criteria2 = criteriaForStats[int(index)]
                print(self.getTopPlayersFromTourny(howManyPlayers, criteria, criteria2))
            elif criteria == 'boost':
                criteriaForBoost = {1:'bpm', 2:'avgAmount', 3:'amountCollected', 4:'amountStolen', 5:'amountCollectedBig', 6:'amountStolenBig', 7:'amountCollectedSmall', 8:'amountStolenSmall', 9:'amountOverfill', 10:'amountUsedWhileSupersonic', 11:'timeZeroBoost', 12:'percentFullBoost'}
                print(criteriaForBoost)
                index = input("Select which stat (1-N): ")
                criteria2 = criteriaForBoost[int(index)]
                print(self.getTopPlayersFromTourny(howManyPlayers, criteria, criteria2))
            elif criteria == 'movement':
                criteriaForMovement = {1:'avgSpeed', 2:'totalDistance', 3:'timeSupersonicSpeed', 4:'timeSlowSpeed', 5:'timeGround', 6:'timeLowAir', 7:'timeHighAir', 8:'timePowerslide', 9:'avgPowerslideDuration'}
                print(criteriaForMovement)
                index = input("Select which stat (1-N): ")
                criteria2 = criteriaForMovement[int(index)]
                print(self.getTopPlayersFromTourny(howManyPlayers, criteria, criteria2))
            elif criteria == 'demo':
                criteria2 = input("inflicted or taken?: ")
                print(self.getTopPlayersFromTourny(howManyPlayers, criteria, criteria2))
            else:
                print("Unknown input..")

    # Practice function for writing out stats

    #def writeOutAllStatLeaders(self):
        # statFile = open('All Stat Leaders For Recent Tourny.txt', 'w')
        # id, name = self.getIdofLatestTourny()
        # statFile.write(name + "\n\n")
        # howManyPlayers = 10
        # criteria = ['core', 'boost', 'movement', 'demo']

        # print("At Core")
        # criteriaForStats = {1:'shots', 2:'goals', 3:'saves', 4:'assists', 5:'score', 6:'shootingPercentage'}
        # for criterionForStats in criteriaForStats.values():
        #     statFile.write("\n-----" + criterionForStats + "------\n\n")
        #     statFile.write(self.getTopPlayersFromTourny(howManyPlayers, criteria[0], criterionForStats) + "\n")

        # print("At Boost")
        # criteriaForBoost = {1:'bpm', 2:'avgAmount', 3:'amountCollected', 4:'amountStolen', 5:'amountCollectedBig', 6:'amountStolenBig', 7:'amountCollectedSmall', 8:'amountStolenSmall', 9:'amountOverfill', 10:'amountUsedWhileSupersonic', 11:'timeZeroBoost', 12:'percentFullBoost'}
        # for criterionForBoost in criteriaForBoost.values():
        #     statFile.write("\n-----" + criterionForBoost + "------\n\n")
        #     statFile.write(self.getTopPlayersFromTourny(howManyPlayers, criteria[1], criterionForBoost) + "\n")

        # print("At Movement")
        # criteriaForMovement = {1:'avgSpeed', 2:'totalDistance', 3:'timeSupersonicSpeed', 4:'timeSlowSpeed', 5:'timeGround', 6:'timeLowAir', 7:'timeHighAir', 8:'timePowerslide', 9:'avgPowerslideDuration'}
        # for criterionForMovement in criteriaForMovement.values():
        #     statFile.write("\n-----" + criterionForMovement + "------\n\n")
        #     statFile.write(self.getTopPlayersFromTourny(howManyPlayers, criteria[2], criterionForMovement) + "\n")

        # print("at Demo")
        # criteriaForDemo = {1: 'inflicted', 2: 'taken'}
        # for criterionForDemo in criteriaForDemo.values():
        #     statFile.write("\n-----" + criterionForDemo + "------\n\n")
        #     statFile.write(self.getTopPlayersFromTourny(howManyPlayers, criteria[3], criterionForDemo) + "\n")
        # statFile.close()
        # print("Finished")
        # return 0
    

    def getStatsToWriteOut(self, criteria, criteria2, players, index, id, criteriaHasChanged):
        url = 'https://zsr.octane.gg/matches'
        params = {"event" : id}

        response = requests.get(url, params=params)
        for firstKey in response.json()['matches']:
            try:
                numGames = len(firstKey['games'])
            except KeyError:
                if(firstKey['blue']['winner'] == True): # Handles DQ
                    numGames = firstKey['blue']['score']
                else:
                    numGames = firstKey['orange']['score']
            try:
                playersInBlueMatch = firstKey['blue']['players']
                playersInOrangeMatch = firstKey['orange']['players'] # Again, handles case when no key 'players'
            except KeyError:
                continue
            for secondKey in playersInBlueMatch:
                if(secondKey['player']['tag'] in players):
                    if(criteriaHasChanged):
                        players[secondKey['player']['tag']].append(0)
                    players[secondKey['player']['tag']][index] += (secondKey['stats'][criteria][criteria2])/numGames
                    players[secondKey['player']['tag']][index] /= 2
                else:
                    players[secondKey['player']['tag']] = [(secondKey['stats'][criteria][criteria2])/numGames]

            for secondKey in playersInOrangeMatch:
                if(secondKey['player']['tag'] in players):
                    players[secondKey['player']['tag']][index] += (secondKey['stats'][criteria][criteria2])/numGames
                    players[secondKey['player']['tag']][index] /= 2
                else:
                    players[secondKey['player']['tag']] = [(secondKey['stats'][criteria][criteria2])/numGames]
        return players


    def writeOutAllStats(self):
        players = {}
        statFile = open('totalStats.txt', 'w')
        id, name = self.getIdofLatestTourny()
        statFile.write(name + "\n\n")
        criteria = ['core', 'boost', 'movement', 'demo']
        index = -1
        criteriaHasChanged = False

        print("At Core")
        criteriaForStats = {1:'shots', 2:'goals', 3:'saves', 4:'assists', 5:'score', 6:'shootingPercentage'}
        for criterionForStats in criteriaForStats.values():
            index += 1
            statFile.write("\n-----" + criterionForStats + "------\n\n")
            players = self.getStatsToWriteOut(criteria[0], criterionForStats, players, index, id, criteriaHasChanged)
            criteriaHasChanged = True


if __name__ == '__main__':
    # tag = "Daniel"
    # getAvgScorePerPlayer(region, tag)
    region = input("What region?: ")
    mode = input("What mode? (1-3): ")
    tier = input("What tier? (B-S): ")
    rocketStats = Stats(region, mode, tier)
    #rocketStats.interfaceForTopPlayers() # To get top N number of players and their stats.
    #rocketStats.writeOutAllStats() # Work in progress method.
