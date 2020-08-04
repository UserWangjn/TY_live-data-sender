import unittest
from front_end import util, event_message as event, meta_message as meta, metric_message as metric, \
    common_message as common
from apscheduler.schedulers.blocking import BlockingScheduler

live_frontend_url = 'http://10.128.1.96:9111/live'
# 本地测试
# live_frontend_url = 'http://127.0.0.1:9111/live'

headers = {'Content-Type': 'application/json'}


class LiveFrontTestCase(unittest.TestCase):
    def test_push(self):
        '''
        单次 push, 开始推流消息
        :return:
        '''
        data = util.stringify([
            common.gen_push_common(),
            meta.gen_push_meta_message(),
            metric.gen_push_metric_message(),
            event.gen_push_ping_event(),
            event.gen_push_traceroute_event()
        ])
        print(data)
        util.send_request(live_frontend_url, headers, data)

    def test_push_stream(self):
        '''
        多次push测试, 首先发送初始消息, 之后每5秒发送一次指标数据, 随机发送event数据，持续发送
        '''
        self.test_push()

        def send_push_metric():
            print('sending push metric...', util.datetime_toString())
            metric_data = util.stringify([
                common.gen_push_common(),
                metric.gen_push_metric_message()
            ])
            util.send_request(live_frontend_url, headers, metric_data)

        scheduler = BlockingScheduler()
        scheduler.add_job(send_push_metric, 'interval', seconds=5, id='push_metric_job')
        scheduler.start()

    def test_push_custom_event(self):
        '''
        测试发送自定义事件
        :return:
        '''
        data = util.stringify([
            common.gen_push_common(),
            meta.gen_push_meta_message(),
            event.gen_push_custom_event()
        ])
        print(data)
        util.send_request(live_frontend_url, headers, data)

    def test_pull(self, on_demand=False):
        '''
        单次pull 开始拉流消息
        :return:
        '''
        data = util.stringify([
            common.gen_pull_common(on_demand),
            meta.gen_pull_meta_message(),
            metric.gen_pull_metric_message(),
            event.gen_pull_ping_event(),
            event.gen_pull_traceroute_event()
        ])
        print(data)
        util.send_request(live_frontend_url, headers, data)

    def test_pull_stream(self, on_demand=False):
        '''
        多次pull测试, 首先发送初始消息, 之后每5秒发送一次指标数据, 随机发送event数据，持续发送
        '''
        self.test_pull(on_demand)

        def send_pull_metric():
            print('sending pull metric...', util.datetime_toString())
            metric_data = util.stringify([
                common.gen_pull_common(on_demand),
                metric.gen_pull_metric_message()
            ])
            util.send_request(live_frontend_url, headers, metric_data)

        scheduler = BlockingScheduler()
        scheduler.add_job(send_pull_metric, 'interval', seconds=5, id='pull_metric_job')
        scheduler.start()

    def test_pull_on_demand(self):
        '''
        单次点播
        :return:
        '''
        self.test_pull(True)

    def test_pull_stream_on_demand(self):
        '''
        点播流
        :return:
        '''
        self.test_pull_stream(True)

if __name__ == '__main__':
    unittest.main()
