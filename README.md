# GUTIC NEWSLETTER TOOL

This a simple tool built for the Glasgow University Trading and Investment Club (GUTIC) to quickly produce and send out a newsletter with financial news for the members. This project uses *summa* to summarise the text of an article into a digestable format (the aim is to implement *smmry* instead). This project is not entirely finished, but will at this stage produce an acceptable output. The code has only beed tested on Mac OS, but should run fine (in theory) on windows machines.

###### Getting started
To get started, follow these simple steps:

1. Download and locate the NewsBot folder
2. Navigate to the folder using the terminal and run the following command:
> pip install requirements.txt
3. Run newsbot.py to start the GUI



###### Using the the tool
When you run newsbot.py, you should be presented with a simple GUI. 

![alt text](https://i.imgur.com/DXYFLto.png)


The basic workflow of using the bot is as follows.
1. Enter the title of the article in the **Article Title** field.
2. Paste the article text in the **Insert text** field. 
3. Add the URL to the **URL** field to make sure you credut the original authour **(unimplemnted feature)**.
4. Press *Summarise Input*, a summary of the article should now appear in the **Summary** field.
5. Edit the summary, *summa* is not the most effective algorithm. 
6. Press the *Accept Summary* button. The article will be added to the **Article List**.
7. Five articles should be added. Pictures can now also be added by drag and drop. The picture functionality is slightly broken.
8. Press *create*. The programme will ask you to choose a directory for the output. The newsletter will be porduced as .pptx file and can manually be saved to a desirable format (.pdf/.jpg).

###### Sample Out
![alt text](https://i.imgur.com/l856sMN.png)






