import uuid
from front_end import util

common_template = {
    "type": "common",
    "key": "p35OnrDoP8k",
    "t": 1590567933155,
    "did": "9a6ade06-9904-44e2-a57d-ae532d555932?1",
    # "sid": "9a6ade06-9904-44e2-a57d-ae532d555932",
    "sn": "666",
    "agent_version": "1.0.0",
    "agent_name": "Android",
    "uid": "xxx"
}

def gen_common(type):
    data = common_template.copy()
    data['type'] = type + '_' + data['type']
    data['sid'] = util.gen_uuid()
    data['t'] = util.gen_timestamp()
    return data

def gen_push_common():
    return gen_common('push')

def gen_pull_common():
    return gen_common('pull')

