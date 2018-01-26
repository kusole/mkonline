# _*_ encoding:utf-8 _*_
from django.shortcuts import render, render_to_response
from django.views.generic.base import View
from .models import CourseOrg, CityDict
from operation.forms import UserAskForm
from django.http import HttpResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

class OrgView(View):
    """
    课程机构列表功能
    """

    def get(self, request):
        # 课程机构
        all_orgs = CourseOrg.objects.all()
        hot_orgs = all_orgs.order_by("-click_nums")[:3]

        # 城市
        all_citys = CityDict.objects.all()

        # 取出城市
        city_id = request.GET.get('city', "")
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 类别刷选
        category = request.GET.get('ct', "")
        if category:
            all_orgs = all_orgs.filter(category=category)

        # 排序筛选
        sort = request.GET.get('sort',"")
        if sort:
            if sort=='student':
                all_orgs = all_orgs.order_by("-students")
            elif sort == 'courses':
                all_orgs = all_orgs.order_by("course_nums")
        # 统计筛选出的课程数目
        org_nums = all_orgs.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, request=request, per_page=3)

        orgs = p.page(page)

        return render(request, "org-list.html", {
            'all_orgs': orgs,
            'all_citys': all_citys,
            'org_nums': org_nums,
            'city_id': city_id,
            'category': category,
            'hot_orgs':hot_orgs,
            'sort':sort,
        })

# modelform方法,省事
class AddUserAskView(View):
    """
    用户添加咨询
    """
    def post(self,request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse('{"status":"success"}',content_type='application/json')
        else:
            # return HttpResponse("{'status':'fail,'msg':{0}}".format(userask_form.errors),content_type='application/json')
            return HttpResponse('{"status":"fail","msg":"添加出错"}', content_type='application/json')