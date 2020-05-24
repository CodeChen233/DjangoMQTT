# __author: gy-chen
# data: 2020/5/23
# -*- coding: UTF-8 -*-


# 为了能在外部脚本中调用Django ORM模型，必须配置脚本环境变量，将脚本注册到Django的环境变量中
import os, sys
import django
# 第一个参数固定，第二个参数是工程名称.settings
os.environ.setdefault('DJANGO_SETTING_MODULE', 'backend.settings')
django.setup()

# 引入mqtt包
import paho.mqtt.client as mqtt
# 使用独立线程运行
from threading import Thread
# from app名 import models
from backend import models    # import models可以操作数据

import time
import json


# 建立mqtt连接
def on_connect(client, userdata, flag, rc):
    print("Connect with the result code " + str(rc))
    client.subscribe('data/receive', qos=0)


# 接收、处理mqtt消息
def on_message(client, userdata, msg):
    out = msg.payload.decode('utf-8')
    # print("topic:"+msg.topic)
    # print(out)  # string类型
    # out = json.loads(out)

    # 收到消息后执行任务
    if msg.topic == 'data/receive':

        # 处理model层业务
        # 增
        # obj = models.MqttData(topic=msg.topic, msg=out)
        # obj.save()
        # print("==>" + out)
        # 查
        # data = models.MqttData.objects.all()
        # print(data)
        # 改
        models.MqttData.objects.filter(topic=msg.topic).update(msg=out)


# mqtt客户端启动函数
def mqttfunction():
    global client
    # 使用loop_start 可以避免阻塞Django进程，使用loop_forever()可能会阻塞系统进程
    # client.loop_start()
    # client.loop_forever() 有掉线重连功能
    client.loop_forever(retry_first_connection=True)


client = mqtt.Client(client_id="test", clean_session=False)


# 启动函数
def mqtt_run():
    client.on_connect = on_connect
    client.on_message = on_message
    # 绑定 MQTT 服务器地址
    broker = '120.79.57.0'
    # MQTT服务器的端口号
    client.connect(broker, 1883, 4000)
    client.username_pw_set('admin', 'admin')
    client.reconnect_delay_set(min_delay=1, max_delay=2000)
    # 启动
    mqttthread = Thread(target=mqttfunction)
    mqttthread.start()


# 启动 MQTT
# mqtt_run()


if __name__ == "__main__":
    mqtt_run()











