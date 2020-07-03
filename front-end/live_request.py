import requests
from json import dumps
import time

live_frontend_url = 'http://10.128.1.96:9111/live'
headers = {'Content-Type': 'text/plain'}
common_template = {
    "type": "common",
    "key": "p35OnrDoP8k",
    "t": 1590567933155,
    "did": "9a6ade06-9904-44e2-a57d-ae532d555932",
    "sid": "9a6ade06-9904-44e2-a57d-ae532d555932",
    "sn": "666",
    "agent_version": "1.0.0",
    "agent_name": "中文",
    "uid": "user1"
}

push_meta_template = {
    "type": "push_meta",
    "manufacurer": "Sumsang",
    "manufacurer_model": "?",
    "os_name": "Android",
    "os_version": "10",
    "cpu": "4 Intel(R) Xeon(R) CPU E7-4850 v3 @ 2.20GHz",
    "cname": "live.example.com",
    "server_ip": "10.1.1.1",
    "carrier": "46000",
    "connect_type": "WIFI",
    "lng": "123.42925",
    "lat": "41.83571",
    # "begin_time": 1590741627629,
    "app_version": "V1.1",

    "push_url": "rtmp://apppush.tingyun.com/live/666",
    "state": "OPEN",
}

pull_meta_template = {
    "type": "pull_meta",
    "manufacurer": "Sumsang",
    "manufacurer_model": "?",
    "os_name": "Android",
    "os_version": "10",
    "cpu": "4 Intel(R) Xeon(R) CPU E7-4850 v3 @ 2.20GHz",
    "cname": "live.example.com",
    "server_ip": "10.1.1.1",
    "carrier": "46000",
    "connect_type": "WIFI",
    "lng": "123.42925",
    "lat": "41.83571",
    # "begin_time": 1590741627629,
    "app_version": "V2.1",
    "pull_url": "rtmp://apppush.tingyun.com/live/666",
    "screen_width": 480,
    "screen_height": 720,
    "state": "OPEN",
}

push_metric_template = {
    "type": "push_metric",
    "vfr": 30,
    "vbr": 12900,
    "abr": 320,
    "usp": 1000,
    "vol": 50,
    "skt": 1000,
    "skc": 1,
    "csu": 10,
    "cau": 1,
    "lvt": 60000
}

pull_metric_template = {
    "type": "pull_metric",
    "dsp": 1000,
    "vfr": 30,
    "vbr": 12900,
    "plt": 60000,
    "csu": 10,
    "cau": 1,
    "fpt": 2000,
    "skt": 1000,
    "skc": 1,
    "nfs": 11111
}

def get_timestamp():
    return int(round(time.time() * 1000))

def stringify(data):
    return dumps(data, ensure_ascii=False)

def send_request(data):
    requests.post(live_frontend_url, data.encode('utf-8'), headers=headers)

def send_pull_metric():
    common = common_template.copy()
    common['t'] = get_timestamp()
    lines = [common,
            pull_meta_template.copy(),
            pull_metric_template.copy()]

    data = list(map(lambda l: stringify(l), lines))
    data = '\n'.join(data)
    send_request(data)

def send_push_metric():
    common = common_template.copy()
    common['t'] = get_timestamp()
    lines = [common,
             push_meta_template.copy(),
             push_metric_template.copy()]

    data = list(map(lambda l: stringify(l), lines))
    data = '\n'.join(data)
    send_request(data)


if __name__ == '__main__':

    send_pull_metric()

    # send_push_metric()