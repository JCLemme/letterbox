import zmq
import random
import sys
import time

import letterbox.messagebus

bus = letterbox.messagebus.Bus("localhost")

while(True):
    bus.send(letterbox.messagebus.Message(topic=b"test", data={"message": random.randrange(0, 10)}))
    time.sleep(1)
    
bus.close()
