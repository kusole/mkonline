# _*_ encoding:utf-8 _*_
__author__ = "kusole"
__date__ = "17-11-22 下午3:40"

from random import Random

from users.models import EmailVerifyRecord
from django.core.mail import send_mail
from mkonline.settings import EMAIL_FROM

def random_str(randomlenth=8):
    str = ''
    chars = 'abcdefghikglmnopqrstuvwxyzABCDEFGHIJGLMNOPQRSTUVWXYZ1234567890'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlenth):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type="register"):
    code = random_str(16)
    email_record = EmailVerifyRecord()
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == 'register':
        email_title = u"mxonline在线激活链接"
        email_body = u"请点击下面的链接进行激活：http://127.0.0.1:8000/active/{0}".format(code)
        send_status = send_mail(email_title, email_body,EMAIL_FROM,[email])
        if send_status:
            pass
