# _*_ encoding:utf-8 _*_
__author__ = "kusole"
__date__ = "17-11-21 上午10:45"

from .models import CityDict, CourseOrg, Teacher
import xadmin


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years','work_company','points','click_nums','fav_nums','add_time']
    search_fields = ['org', 'name', 'work_years','work_company','points','click_nums','fav_nums']
    list_filter = ['org__name', 'name', 'work_years','work_company','points','click_nums','fav_nums','add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
