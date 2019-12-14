#!/usr/bin/env python3

import os
import sys
import time
import asyncio
import zmq
import zmq.asyncio

                                          
#  _______   
# |==   []| 
# |  ==== | *letterbox*
# '-------'   
#
# messagebus - message passing between components
# written by John Lemme, 2019-2020 (jclemme at my dot uri dot edu)

        
class Message:
    topic = b""
    data = {}
    
    def __init__(self, topic=b"", data={}):
        self.topic = topic
        self.data = data
    
class Bus:
    server = ""
    ctx = None
    sok_send = None
    sok_recv = None
    recv_callback = None
    
    def __init__(self, server):
        # Async IO zMQ functions
        self.ctx = zmq.asyncio.Context.instance()
        
        self.sok_send = self.ctx.socket(zmq.PUB)
        self.sok_send.connect("tcp://" + server + ":20550")
        
        self.sok_recv = self.ctx.socket(zmq.SUB)
        self.sok_recv.connect("tcp://" + server + ":20551")
        
    def send(self, message:Message):
        self.sok_send.send(message.topic, zmq.SNDMORE)
        self.sok_send.send_pyobj(message.data)
        
    def subscribe(self, subs):
        for sub in subs:
            self.sok_recv.subscribe(sub)

    def unsubscribe(self, subs):
        for sub in subs:
            self.sok_recv.unsubscribe(sub)
            
    async def recv(self, handler=None, kwargs={}):
        message = await self.sok_recv.recv_multipart()
        message = Message(topic=message[0], data=message[1])
        
        if(handler == None): return message
        else: handler(self, message, kwargs)
        
    def on_recv(self, handler, optargs={}):
        asyncio.get_event_loop().create_task(self.recv(handler=handler, kwargs=optargs))
        
    def close():
        self.sok_send.close()
        self.sok_recv.close()
        self.ctx.term()
        
        
def server():

    sok_send = None
    sok_recv = None
    ctx = None
    error = None
    
    try:
        ctx = zmq.Context()

        sok_recv = ctx.socket(zmq.SUB)
        sok_recv.bind("tcp://*:20550")
        sok_recv.subscribe(b"")
        
        sok_send = ctx.socket(zmq.PUB)
        sok_send.bind("tcp://*:20551")

        zmq.device(zmq.FORWARDER, sok_send, sok_recv)
    except Exception as e:
        error = e
        print(e)
    finally:
        pass
        if sok_send != None: sok_send.close()
        if sok_recv != None: sok_recv.close()
        if ctx != None: ctx.term()

    return error
    
if __name__ == "__main__":
    server()
