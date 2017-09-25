# -*- coding: utf-8 -*-
from flask import current_app
from qiniu import Auth, put_file, BucketManager, etag, urlsafe_base64_encode



def upload_qiniu(pic_url,name):
    # 需要填写你的 Access Key 和 Secret Key
    access_key = current_app.config['QINIU_ACCESS_KEY']
    secret_key = current_app.config['QIUNU_SECRETE_KEY']
    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    # 要上传的空间
    bucket_name = 'acs-web'
    # 上传到七牛后保存的文件名
    key = unicode(name);
    token = q.upload_token(bucket_name, key, 3600)
    # 要上传文件的本地路径
    localfile = pic_url
    print pic_url
    ret, info = put_file(token, key, localfile)
    if info.status_code == 200:
        return 'http://'+current_app.config['UPLOAD_DOMAIN']+'/'+key
    else:
        raise Exception('upload failed')

def del_pic(pic_name):
    access_key = current_app.config['QINIU_ACCESS_KEY']
    secret_key = current_app.config['QIUNU_SECRETE_KEY']
    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    bucket = BucketManager(q)
    bucket_name = 'acs-web'
    ret,info = bucket.delete(bucket_name,pic_name)
    if info.status_code != 200:
        raise  Exception('del failed')

# if __name__ == '__main__':
#     file_path = os.path.join(os.path.dirname(__file__), 'static')
#     print upload_qiniu(r'D:\acs\ACS-Website\app\static\u32321044642744552114fm21gp0.jpg','123')