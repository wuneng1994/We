class Pagination(object):
	def __init__(self,total_num,current_page,per_page_item_num=30,max_page_num = 7):
		# 数据总个数
		self.total_num = total_num
		# 当前页
		try:
			self.current_page = int(current_page)
		except Exception as e:
			print(e)
		# 每页显示的行数
		self.per_page_item_num = per_page_item_num
		# 最多显示页面
		self.max_page_num = max_page_num

	def start(self):
		return (self.current_page-1)*self.per_page_item_num

	def end(self):
		return self.current_page*self.per_page_item_num

	@property
	def num_pages(self):
		# 总页数
		temp = divmod(self.total_num,self.per_page_item_num)
		if temp[1]:
			return temp[0]+1
		return temp[0]

	def per_page_range(self):
		# 页码范围
		if self.num_pages < self.max_page_num:
			return range(1,self.num_pages+1)
		part = int(self.max_page_num/2)
		if self.current_page <= part:
			return range(1,self.max_page_num)
		if self.current_page >= self.num_pages-part:
			return range(self.num_pages-self.max_page_num+1,self.num_pages+1)
		return range(self.current_page-part,self.current_page+part+1)

	def prev_page(self):
		if self.current_page ==1:
			return 1
		return self.current_page-1

	def next_page(self):
		if self.current_page == self.num_pages:
			return self.num_pages
		return self.current_page+1

	def has_next_page(self):
		if self.current_page == self.num_pages:
			return False
		return True

	def has_prev_page(self):
		if self.current_page == 1:
			return False
		return True

	def page_str(self):
		# 生成分页html文本
		page_list = []
		first = "<li><a href='/home2.html/?p=1'>首页</a></li>"
		page_list.append(first)
		if self.current_page == 1:
			prev = "<li><a href=''>上一页</a></li>"
		else:
			prev = "<li><a href='/home2.html/?p=%s'>上一页</a></li>"%(self.current_page-1)
		page_list.append(prev)
		for i in self.per_page_range():
			if i == self.current_page:
				temp = "<li class='active'><a href='/home2.html/?p=%s'>%s</a></li>"%(i,i)
			else:
				temp = "<li><a href='/home2.html/?p=%s'>%s</a></li>"%(i,i)
			page_list.append(temp)
		if self.current_page == self.current_page:
			nex = "<li><a href=''>下一页</a></li>"
		else:
			nex = "<li><a href='/home2.html/?p=%s'>下一页</a></li>"%(self.current_page+1)
		page_list.append(nex)
		first = "<li><a href='/home2.html/?p=%s'>尾页</a></li>"%self.num_pages
		page_list.append(first)
		return page_list



