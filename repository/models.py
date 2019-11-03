from django.db import models
import uuid

# Create your models here.
class User(models.Model):
	uid = models.AutoField(primary_key=True,verbose_name="用户id")
	account = models.CharField(max_length=128,verbose_name='用户名',unique=True)
	username = models.CharField(max_length=25,verbose_name="用户昵称")
	pwd = models.CharField(max_length=32,verbose_name="密码")
	email = models.EmailField(max_length=255,verbose_name="邮箱")
	img = models.ImageField(upload_to='static/user_img')
	# relationship = models.ManyToManyField(to='self', related_name='ship',blank=True,null=True)

	def __str__(self):
		return self.username

	class Meta:
		verbose_name_plural = "用户信息"

class Blog(models.Model):
	theme_type = [('blue',"蓝色"),('red',"红色"),('green',"绿色")]
	bid = models.AutoField(primary_key=True,verbose_name="博客id")
	# surfix = models.CharField(max_length=32,verbose_name="博客后缀")
	theme = models.CharField(choices=theme_type,max_length=10,verbose_name="主题类型")
	title = models.CharField(max_length=255,verbose_name="博客标题")
	summary = models.TextField(verbose_name="博客简介",null=True,blank=True)
	user = models.OneToOneField(to=User,on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = "博客信息"

class UserRelationship(models.Model):
	start = models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name='被关注者',related_name='s')
	fans = models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name='关注者',related_name='f')

	def __str__(self):
		return "%s > %s" %(self.fans.username,self.start.username)

	class Meta:
		verbose_name_plural = "互粉表"
		unique_together = ('start','fans',)

class Reporting(models.Model):
	UUID = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,verbose_name='报障单号')
	title = models.CharField(max_length=255,verbose_name="标题")
	detail = models.TextField(verbose_name='故障详细描述')
	user = models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name='提交用户',related_name='u')
	processor = models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name='处理者',null=True,blank=True,related_name='p')
	status = models.CharField(max_length=25,verbose_name='状态',choices=[('unprocess','待处理'),('processing','处理中'),('processed','已处理')])
	create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
	process_time = models.DateTimeField(null=True,blank=True,verbose_name='处理时间')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = '报障单'

class Classification(models.Model):
	name = models.CharField(max_length=32,verbose_name='博客分类')
	blog = models.ForeignKey(Blog,on_delete=models.CASCADE,verbose_name='博客')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = '博客分类'


class Caption(models.Model):
	name = models.CharField(max_length=32, verbose_name='博客标签')
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='博客')

	def __str__(self):
		return "%s <--->%s" %(self.blog,self.name)

	class Meta:
		verbose_name_plural = '博客标签'

class ArticleDetial(models.Model):
	text = models.TextField(verbose_name="文章正文")


	class Meta:
		verbose_name_plural = '文章正文'

class Article(models.Model):
	article_type = [(1,"Python"),(2,"Java"),(3,"Django"),(4,"JavaScript"),(5,"五彩缤纷")]
	title = models.CharField(max_length=255,verbose_name='文章标题')
	author = models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name="作者")
	summary = models.TextField(verbose_name='文字简介')
	ctime = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
	text = models.OneToOneField(to=ArticleDetial,on_delete=models.CASCADE,verbose_name="文章正文")
	type_id = models.IntegerField(verbose_name='文章类型',choices=article_type,)

	def __str__(self):
		return "%s----%s"%(self.author,self.title)
	class Meta:
		verbose_name_plural = '文章列表'

class ArticleToCaption(models.Model):
	article = models.ForeignKey(to=Article,on_delete=models.CASCADE,verbose_name='文章')
	caption = models.ForeignKey(to=Caption,on_delete=models.CASCADE,verbose_name='标签')

	class Meta:
		verbose_name_plural = '文章标签关系'
		unique_together = ('article','caption')

class Comment(models.Model):
	content = models.TextField(verbose_name='评论内容')
	article = models.ForeignKey(to=Article, on_delete=models.CASCADE, verbose_name='文章')
	user = models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name='用户')
	ctime = models.DateTimeField(auto_now_add=True)
	parent_comment = models.ForeignKey('self',verbose_name='父评论',on_delete=models.CASCADE,null=True,blank=True)

	def __str__(self):
		return self.content
	class Meta:
		verbose_name_plural = '评论表'

class Perference(models.Model):
	article = models.ForeignKey(to=Article, on_delete=models.CASCADE, verbose_name='文章')
	user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='用户')
	perfer = models.NullBooleanField(verbose_name="偏好")

	class Meta:
		verbose_name_plural = '踩赞表'
		unique_together = ('article','user')


