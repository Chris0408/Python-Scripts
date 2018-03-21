# -*- coding: utf-8 -*-

import os
import time
import datetime

import shutil
import oss2
loopnum = input('请输入上传次数：')
SOURCEPTAH = input('请输入需要上传的文件目录（eg: /data/1/2/）：')
OSSPATH = input('请输入OSS上的保存目录 (eg: img/1/2/):')
int(loopnum)
i = loopnum
while i > 0:
	i = i-1
	BACKUPFILE = input('请输入要上传文件的文件名：') 
	OSSFILE	= input('请输入保存在OSS中的文件名： ')
	#DATETIME = time.strftime('%Y%m%d-%H%M%S')

	access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', '**')
	access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', '**')
	bucket_name = os.getenv('OSS_TEST_BUCKET', '**')
	endpoint = os.getenv('OSS_TEST_ENDPOINT', 'http://oss-cn-hangzhou-internal.aliyuncs.com')

	for param in (access_key_id, access_key_secret, bucket_name, endpoint):
    	assert '<' not in param, '请设置参数：' + param

	bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

	bucket.put_object_from_file(OSSPATH + OSSFILE ,SOURCEPATH + BACKUPFILE)
print "upload OSS success"
