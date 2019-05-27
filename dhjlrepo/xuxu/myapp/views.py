import pymysql
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


from myapp.models import User
from myapp.forms import UserForm
from libs.cache import get_code


conn = pymysql.Connect(host='localhost',
                       port=3306,
                       user='root',
                       password='dong',
                       database='xmdb')


def go_home(request):  # 跳转至首页,仅能注册登录
    return render(request, 'base_home.html')


def quicksou(request):  # 跳转至登录后的主页
    username = request.session['username']
    return render(request, 'nav/quicksou.html', locals())


def regist(request):  # 注册
    if request.method == 'GET':
        return render(request, 'reg-log/sign-up.html')
    elif request.method == 'POST':
        form = UserForm(request.POST)
        # 验证数据的完整性
        if form.is_valid():
            code = get_code(form.cleaned_data.get('telephone')).decode()
            if code == form.cleaned_data.get('code'):
                form.save()  # 无错时保存数据
                return redirect(reverse('myapp:login'))
            else:
                return render(request, 'reg-log/sign-up.html', {'errors':'验证失败'})
        errors = form.errors  # 默认情况下，是html的错误信息
        return render(request, 'reg-log/sign-up.html', locals())


def login_view(request):  # 登录
    if request.method == 'GET':
        return render(request, 'reg-log/sign-in.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        passwd = request.POST.get('passwd')
        users = User.objects.filter(username=username)
        if users:
            user = users.first()
            if user.password == passwd:
                request.session['username'] = username
                return redirect(reverse('myapp:jobs'))
        else:
            return render(request, 'reg-log/sign-in.html', {'errors': '用户名或密码错误'})


def to_jobs(request):
    username = request.session['username']
    return render(request, 'nav/jobs.html',locals())


def to_company(request, name):
    username = request.session['username']
    company_temp = 'job_company/' + name + '.html'
    print(company_temp,'-------------------------------------')
    return render(request, company_temp, locals())


page_size = 10


def map_table(name):
    if name == 'zhilian':
        name = 'zhilian_01'
    elif name == 'boss':
        name = 'boss_01'
    elif name == 'qiancheng':
        name = 'qiancheng2'
    return name


def find_jobs(request, name, pagenum=1):
    username = request.session['username']
    info = request.POST.get('info')
    if info:
        request.session['info'] = info
    info = request.session['info']
    print(info)
    # path = request.path
    # name = re.findall(r'job/(\(w+)\)', path)[0]
    job_temp = 'job_company/' + name + '.html'
    tablename = map_table(name)
    username = request.session['username']
    fields = 'job_name, job_company, job_region, job_company_type, \
            job_company_pernum, job_exp, job_edu, job_salary '
    limit = 'job_name like "%' + info +  \
            '%" or job_company like "%' + info + \
            '%" or job_salary like "%' + info + \
            '%" or job_region like "%' + info + \
            '%" or job_company_type like "%' + info + \
            '%" or job_company_pernum like "%' + info + \
            '%" or job_exp like "%' + info + \
            '%" or job_edu like "%' + info + '%"'
    sql = 'select %s from %s where %s' % (fields, tablename, limit)
    # print(sql)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql)
    results = cursor.fetchall()
    paginator = Paginator(results, page_size)
    page = paginator.page(pagenum)
    pagecount = paginator.num_pages
    current_page_num = page.number
    return render(request, job_temp, {'page': page,
                                       'pagecount':pagecount,
                                       'current_page':current_page_num,
                                       'paginator': paginator,
                                       'username':username})


def logout(request):
    request.session.flush()
    return redirect(reverse('myapp:home'))
