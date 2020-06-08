import os #file에 접근하려
import random #random 하게 섞으려고
#C:/ wra wer / asdv /raw /random

#path = input() # C:/ 를 입력하면 C폴더안의 내용이 file_name에 들어감.
splitList1 =[]
ignoreList1=[]
result=[]
ignoreCheck=""
path= input()
splitList1 = path.split('/')
lastlistLen=len(splitList1[-1]) # 맨마지막 부분 길이
splitList1[-1]=splitList1[-1].strip()
checkPoint = splitList1[-1].strip() # wer/ random 처럼 공백이 있을까봐 공백제거

if len(checkPoint)<7:
    pass
else:
    s1=checkPoint[0] #i
    s2=checkPoint[1] #g 
    s3=checkPoint[2] #n
    s4=checkPoint[3] #o
    s5=checkPoint[4] #r
    s6=checkPoint[5] #e
    s7=checkPoint[6] #-
    ignoreCheck = s1+s2+s3+s4+s5+s6+s7

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

if checkPoint =='random': #random으로 배열
    path=path[:-lastlistLen] #random뺴줘야함
    file_names=os.listdir(path)
    random.shuffle(file_names)
    result = file_names
elif ignoreCheck=='ignore-':
    ignoreList1=checkPoint.split('-')
    save_file_name=[]
    path=path[:-lastlistLen]
    file_names=os.listdir(path)
    file_names.sort(key=str.lower)
    #여기에서 ignore뒤에 -로 나뉜부분만 걸러내야함. 띄어쓰기없슴
    save_file_name= remove_values_from_list(file_names,ignoreList1[1])
    result = save_file_name
    pass
else: # 소문자로바꿔서 사전순으로 배열
    file_names=os.listdir(path)
    file_names.sort(key=str.lower)
    result = file_names
print (result)
