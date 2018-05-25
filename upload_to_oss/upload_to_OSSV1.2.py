# -*- coding: utf-8 -*-
'''
使用阿里云提供的python SDK将文件批量上传到阿里云OSS
使用前需要先安装阿里云SDK OSS2
'''
import os
import time
import datetime

import shutil
import oss2

# 输入要上传文件的源文件夹和OSS上的目标文件夹
SRCPATH = input('请输入需要上传的文件目录（eg: /data/1/2/）：')
OSSPATH = input('请输入OSS上的保存目录 (eg: img/1/2/):')

# 遍历源文件夹下的所有文件
FILENAMES = os.listdir(SRCPATH)
for filename in FILENAMES :   #将遍历到的文件名循环赋值

	BACKUPFILE = filename
	OSSFILE	= filename
# 通关环境变量获取OSS相关参数
	access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', '**')
	access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', '**')
	bucket_name = os.getenv('OSS_TEST_BUCKET', 'bak-data')
	endpoint = os.getenv('OSS_TEST_ENDPOINT', 'http://oss-cn-hangzhou-internal.aliyuncs.com')
# 确认上面的OSS参数填写正确
	for param in (access_key_id, access_key_secret, bucket_name, endpoint):
    	assert '<' not in param, '请设置参数：' + param
# 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
	bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)
	bucket.put_object_from_file(OSSPATH + OSSFILE ,SRCPATH + BACKUPFILE)
print "upload OSS success"
