from django.shortcuts import render,redirect,render_to_response
from Foods.models import User
from django.http import JsonResponse,HttpResponseRedirect
import hashlib
import smtplib #登陆邮件服务器，进行邮件发送
from email.mime.text import MIMEText #负责构建邮件格式

#加密
def setPassword(passwored):
    #进行加密
    md5 = hashlib.md5()
    md5.update(passwored.encode())
    return md5.hexdigest()


#发送邮件的函数
def email_info(emails):
    subject = "那都爬平台"
    content = "恭喜你注册成功，那都爬网站欢迎你的加入"#发送的内容
    sender = "1529825704@qq.com" #发送方的邮件
    recver = """{}""".format(emails)

    password = "ikamyyxncwsbjhhg" #邮箱配置生成器的那个编码

    message = MIMEText(content,"plain","utf-8")
    message["Subject"] = subject
    message["To"] = recver
    message["From"] = sender

    smtp = smtplib.SMTP_SSL("smtp.qq.com",465)
    smtp.login(sender,password)
    smtp.sendmail(sender,recver.split(",\n"),message.as_string())
    smtp.close()
#登录的装饰器
def loginValid(fun):
    def inner(request,*args,**kwargs):
        #获取cookies 和 session 去和数据库的对比
        c_user = request.COOKIES.get('username')
        s_user = request.session.get('username')
        if c_user and s_user:
            user = User.objects.filter(username=c_user).first()#返回的是一个对象
            print(user)
            if user and user.username == s_user:
                print(111)
                return fun(request,*args,**kwargs)
        return HttpResponseRedirect('/Foods/login/')
    return inner

#主页面
@loginValid
def index(request):
    name = request.COOKIES.get('username')
    return render(request,'index.html',locals())

#登录页面
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username :
            user = User.objects.filter(username=username).first()#从数据库读取密码
            if setPassword(password) == user.password:
                response = HttpResponseRedirect('/Foods/index/')
                response.set_cookie('username',user.username)#生成用户名的cookie
                request.session['username'] = user.username
                return response
        else:
            return render(request,'login.html',locals())
    else:
        return render(request,'login.html',locals())

#验证码的验证
def ajax_yz(request):
    result = {'status':'error','content':''}
    if request.method == 'GET':
        deco = request.GET.get('deco')#获取输入的验证码
        print(deco.lower())
        deco1 = request.GET.get('deco1')#获取生成的验证码
        print(deco1.lower())
        if deco:
            if deco.lower() == deco1.lower() :
                result['status'] = 'success'
                result['content'] = '验证码正确'
            else:
                result['content'] = '验证码错误'
        else:
            result['content'] = '验证码不可以为空'
    return JsonResponse(result)

#注册页面
def register(request):
    result = {'content':''}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if username and password:
            #从数据库获取用户名
            user = User.objects.filter(username=username).first()
            if user:
                result['content'] = '用户名已经被注册了'
            else:
                user = User()
                user.username = username
                user.mail = email
                user.password = setPassword(password)
                #保存数据
                user.save()
                email_info(email)
                return redirect('/Foods/login/')#返回登录页面
        else:
            result['content'] = '用户名或密码不可以为空'
    return render(request,'register.html',locals())

#前端的验证
def q_ajax(request):
    result = {'status': 'error', 'content': ''}
    username = request.GET.get('username')
    pas = request.GET.get('pas')
    if username:
        if  pas:
            result['content'] = 'ok'
        else:
            result['content'] = '密码不可以为空'
    else:
        result['content'] = '用户名不可以为空'
    return JsonResponse(result)

#注册页面的ajx的验证
#如果注册成功 发送邮件 告诉用户
def ajx_register(request):
    result = {'status':'error','content':''}
    username = request.GET.get('username')
    if username:
        username = User.objects.filter(username=username).first()
        if username:
            result['content'] = '这个用户名被抢走了'
        else:
            result['content'] = '用户名可以用'
            result['status'] = 'success'
    else:
        result['content'] = '用户名不可以为空'

    return JsonResponse(result)