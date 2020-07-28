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
    "fpt": 6000,
    "skt": 1000,
    "skc": 1,
    "nfs": 11111
}

def gen_push_metric_message():
    return push_metric_template.copy()


def gen_pull_metric_message():
    return pull_metric_template.copy()

