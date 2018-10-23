import os
import sys
#from smmryapi import SmmryAPI
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QWidget,QApplication, QMainWindow, 
							QPushButton, QFileDialog,
							QPlainTextEdit, QListWidget,
							QLabel, QLineEdit)
from newsbot_data import data
from newsbot_output import pptx_output
#from smmryAPI import summarize
from summa.summarizer import summarize



class NewsBotGUI(QWidget):
	def __init__(self):
		super(NewsBotGUI, self).__init__()
		self.all_data = data() #Initialise data class
		self.article_index = []
		self.pic_index = []
		self.initUI()

	def initUI(self):
		self.setWindowTitle("GUTIC NewsBot")
		self.setFixedSize(640,450)
		self.input()
		self.buttons()
		self.labels()
		self.show()

	def input(self):
		#Create all the input fields
		self.titleBox = QLineEdit(self)
		self.titleBox.setGeometry(10,30,200,20)

		self.inputBox = QPlainTextEdit(self)
		self.inputBox.setGeometry(10,80,200,270)

		self.summaryBox = QPlainTextEdit(self)
		self.summaryBox.setGeometry(220,30,200,370)

		self.urlBox = QLineEdit(self)
		self.urlBox.setGeometry(10,380,200,20)

		self.articleList = QListWidget(self)
		self.articleList.setGeometry(430,30,200,100)

		self.picList = QListWidget(self)
		self.picList.setGeometry(430,190,200,100)


	def labels(self):
		#Create all static labels
		titleLab = QLabel( self)
		titleLab.setGeometry( 10, 10, 200, 20 )
		titleLab.setText('<b>Article Title </b>')

		inputLab = QLabel( self)
		inputLab.setGeometry( 10, 60, 200, 20 )
		inputLab.setText('<b>Insert text  </b>')

		summaryLab = QLabel( self)
		summaryLab.setGeometry( 220, 10, 200, 20 )
		summaryLab.setText('<b>Summary </b>')

		summaryLab = QLabel( self)
		summaryLab.setGeometry( 430, 10, 210, 20 )
		summaryLab.setText('<b>Article List </b>')

		urlLab = QLabel( self)
		urlLab.setGeometry( 10, 360, 200, 20 )
		urlLab.setText('<b>URL (instead of manual input)</b>')

		DragAndDropLab = DragAndDropLabel('Drop picture here', self)
		DragAndDropLab.setGeometry( 430, 360, 200, 20 )
		#logoLab = QLabel(self)
		#logoLab.setGeometry(50, 40, 250, 250)
		#pixmap = QPixmap(os.getcwd() + "/gutic_logo.png")
		#logoLab.setPixmap(pixmap)
		#Put the GUTIC logo in the coner, dome back and finish later

	def buttons(self):
		#Initialise all the buttons
		ouputButton = QPushButton('Create', self)   
		ouputButton.clicked.connect(self.produce_putput) 
		ouputButton.setGeometry(430,410,210,40)

		summariseButton = QPushButton('Summarise Input', self)   
		summariseButton.clicked.connect(self.summarise) 
		summariseButton.setGeometry(5,410,210,40)

		acceptButton = QPushButton('Accept Summary', self)   
		acceptButton.clicked.connect(self.accept_input) 
		acceptButton.setGeometry(215,410,210,40)

		deleteArticleButton = QPushButton('Delete Article', self)   
		deleteArticleButton.clicked.connect(self.delete_article) 
		deleteArticleButton.setGeometry(425,140,210,40)

		deletePicButton = QPushButton('Delete Picture', self)   
		deletePicButton.clicked.connect(self.delete_picture) 
		deletePicButton.setGeometry(425,300,200,40)

	def summarise(self):
		input_text = self.inputBox.toPlainText()
		if input_text != "": #If there is text, summarise it
			summary = summarize(input_text, words = 50)
		else:
			summary = ""
			#		self.urlBox.text()
		self.summaryBox.clear()
		self.summaryBox.insertPlainText(summary)

	def accept_input(self): 
		article = self.summaryBox.toPlainText()
		title   = self.titleBox.text()
		if title == "" or article == "":
			self.test() #Implement a popup feature
			return 
		if len(self.article_index) == 5:
			self.test()
			return


		self.articleList.addItem(title)
		self.all_data.add_articles(article, title)
		self.article_index.append(title)
		
		#Clear everything for a new article
		self.titleBox.clear()
		self.inputBox.clear()
		self.summaryBox.clear()

	def add_picture_drag_and_drop(self, path):
		self.picList.addItem(path)
		self.pic_index.append(path)
		self.all_data.add_pictures(path)
	
	def delete_article(self):
		listItems=self.articleList.selectedItems()
		if not listItems: #Check if a list item has actually been slected
			return
		for item in listItems:
			self.articleList.takeItem(self.articleList.row(item))
			index = self.article_index.index(item.text())
			self.article_index.pop(index)
			self.all_data.remove_articles(index)

	def delete_picture(self):
		listItems=self.picList.selectedItems()
		if not listItems:
			return
		for item in listItems:
			self.picList.takeItem(self.picList.row(item))
			index = self.pic_index.index(item.text())
			self.pic_index.pop(index)
			self.all_data.remove_pictures(index)

	def set_save_folder(self): 
		self.all_data.set_savefolder(str(QFileDialog.getExistingDirectory(self, "Select Directory")))

	def produce_putput(self):
		self.set_save_folder()
		print(self.all_data.articles)
		print(self.all_data.titles)
		if len(self.all_data.articles) == 5: #Five articles required for template
			titles     = self.all_data.titles
			articles   = self.all_data.articles
			pics       = self.all_data.pics
			savefolder = self.all_data.savefolder
			pptx_output(titles, articles, pics, savefolder)

		else:
			self.test() #An error function should be implemented
			
	def test(self):
		print("This button works")

class DragAndDropLabel(QLabel):
	#A class to hadnle drag and drop events
	def __init__(self, title, parent):
		super().__init__(title, parent)
		self.parent = parent
		self.setAcceptDrops(True)

	def dragEnterEvent(self, event):
		if event.mimeData().hasUrls():
			event.accept()
		else:
			event.ignore()

	def dropEvent(self, event):
		for url in event.mimeData().urls():
			path = url.toLocalFile()
			print(path)
			self.parent.add_picture_drag_and_drop(path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NewsBotGUI()
    sys.exit(app.exec_())
