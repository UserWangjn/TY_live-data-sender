from kafka import KafkaConsumer
from json import loads
import time

consumer = KafkaConsumer(
    'drd-live-pull',
    # 'live-access-log',
    bootstrap_servers='10.128.1.139:9092',
                         security_protocol='SASL_PLAINTEXT',
                         sasl_mechanism='PLAIN',
                         sasl_plain_username='tingyun',
                         sasl_plain_password='nEtben@2_19',
                         group_id='local_test',
                         value_deserializer=lambda x: x.decode('utf-8'),
                         enable_auto_commit = True
                         )

for message in consumer:
    message = message.value
    print(message)