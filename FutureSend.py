import android
import time

droid = android.Android()

print time.strftime("%_I %M %p on %A, %B %_e, %Y ")

droid.dialogCreateDatePicker(int(time.strftime('%Y')), int(time.strftime('%m')), int(time.strftime('%d')))
droid.dialogShow()
date = droid.dialogGetResponse()
print date
droid.dialogCreateTimePicker(0, 0, False)
droid.dialogShow()
minhour = droid.dialogGetResponse()
#print date
#print minhour
tyear = date.result['year']
tmonth = date.result['month']
tday = date.result['day']
thour = minhour.result['hour']
tminute = minhour.result['minute']

smstext = droid.dialogGetInput('SMS', 'Please enter message:', None).result
receiver = droid.dialogGetInput('Receiver', ' Who will get the message:', None).result

#print receiver
#print smstext

#cyear = time.strftime("%Y")
#cmonth = time.strftime("%m")
#cday = time.strftime("%d")
#chour = time.strftime("%H")
#cminute = time.strftime("%M")
#if cmonth[0] == "0":
#	cmonth = cmonth[1]
#if cday[0] == "0":
#	cday = cday[1]
#if chour[0] == "0":
#	chour = chour[1]
#if cminute[0] == "0":
#	cminute = cminute[1]



def futuresend():
	cyear = time.strftime("%Y")
	while int(cyear) < tyear:
		time.sleep(60)
		cyear = time.strftime('%Y')
	cmonth = time.strftime("%m")
	while int(cmonth) < tmonth:
		time.sleep(60)
		cmonth = time.strftime('%m')
		if cmonth[0] == "0":
			cmonth = cmonth[1]
	cday = time.strftime("%d")
	while int(cday) < tday:
		time.sleep(60)
		cday =time.strftime("%d")
		if cday[0] == "0":
			cday = cday[1]
		print cday, tday
	chour = time.strftime("%H")
	while int(chour) < thour:
		time.sleep(60)
		chour = time.strftime("%H")
		if chour[0] == "0":
			chour = chour[1]
		print chour, thour
	cminute = time.strftime("%M")
	while int(cminute) < tminute:
		time.sleep(30)
		cminute = time.strftime("%M")
		if cminute[0] == "0":
			cminute = cminute[1]
		print cminute, tminute

	print("Sending message.")
	droid.smsSend(str(receiver), str(smstext))
	print ("Successful.")

futuresend()