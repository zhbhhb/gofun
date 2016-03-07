#!/bin/python
#coding:utf-8
#rabbitMQ介绍:http://blog.csdn.net/whycold/article/details/41119807

import sys
import amqp
import time
import threading
from threading import current_thread

conn = amqp.Connection(host="localhost:5672", userid="guest", password="guest", virtual_host="/", insist=False)
chan = conn.channel()
cnt = 1
tid = threading.current_thread().ident
while True:
    cnt += 1
    msg = amqp.Message('%s:%d:%s' % (tid, cnt, time.asctime(time.localtime(time.time()))))
    msg.properties['delivery_mode'] = 2
    #发送时指定exchange和routing_key
    chan.basic_publish(msg, exchange="sorting_room", routing_key="json")
    #time.sleep(1)

chan.close()
conn.close()
