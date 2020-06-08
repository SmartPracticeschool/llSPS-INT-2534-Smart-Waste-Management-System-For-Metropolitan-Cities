import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
#Provide your IBM Watson Device Credentials
organization = "1o823s"
deviceType = "raspberrypi"
deviceId = "123456"
authMethod = "token"
authToken = "123456789"

# Initialize GPIO

def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)
        print(type(cmd.data))
        i=cmd.data['command']
        if i=='lighton':
                print("light is on")
        elif i=='lightoff':
                print("light is off")

try:
        deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
        deviceCli = ibmiotf.device.Client(deviceOptions)#.............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        
        hit=random.randint(10,20)
        #print(hum)
        gbe=random.randint(10,50)
        #Send garbage & height to IBM Watson
        data = { 'garbage' : gbe, 'height': hit }
        #print (data)
        def myOnPublishCallback():
            print ("Published garbage = %s C" % gbe, "height= %s %%" % hit, "to IBM Watson")

        success = deviceCli.publishEvent("garbage", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(2)
        
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
