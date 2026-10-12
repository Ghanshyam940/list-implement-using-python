# f=open('file.txt')
# content=f.read()
# print(content)
# f.close()


# file=("Ram is studying in class 10th")
# file=open('file.txt','w')
# file.write("Ram is studying in class 10th")
# file.close() 


file=open('file.txt')
line1=file.readline()
print(line1,type(file))
file.close()