import android
import urllib2

droid = android.Android()

f = urllib2.urlopen("http://www.eos.ncsu.edu/labs/generate-availability-table.php?ajax_refresh")
S = f.read()
for sub in S.split("<tr "):
	if "DHL" in sub:
		targetsub = sub
for subsub in targetsub.split("<td "):
	if "lin" in subsub:
		linsub = subsub
compys = int(linsub.split("<span>")[1][0])

use_plural =  compys!=1

if use_plural:
	droid.notify('Red Hat Compys' , "There are "+str(compys)+" Red Hat Compys available.")
else:
	droid.notify('Red Hat Compys' , "There is "+str(compys)+" Red Hat Compy available.")