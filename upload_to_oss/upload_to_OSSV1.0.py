# -*- coding: utf-8 -*-

import os
import time
import datetime

import shutil
import oss2

DATETIME = time.strftime('%Y%m%d-%H%M%S')
BACKUPFILE = '/var/log/nginx/core.access.log.2.gz'

access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', '**')
access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', '**')
bucket_name = os.getenv('OSS_TEST_BUCKET', '**')
endpoint = os.getenv('OSS_TEST_ENDPOINT', 'http://oss-cn-hangzhou-internal.aliyuncs.com')

for param in (access_key_id, access_key_secret, bucket_name, endpoint):
    assert '<' not in param, '请设置参数：' + param

bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

bucket.put_object_from_file('img/'+'公司名/'+DATETIME,BACKUPFILE)
print "upload OSS success"
