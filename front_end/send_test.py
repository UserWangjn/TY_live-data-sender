import unittest
from front_end import util, event_message as event, meta_message as meta, metric_message as metric, common_message as common

live_frontend_url = 'http://10.128.1.96:9111/live'
# 本地测试
# live_frontend_url = 'http://127.0.0.1:9111/live'
headers = {'Content-Type': 'text/plain'}

class LiveFrontTestCase(unittest.TestCase):
    def test_push_message(self):
        data = util.trans_line_data([
            common.gen_push_common(),
            meta.gen_push_meta_message(),
            metric.gen_push_metric_message(),
            event.gen_push_ping_event(),
            event.gen_push_traceroute_event()
        ])
        print(data)
        util.send_request(live_frontend_url, headers, data)


if __name__ == '__main__':
    unittest.main()
