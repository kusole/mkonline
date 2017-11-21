# _*_ encoding:utf-8 _*_
__author__ = "kusole"
__date__ = "17-11-20 下午10:49"
from .models import EmailVerifyRecord

import xadmin

class EmailVerifyRecordAdmin(object):
    pass
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
