import sys
import zmq
import random
import time

port = "5560"
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
print "Collecting updates from server..."
socket.connect ("tcp://localhost:%s" % port)

ssocket = context.socket(zmq.PUB)
ssocket.connect("tcp://localhost:%s" % "5559")
    
topicfilter = str(random.randrange(1, 10))
print topicfilter

socket.setsockopt(zmq.SUBSCRIBE, topicfilter)
for update_nbr in range(10):
    string = socket.recv()
    topic, messagedata = string.split()
    print topic, messagedata

    if topicfilter != "1":
        ssocket.send("%d %s" % (1, "beepbeep"))
    
    time.sleep(1)

