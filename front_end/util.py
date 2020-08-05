import time
import requests
import uuid
from json import dumps
import datetime

# 获取当前时间戳
def gen_timestamp():
    return int(round(time.time() * 1000))

def send_request(url, headers, data):
    return requests.post(url, data.encode('utf-8'), headers=headers)

def gen_uuid():
    return str(uuid.uuid1())

def stringify(data):
    return dumps(data, ensure_ascii=False)

def trans_line_data(lines):
    '''
    组装发送的数据格式
    :param lines:
    :return:
    '''
    data = []
    for line in lines:
        prefix = line['type']
        if 'event_type' in line:
            prefix += ('_' + line['event_type'])
        data.append(prefix + stringify(line))
    data = '\n'.join(data)
    return data

def datetime_toString():
    dt = datetime.datetime.now()
    return dt.strftime("%Y-%m-%d %H:%M:%S")