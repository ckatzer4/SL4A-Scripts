#A simple score keeper for any number of players
#Written in Python by Charles Katzer

#Standard setup:

import android

droid = android.Android()


#Get number of players and setup empty lists:

droid.dialogGetInput('Players', 'How many players?', None)
numberofplayers = int(droid.dialogGetResponse().result['value'])
players = []
names=[]


#Get player names and fill lists:

for i in range(numberofplayers):
    droid.dialogGetInput('Name', 'Name of player '+str(i+1)+':', None)
    player=droid.dialogGetResponse().result['value']
    players.append([])
    players[i].append(str(player))
    players[i].append(0) #Starting score is 0
    names.append(str(player))

#My trouble shooting:
#print players
#print names


#Endless Score Loop:

nextturn = True #Boolean deciding turn rotation
while nextturn:
    #Total up scores
    for name in names:
        droid.dialogGetInput('Score Change', 'Score change for '+name+':', None)
        score =int(droid.dialogGetResponse().result['value'])
        players[names.index(name)][1]=players[names.index(name)][1]+score
    
    #Display current scores
    dialog=''
    for player in players:
        dialog = dialog + player[0] +':  '+str(player[1])+'\n'
    droid.dialogCreateAlert('Scores', dialog)
    droid.dialogSetNeutralButtonText('Continue')
    droid.dialogShow()
    droid.dialogGetResponse()
    
    #Ask for another turn rotation
    droid.dialogCreateAlert('Another turn?', None)
    droid.dialogSetPositiveButtonText('Yes')
    droid.dialogSetNegativeButtonText('No')
    droid.dialogShow()
    nextturn = droid.dialogGetResponse().result['which'] == 'positive'


#Display Final Score:

dialog = ''
for player in players:
    dialog = dialog + player[0] +':  '+str(player[1])+'\n'
droid.dialogCreateAlert('Final Scores', dialog)
droid.dialogSetNeutralButtonText('Finish')
droid.dialogShow()
droid.dialogGetResponse()