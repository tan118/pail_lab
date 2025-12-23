# import pyjokes
# joke=pyjokes.get_joke()
# print(joke)
# a=9
# b=6
# b+=3
# print(b)
# b<a
# print(b)
# n=int(input("entre a no "))
# i=0
# while (i<=10):
#     print(f"{n}X{i}={n*i}")
#     i+=1   
# n=int(input("enter a no "))
# for i in range (1,n):
#     if (n%i)==0:
#       print("n is not  prime ")
#       break
#     else:
#        print("is  prime ")
# i=1
# sum=0
# while(i<=10):
#     sum+=i 
#     i+=1
#     print(sum)
# n=int(input("enter a no"))
# product=1
# for i in range(1,n+1):
#     product=product*i
#     print(product)
'''  
  *
 ***
*****
 '''
# n=int(input("enter a no"))
# for i in range(1,n+1):
#     print("*"* (3*i))
#     print("*",end="")
#     print(" ",end="")
#     print("*")
#     print("*"* (3*i))
# n=int(input("enter a no"))
# for i in range(1,n+1):
#     if i==1 or i==n:
#         print("*"*n) 
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*")
#     print("")
 
# n=int(input("enter a no"))  
# for i in range(1,11):
#     print((11-i)*n)
   
# n=int(input("enter a no"))
# i=1
# while(i<=10):
#     print((11-i)*n)
#     i+=1
# def goodday(name,end):
#     print(f"hey how are u. good dsy{name}\n bye\n{end}")
#     return 3
    
# a=goodday("harry","tq")

# def factorial(n):
#         if(n==1 or n==0):
#             return 1
#         return n * factorial(n-1)

# n=int(input("enter a no"))
# print(f"the factorialof no is :",factorial(n))

# def greatest_all():
#     if (n>n1 and n>n2):
#         print(" gratest ",n)
#     elif (n1>n and n1>n2):
#         print(" gratest ",n1)
#     elif(n2>n and n2>n1):
#         print(" gratest ",n2)
# n=int(input("enter a no"))
# n1=int(input("enter a no"))
# n2=int(input("enter a no"))
# greatest_all()
# def f_to_c(f):
#     return 5*(f-32)/9
# def c_to_f(c):
#     return c*9/5+32
# c=int(input("enter value in celcius"))
# print(c_to_f(c))
# f=int(input("enter value in f")
# print((f_to_c(f))


# def sum(n):
#         if(n==1 or n==0):
#             return 1
#         return sum(n-1)+n
# print(sum(4))
'''***
   **
   *
   '''
# def pattern(n):
#       if (n==0):
#        return
#       print("*"*n)
#       (pattern(n-1))
# n=int(input("enter a no"))
# pattern(n)
# print(pattern(3))
# print(pattern(5))
# def table(n):
#     for i in range(1,11):
#         print(n*i)
# print(table(6))    
# f=open("sample.txt")
# data=f.readline()
# print(data)
# f.close
# the same can be writtten as 
# with open("sample.txt") as f:
#   print(f.readline())
  
# f=open("sample1.txt","w")
# f.write("hey gorgeouss !!")
# f.close

# f=open("sample.txt","a")
# f.write("omg")
# f.close

# with open("sample.txt") as f:
#    a= f.read()
# if("twinkle" in a):
#     print("found") 
# else:
#     print ("not found ")
# grate ques
# import random
# def game():
#     print("you are playing this game")
#     score=random.randint(1,600)
#     with open("sample.txt")as f:
#         hi_score=f.read()

#         if (int(hi_score=="" or hi_score==0)):
#          print("hi_score=0")
#         else:
#            print ("hi_score is")
#            print (int(hi_score))

#     print(f"your score is {score}")           
#     if (int(score) > int(hi_score)):
#        print(f"you have set new hi_score{score}")
#        with open("sample.txt","w")as f:
#           f.write(str(score))
#     else:
#        print("try again")
# game()
# def generatetable(n):
#   table=""
#   for i in range(1,11):
    
#     table+=f" {n}X{i} = {n*i}\n"

#   with open("tables.table{n}.txt","w")as f:
#    f.write(table)

# for i in range(2,21):
# #    generatetable(i)

# words=["donkey","bullshit","creep"]
# with open("sample.txt","r")as f:
#     content=f.read()
# for word in words:
#    content=content.replace(word,"#"*len(word))
# with open("sample.txt","w")as f:
#                 f.write(content)

# lineno=1     
# with open("sample.txt","r") as f:
#   lines=f.readlines()
# for line in lines:
#  if("python" in line ):
#   print("python found {lineno}")
#   break
#  lineno+=1

with open("sample.txt","r")as f:
    content1=f.read()
with open("sample1.txt","r")as f:
    content2=f.read()
if(content1==content2):
    print("content idnetical")
else:
    print("nope")

