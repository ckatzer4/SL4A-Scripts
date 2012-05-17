import android
import time

droid = android.Android()

droid.dialogGetInput('Phone Number', 'Phone number of poor recipient:', None)

phonenumber = droid.dialogGetResponse().result['value']

droid.dialogGetInput('Content', 'What should the message say?', None)

messagestring = droid.dialogGetResponse().result['value']

droid.dialogGetInput('Messages', 'Send how many times?', None)

timesnum = int(droid.dialogGetResponse().result['value'])

print phonenumber, messagestring, timesnum

for i in range(timesnum):
    droid.smsSend(phonenumber, messagestring)
    print 'Sent message', i
    time.sleep(2)