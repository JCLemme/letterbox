#!/usr/bin/env python3

import os
import sys
import time
import zmq

def main():

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
    main()
