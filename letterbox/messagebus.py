#!/usr/bin/env python3

import os
import sys
import time
import zmq
               
                                          
#  _______   
# |==   []| 
# |  ==== | *letterbox*
# '-------'   
#
# MessageBus - message passing between components
# written by John Lemme, 2019-2020 (jclemme at my dot uri dot edu)


class Bus:
    server = ""
    ctx = None
    sok_send = None
    sok_recv = None
    recv_hdlr = None
    
    def send(message:Message):
        socket.send(message.topic, zmq.SENDMORE)
        socket.send_pyobj(message.messagedata)
        
    def recv_subscriptions_set(subs):
        for sub in subs:
            self.sok_recv.setsockopt(zmq.SUBSCRIBE, bytes(sub))
        
    def recv_handler_set(handler):
        self.recv_hdlr = handler
        
    def recv_run():
    
class Message:
    type = b""
    data = {}
    
def connect(server):



def main_server():

    frontend = None
    backend = None
    context = None
    
    try:
        context = zmq.Context(1)
        # Socket facing clients
        frontend = context.socket(zmq.SUB)
        frontend.bind("tcp://*:5559")
        
        frontend.setsockopt(zmq.SUBSCRIBE, b"")
        
        # Socket facing services
        backend = context.socket(zmq.PUB)
        backend.bind("tcp://*:5560")

        zmq.device(zmq.FORWARDER, frontend, backend)
    except Exception as e:
        print(e)
        print("bringing down zmq device")
    finally:
        pass
        if frontend != None: frontend.close()
        if backend != None: backend.close()
        if context != None: context.term()

if __name__ == "__main__":
    main_server()
