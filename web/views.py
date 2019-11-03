from django.shortcuts import render,redirect,HttpResponse
from django.template.loader import get_template
from django.template import RequestContext
from repository import models
from django.core import paginator
from django.urls import reverse
from django.views import View
from web import form_check
from utils import create_vcode_img
from io import BytesIO
# Create your views here.

class CustomPaginate(paginator.Paginator):
	#django分页自定制页
	def __init__(self,current_page,per_page_num,*args,**kwargs):
		self.current_page = int(current_page)
		self.per_page_num = int(per_page_num)
		super().__init__(*args,**kwargs)

	def per_page_range(self):
		if self.num_pages < self.per_page_num:
			return range(1,self.num_pages+1)
		part = int(self.per_page_num/2)
		if self.current_page <= part:
			return range(1,self.per_page_num+1)
		if self.current_page >= self.num_pages-part:
			return range(self.num_pages-self.per_page_num+1,self.num_pages+1)
		return range(self.current_page-part,self.current_page+part+1)

def apply_verify_code(request):
	'''
	@todo:相应验证码请求，返回图片
	:param request: request
	:return:
	'''
	try:
		img,code = create_vcode_img.create_validate_code()
	except:
		raise OSError("创建验证码图片失败")
	print(code)
	request.session['verify_code']=code.upper()
	img_obj = BytesIO()
	img.save(img_obj,'PNG')
	return HttpResponse(img_obj.getvalue())


def index(request,*args,**kwargs):
	article_type = models.Article.article_type#获取数据库中文章类型

	if kwargs.get('type_id'):
		base_url = reverse('index',kwargs=kwargs)
	else:
		base_url = '/index/'

	article_obj = models.Article.objects.all().filter(**kwargs).order_by('-id')

	try:
		current_page = int(request.GET.get('page_num'))
	except:
		current_page = 1
	pag_obj = CustomPaginate(current_page,3,article_obj,3)

	if current_page in pag_obj.page_range:
		# print(current_page)
		pass
	else:
		if current_page>pag_obj.num_pages:
			current_page = pag_obj.num_pages
		else:
			current_page = 1

	article_list = pag_obj.page(current_page)

	if 'is_login' in request.session and request.session['is_login']==True:
		account = request.session['account']

	# template = get_template('index.html')
	# request_context = RequestContext(request)
	# request_context.push(locals())
	# html = template.render(**locals())
	# # template.render(locals())
	# response = HttpResponse(template)

	return render(request,'index.html',locals())

class Register(View):
	def get(self,request):
		obj = form_check.Register()
		return render(request,'register.html',locals())

	def post(self,request):
		obj = form_check.Register(request.POST or None,request.FILES or None)
		verify_code = request.POST.get("verify_code").upper()

		if verify_code == request.session['verify_code']:
			print('验证码正确')
		else:
			obj.errors['verify_code']=("验证码输入错误",)
			return render(request, 'register.html', locals())

		if obj.is_valid():
			try:
					dic_user = {
						'username': obj.cleaned_data['username'],
						'pwd': obj.cleaned_data['pwd'],
						'account': obj.cleaned_data['account'],
						'email': obj.cleaned_data['email'],
						'img': obj.cleaned_data['img']
					}
					print(dic_user)
					models.User.objects.create(**dic_user)
					request.session['is_login'] = True
					request.session['account'] = dic_user['account']
					request.session.set_expiry(0)
			except:
				print("用户创建失败")
				return render(request, 'register.html', locals())
		else:
			return render(request, 'register.html', locals())

		response = redirect(reverse('index', kwargs={'type_id': 0}))
		return response

class Login(View):
	def get(self,request):
		obj = form_check.Login()
		return render(request,'login.html',locals())

	def post(self,request):
		obj = form_check.Login(request.POST)
		verify_code = request.POST.get("verify_code").upper()
		if verify_code == request.session['verify_code']:
			print('验证码正确')
		else:
			obj.errors['verify_code']=("验证码输入错误",)
			return render(request, 'register.html', locals())
		if obj.is_valid():
			request.session['is_login'] = True
			request.session['account'] = request.POST['account']
			request.session.set_expiry(0)
			response = redirect(reverse('index',kwargs={'type_id':0}))
			return response
		else:
			print("登录失败")
			return render(request, 'login.html', locals())

def logout(request):
	request.session['is_login'] = False
	request.session['account'] = ""
	response = redirect(reverse('index', kwargs={'type_id': 0}))
	return response


def blog(request,blog):
	user_obj = models.User.objects.filter(account=blog).all().first()
	blog_obj = models.Blog.objects.filter(user__account=blog).all().first()
	caption_obj = models.Caption.objects.filter(blog__user__account=blog)
	article_obj = models.Article.objects.filter(author__account=blog)
	return render(request,'blog.html',locals())

def get_article(request,blog,article_id):
	user_obj = models.User.objects.filter(account=blog).all().first()
	blog_obj = models.Blog.objects.filter(user__account=blog).all().first()
	caption_obj = models.Caption.objects.filter(blog__user__account=blog)
	article_obj = models.Article.objects.filter(author__account=blog,id=article_id)[0]
	print(article_obj.comment_set.all())
	return render(request,'article.html',locals())