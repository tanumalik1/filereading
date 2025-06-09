import os
input_user=input("Enter text to write to the file: ")
with open("output.txt","w") as file :
    file.write(input_user+ "\n")
new_data= input("Enter additional text to append: ")
with open("output.txt","a") as file:
    file.write(new_data+ "\n")
    print("Data succesfully appended")
with open("output.txt","r") as file:
    content1= file.read()
    print(content1)