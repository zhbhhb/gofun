#!/usr/bin/python
#coding:utf-8
import amqp

conn = amqp.Connection(host="localhost:5672", userid="guest", password="guest", virtual_host="/", insist=False)
chan = conn.channel()
#1.声明queue
chan.queue_declare(queue="po_box", durable=True, exclusive=False, auto_delete=False)
#2.创建exchange，并指定type
chan.exchange_declare(exchange="sorting_room", type="direct", durable=True, auto_delete=False)
#3.绑定exchange和queue,并指定routing_key
chan.queue_bind(queue="po_box", exchange="sorting_room", routing_key="json")

def recv_callback(msg):
    print 'Received:' + msg.body + 'from channel#' + str(msg.channel.channel_id)
#4.从queue中取数据处理
chan.basic_consume(queue='po_box', no_ack=True, callback=recv_callback, consumer_tag="testtag")

while True:
    chan.wait()

chan.basic_cancel("testtag")
chan.close()
conn.close()

#http://www.oschina.net/p/rabbitmq
#rabbitMQ介绍:http://blog.csdn.net/whycold/article/details/41119807
#若type 为 direct 时：
#1. Producer将msg扔到exchange，并指定routing_key
#a. msg->exchange->routing_key的关系在Producer中指定
#2. exchange根据指定routing_key将msg扔到对应的queue中
#b. exchange->routing_key->queue->Consumer的关系在Consumer中指定
#3. Consumer从queue中取数据
