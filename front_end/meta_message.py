push_meta_template = {
    "type": "push_meta",
    "manufacurer": "Sumsang",
    "manufacurer_model": "!!!",
    "os_name": "Android",
    "os_version": "10",
    "cpu": "4 Intel(R) Xeon(R) CPU E7-4850 v3 @ 2.20GHz",
    "cname": "live.wswebpic.com",
    "server_ip": "116.234.222.36:9900",
    "carrier": "46000",
    "connect_type": 1,
    "lng": 0,
    "lat": 0,
    # "lng": 123.42925,
    # "lat": 41.83571,
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
    "cname": "live.wswebpic.com",
    "server_ip": "116.234.222.36",
    "carrier": "46000",
    "connect_type": 1,
    "lng": 123.42925,
    "lat": 41.83571,
    # "begin_time": 1590741627629,
    "app_version": "V2.1",
    "pull_url": "rtmp://apppush.tingyun.com/live/666",
    "screen_width": 480,
    "screen_height": 720,
    "state": "OPEN",
}

def gen_push_meta_message():
    return push_meta_template.copy()


def gen_pull_meta_message():
    return pull_meta_template.copy()