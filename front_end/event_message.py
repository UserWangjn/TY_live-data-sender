import copy
import front_end.util as common_util

traceroute_template = {
    "type": "event",

    "event_type": "traceroute",
    "name": "traceroute",
    "msg": "traceroute",
    "time": 1590567933155,
    "properties": {
        "target": "182.61.200.6",
        "data": [
            ' 1     1 ms     1 ms     4 ms  192.168.5.1',
            ' 2    <1 毫秒   <1 毫秒   <1 毫秒 192.168.100.252',
            ' 3    <1 毫秒   <1 毫秒   <1 毫秒 192.168.100.252'
        ]
    }
}

ping_template = {
    "type": "event",

    "event_type": "ping",
    "name": "ping",
    "msg": "ping",
    "time": 1590567933155,
    "properties": {
        "sent": 2,
        "lost": 1,
        "rec": 2,
        "min": 6,
        "max": 6,
        "avg": 6,
        "target": "www.qq.com",
        "ip": "113.96.232.215",
        "data": [
            {
                "byte": 32,
                "time": 6,
                "ttl": 45
            }
        ]
    }
}


custom_template = {
    "type": "event",

    "event_type": "custom",
    "name": "fail_test",
    "msg": "A fail event",
    "time": 1590567933155,
    "properties": {
    }
}

def gen_ping_event(type):
    data = copy.deepcopy(ping_template)
    data['type'] = type + '_' + data['type']
    data['time'] = common_util.gen_timestamp()
    return data

def gen_traceroute_event(type):
    data = copy.deepcopy(traceroute_template)
    data['type'] = type + '_' + data['type']
    data['time'] = common_util.gen_timestamp()
    return data

def gen_push_ping_event():
    return gen_ping_event('push')

def gen_pull_ping_event():
    return gen_ping_event('pull')

def gen_push_traceroute_event():
    return gen_traceroute_event('push')

def gen_pull_traceroute_event():
    return gen_traceroute_event('pull')


def gen_push_custom_event():
    '''
    生成自定义事件
    :return:
    '''
    data = copy.deepcopy(custom_template)
    data['type'] = 'push_' + data['type']
    data['time'] = common_util.gen_timestamp()
    return data