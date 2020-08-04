import time
import requests
import uuid
from json import dumps
import datetime

# 获取当前时间戳
def gen_timestamp():
    return int(round(time.time() * 1000))

def send_request(url, headers, data):
    requests.post(url, data.encode('utf-8'), headers=headers)

def gen_uuid():
    return str(uuid.uuid1())

def stringify(data):
    return dumps(data, ensure_ascii=False)

# 将多条消息转行分分行的字符串
def trans_line_data(lines):
    data = list(map(lambda l: stringify(l), lines))
    return data

def datetime_toString():
    dt = datetime.datetime.now()
    return dt.strftime("%Y-%m-%d %H:%M:%S")