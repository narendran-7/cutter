# import os
# 
# # 
# try:
#     os.mkdir("videos")
# except Exception:
#     os.chdir("videos")
# print(os.getcwd())

# 

from process.task import Convert

ob = Convert("yew.mp4",44,77)
ob.process()