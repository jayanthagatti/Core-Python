# def even(num):
#     if num%2==0:
#         return True
#     else:
#         return False
# l=[]
# i=0
# while i<=4:
#     num=int(input("enter a number: "))
#     l.insert(i,num)
#     i+=1
# print(l)
# i=0
# while i<=4:
#     data=l[i]
#     choice=even(data)
#     if choice==True:
#         print(l[i])
#     i+=1


# def even(num):
#     if num%2==0:
#         return True
#     else:
#         return False
# l=[]
# i=0
# while i<=4:
#     num=int(input("enter a number: "))
#     l.insert(i,num)
#     i+=1
# print(l)
# res=list(filter(even,l))
# print(res)

# def odd(num):
#     if num%2!=0:
#         return True
#     else:
#         return False
# l=[]
# i=0
# while i<=4:
#     num=int(input("enter a number: "))
#     l.insert(i,num)
#     i+=1
# print(l)
# res=list(map(odd,l))
# print(res)


#mapping
# def add(num):
#     return num+10
# l=[1,2,3,4,5]
# res=list(map(add,l))
# print(res)

l=[1,2,3,4,5]
res=list(map(lambda num:num+10,l))
print(res)

l=[1,2,3,4,5]
res=list(filter(lambda num:num%2==0,l))
print(res)