from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from myapp.models import User

LOGIN_REQUIRED = ["/myapp/jobs/", '/myapp/company/' ]


class LoginMiddleware(MiddlewareMixin):   # 自定义登录中间件
    def process_request(self,request):
        if request.path in LOGIN_REQUIRED:   #  判断当前请求路径是否需要登录
            username = request.session.get("username")
            if username:
                user = User.objects.get(username=username)  # 查出当前用户
                request.user = user   #  给request请求对象动态添加user属性，属性值为当前登录用户
            else:
                request.session["msg"] = "您还未登录，请先登录！"   # 在session中添加错误消息
                return redirect(reverse("myapp:login"))
