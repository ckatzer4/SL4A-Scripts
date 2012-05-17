import android
import urllib2

droid = android.Android()

compytypes = [
    "lin",
    "win"
]

locations = [
    "DAN 226",
    "EB2",
    "EB3",
    "DHL",
    "MRC 300"
]

def gettype():
    droid.dialogCreateAlert('Location', None)
    droid.dialogSetNegativeButtonText('Cancel')
    droid.dialogSetPositiveButtonText('Continue')
    droid.dialogSetSingleChoiceItems(compytypes, 0)
    droid.dialogShow()
    event = droid.eventWaitFor('dialog', None)
    compresult = droid.dialogGetSelectedItems()
    compindex = compresult.result[0]
    return compytypes[compindex]

def getlocation():
    droid.dialogCreateAlert('Location', None)
    droid.dialogSetNegativeButtonText('Cancel')
    droid.dialogSetPositiveButtonText('Continue')
    droid.dialogSetSingleChoiceItems(locations, 0)
    droid.dialogShow()
    event = droid.eventWaitFor('dialog', None)
    locationresult = droid.dialogGetSelectedItems()
    locindex = locationresult.result[0]
    return locations[locindex]

def grabsauce():
    f = urllib2.urlopen("http://www.eos.ncsu.edu/labs/generate-availability-table.php?ajax_refresh")
    S = f.read()
    return S

def findnumber(typestring,locationstring,S):
    for sub in S.split("<tr "):
    	if locationstring in sub:
    		targetsub = sub
    for subsub in targetsub.split("<td "):
    	if typestring in subsub:
    		linsub = subsub
    compyline = linsub.split("<span>")[1]
    compys = int(compyline[0:compyline.index('<')])
    return compys

def notify(compysstring):
    use_plural =  compysstring!=1
    if use_plural:
    	droid.notify('Compys Available' , "There are "+str(compysstring)+" Compys available.")
    else:
    	droid.notify('Compys Available' , "There is "+str(compysstring)+" Compy available.")

ctype = gettype()
location = getlocation()
sauce = grabsauce()
comps = findnumber(ctype,location,sauce)
notify(comps)