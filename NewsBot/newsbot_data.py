class data():
	# TODO:
	# * Figure out a way to store pictures
	def __init__(self):
		self.articles  = []
		self.pics = []
		self.titles = []
		self.savefolder = ""   




	def add_articles(self, article, title):
		self.articles.append(article)
		self.titles.append(title)

	def add_pictures(self,path):
		self.pics.append(path)

	def remove_articles(self,index):
		self.articles.pop(index)
		self.titles.pop(index)

	def remove_pictures(self,index):
		self.pics.pop(index)


	def set_savefolder(self,string):
		self.savefolder = string