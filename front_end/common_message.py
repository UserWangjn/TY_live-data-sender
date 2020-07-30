from front_end import util

common_template = {
    "type": "common",
    "key": "p35OnrDoP8k",
    "t": 1590567933155,
    "did": "9a6ade06-9904-44e2-a57d-ae532d555932",
    # "sid": "9a6ade06-9904-44e2-a57d-ae532d555932",
    "sn": "666",
    "agent_version": "1.0.0",
    "agent_name": "Android",
    "uid": "user1"
}

def gen_common(type, on_demand = False):
    data = common_template.copy()
    data['type'] = type + '_' + data['type']
    # 点播删除sn
    if on_demand:
        del data['sn']
    data['sid'] = util.gen_uuid()
    data['t'] = util.gen_timestamp()
    return data

def gen_push_common():
    return gen_common('push')

def gen_pull_common(on_demmand = False):
    return gen_common('pull', on_demmand)


if __name__ == '__main__':
    print(gen_pull_common(True))