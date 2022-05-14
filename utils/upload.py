#encoding:utf-8
import oss2
import os, sys
from datetime import datetime
import config
auth = oss2.Auth(config.ALIYUN_OSS_ID,config.ALIYUN_OSS_SECRET)

bucket = oss2.Bucket(auth,'oss-cn-hangzhou.aliyuncs.com','flask-cms')


# 地址前缀
url_pre = config.URL_PREFIX #ECS 的经典网络访问（内网）

base_posts_url = url_pre+'posts/'
base_avater_url = url_pre+'avater/'
base_groups_url = url_pre+'groups/'
base_images_url = url_pre+'images/'
base_resources_url = url_pre+'resources/'

bucket_post = oss2.Bucket(auth,'oss-cn-hangzhou.aliyuncs.com','flask-cms')




def change_filename(filename):
    dt = datetime.now()
    time = dt.strftime('%Y%m%d%H%M%S')
    filename = time+filename
    return filename


def percentage(consumed_bytes, total_bytes):
    if total_bytes:
        rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
        print('\r{0}% '.format(rate), end='')
        sys.stdout.flush()






