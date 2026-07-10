# l=[]
# i=0
# while True:
#     print("enter a number: ")
#     num=int(input())
#     l.insert(i,num)
#     i+=1
#     print("do you want to continue")
#     print("press 1.yes 2.no")
#     choice=int(input())
#     if choice==1:
#         continue
#     else:
#         break
# print(l)

# l=[10,20,["abc","def","xyz"],40]
# print(l)
# print(len(l))
# print(l[3])
# print(l[2][2])

# l1=[10,20,["dale","sindhu",["bro","vishwa"],"ram"],30]
# print(l1)
# print(len(l1))
# print(l1[2][2][1])

#shallow copy
# l=[10,20,30,40,50]
# print(l)
# l1=l#shallow copy
# print(l)
# print(l1)
# l[2]=300
# print(l)
# print(l1)

#deep copy
# l=[10,20,30,40,50]
# print(l)
# l1=l.copy()#deep copy
# print(l)
# print(l1)
# l[2]=3000
# print(l)
# print(l1)

# l=["a","b",[10,20,30],"c"]
# l1=l.copy()
# print(l)
# print(l1)
# l[2][1]=200
# print(l)
# print(l1)

# l[1]="d"
# print(l)
# print(l1)

# import copy
# l=["a","b",[10,20,30],"c"]
# l1=copy.deepcopy(l)
# print(l)
# print(l1)
# l[2][1]=200
# print(l)
# print(l1)

# l[1]="d"
# print(l)
# print(l1)

#arithmetiuc operations on list
# l1=[1,2,3]
# l2=[4,5,6]
# l3=l1+l2
# print(l3)
# # l4=l1-l2
# # l5=l1*l2
# l6=l1*2
# print(l6)
# l7=l1/l2

#indexing and slicing
# l=[1,2,3,4,5,6,7,8,9]
# print(l)
# print(len(l))
# print(l[3])
# print(l[-2:-6])
# print(l[2:6])
# print(l[-3:-7:-1])
# print(l[::-1])
# print(l[::])
# print(l[::2])

#built in function of lists
# l=[1,2,3,4,5]
# print(len(l))
# print(any(l))
# print(all(l))
# print(sorted(l))

# l1=[1,2,0,3,4]
# print(any(l1))
# print(all(l1))
# print(sorted(l1))

# l2=[0,0,0,1,0]
# print(any(l2))
# print(all(l2))
# print(sorted(l2))

#enumerate function in list
# l=[10,20,30,40,50,60]
# for i,v in enumerate(l):
#     print(i,v)

#builtin methods
# l=[10,20,30]
# print(l)
# l.append(40)
# print(l)
# l.extend([50,60])
# print(l)
# l.insert(2,45)
# print(l)
# l.pop()
# print(l)
# l.remove(45)
# print(l)
# l.clear()
# print(l)
# del l
# print(l)

# #list comphrension
# l1=[1,2,3,4,5]
# l=[]
# # l2=[i for i in l1 if i%2==0]
# # print(l2)
# for i in l1:
#     if i%2==0:
#         l.append(i)
#     else:
#         pass
# print(l)

# l=list(range(10))
# print(l)
# l1=list(range(11,19))
# print(l1)

#interview questions
# l=[1,2,3,4,5]
# l1=[]
# for i in l:
#     l1.insert(0,i)
# print(l1)

# l1=[1,0,0,8,9,0,11,0,12]
# n=[]
# z=[]
# for i in l1:
#     if i==0:
#         z.append(i)
#     else:
#         n.append(i)
# print(n+z)


# nums=[1,0,0,8,9,0,11,0,12]
# l=0
# for r in range(len(nums)):
#     if nums[r]:
#         nums[l],nums[r]=nums[r],nums[l]
#         l+=1
# print(nums)


#rev a list
# l=[1,2,3,4,5]
# rev_l=[]
# for i in range(len(l)-1,-1,-1):
#     rev_l.append(l[i])
# print(rev_l)

#handle zeros put in last
# nums=[1,0,4,5,0,12,0,7,0,9]
# i=0
# for j in range(len(nums)):
#     if nums[j]:
#         nums[i],nums[j]=nums[j],nums[i]
#         i+=1
# print(nums)




# l1=[1,4,0,4,0,7,0,8,9,0,5,0]
# i=0
# for j in range(len(l1)):
#     if l1[j]:
#         l1[i],l1[j]=l1[j],l1[i]
#         i+=1
# print(l1)


#acheive deep copy in nested dictionarey
# import copy

# student={
#     'name':'abc',
#     'age':36,
#     'sports':{
#         'game1':'cricket',
#         'game2':'football'
#     }
# }

# print(student)
# s1=student.copy()#deep copy
# s2=copy.deepcopy(student)#nested deep copy in dict
# print(student)
# print(s1)
# print(s2)
# student['sports']['game3']='badminton'
# print(student)
# print(s1)
# print(s2)

# def even(num):
#     return num%2==0
# l=[1,2,3,4,5]
# res=list(filter(even,l))
# print(res)

def add(num):
    return num+10
l=[1,2,3,4,5]
res=list(map(add,l))
print(res)