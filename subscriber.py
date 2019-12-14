import zmq
import random
import sys
import time
import asyncio

import letterbox.messagebus

count = 0

def received(bus, msg, args):
    print(msg.topic)
    
    global count
    count += 1
    if(count <= 10):
        bus.on_recv(received)

def main():
    bus = letterbox.messagebus.Bus("localhost")
    bus.subscribe(["test"])
    
    bus.on_recv(received)

main()
asyncio.get_event_loop().run_forever()
