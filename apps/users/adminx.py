# _*_ encoding:utf-8 _*_
__author__ = "kusole"
__date__ = "17-11-20 下午10:49"

from .models import EmailVerifyRecord
from .models import Banner
import xadmin
from xadmin import views


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


class GlobalSetting(object):
    site_title = u"安捷光通安全培训系统后台管理平台"
    site_footer = u"2017安捷光通成都科技有限公司"
    menu_style = "accordion"

class BaseSetting(object):
    enable_themes=False
    use_bootswatch=False

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView,BaseSetting)