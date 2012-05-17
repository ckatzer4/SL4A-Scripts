import android,os

droid = android.Android()

#print os.getcwd()

#print os.name

droid.dialogCreateAlert('Clear notes', None)
droid.dialogSetPositiveButtonText('Yes')
droid.dialogSetNegativeButtonText('No')
droid.dialogShow()
erase=droid.dialogGetResponse().result['which']=='positive'
if erase:
    schedule =open('schedule','w')
    schedule.close()

schedule=open('schedule','r')
L=schedule.readlines()
#print L

dialogue =""
for l in L:
    dialogue = dialogue + l
schedule.close()

droid.dialogCreateAlert("Notes", dialogue)
droid.dialogSetNeutralButtonText('Continue')
droid.dialogShow()
droid.dialogGetResponse()

droid.dialogCreateAlert('Append a new line?', None)
droid.dialogSetPositiveButtonText('Yes')
droid.dialogSetNegativeButtonText('No')
droid.dialogShow()
opening=droid.dialogGetResponse()
endcondition= opening.result['which']=='negative'

if endcondition:
    exit()
schedule=open('schedule','w')

appendstring=droid.dialogGetInput('Schedule', 'Line to add:', None)

print appendstring.result

for line in L:
    schedule.write(line)
schedule.write(appendstring.result+'\n')

schedule.close()