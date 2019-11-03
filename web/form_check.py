from django.forms import Form,fields,widgets
from repository import models
from django.core.exceptions import ValidationError

class Login(Form):
	account = fields.CharField(max_length=128,
							   required=True,
							   label='用户名',
							   error_messages={
								   'required':"用户名不能为空",
								   'invalid':"输入错误",
							   })
	pwd = fields.CharField(max_length=25,
						   required=True,
						   label='密码',
						   error_messages={
							   'required': "密码不能为空",
							   'invalid': "输入错误",
						   })
	verify_code = fields.CharField(max_length=4,
								   min_length=4,
								   required=True,
								   label='验证码',
								   error_messages={
									   'required': "验证码不能为空",
									   'max_length': "验证码长度必须为4",
									   'min_length': "验证码长度必须为4",
								   })


	def clean(self):
		cleaned_data = super().clean()
		account = cleaned_data.get('account')
		pwd = cleaned_data.get('pwd')
		if models.User.objects.filter(account=account).count():
			if models.User.objects.filter(account=account)[0].pwd != pwd:
				print(pwd)
				raise ValidationError('用户名或密码错误')
			else:
				return self.cleaned_data
		else:
			raise ValidationError("用户名不存在")


class Register(Form):
	username= fields.CharField(max_length=25,
							   required=True,
							   label='昵称',
							   error_messages={
								   'required': "昵称不能为空",
								   'invalid': "输入错误",
								   'max_length': "账户长度不能超过25",
							   })
	account = fields.CharField(max_length=128,
							   required=True,
							   label='用户名',
							   error_messages={
								   'required': "用户名不能为空",
								   'invalid': "输入错误",
							   })

	pwd = fields.CharField(max_length=32,
						   min_length=8,
						   required=True,
						   label='密码',
						   error_messages={
							   'required': "密码不能为空",
							   'invalid': "输入错误",
							   'max_length': "账户长度不能超过32",
							   'min_length': "密码长度不能少于8",
						   })

	confirm_pwd = fields.CharField(max_length=32,
						   min_length=8,
						   required=True,
						   label='密码',
						   error_messages={
							   'required': "密码不能为空",
							   'invalid': "输入错误",
							   'max_length': "账户长度不能超过32",
							   'min_length': "密码长度不能少于8",
						   })

	email = fields.EmailField(max_length=255,
							  required=True,
							  label='邮箱',
							  error_messages={
							   'required': "邮箱不能为空",
							   'invalid': "邮箱格式错误",
						   })

	img = fields.ImageField(required=True,
							label='图片',
							error_messages={
								'required': "图片不能为空",
							})

	verify_code = fields.CharField(max_length=4,
								   min_length=4,
								   required=True,
								   label='验证码',
								   error_messages={
									   'required': "验证码不能为空",
									   'max_length': "验证码长度必须为4",
									   'min_length': "验证码长度必须为4",
								   })


	def clean_account(self):
		try:
			account = self.cleaned_data['account']
		except:
			pass
		if models.User.objects.filter(account=account).count():
			raise ValidationError("账号已存在")
		else:
			return self.cleaned_data["account"]

	def clean(self):
		print("开始校验密码一致性")
		pwd = self.cleaned_data['pwd']
		confirm_code = self.cleaned_data['confirm_pwd']
		print(pwd)
		print(confirm_code)

		if pwd != confirm_code:
			print('密码不一致')
			raise ValidationError("密码输入不一致，请重新输入")
		else:
			print("密码通过校验")
			return self.cleaned_data