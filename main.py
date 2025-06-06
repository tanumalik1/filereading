import os
file= "content.txt"
if os.path.exists(file):
    file=open("content.txt","r")
    content= file.read()
    print(content)
    file.close()
else :
    print("file does not exist")

