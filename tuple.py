# t=(10,20,30)
# print(t)
# print(type(t))
# t1=(10,"rama",1.5)
# print(t1)
# print(type(t1))
# t2=(10)
# print(t2)
# print(type(t2))
# t3=(10,)
# print(t3)
# print(type(t3))

# l=[10,20,30]
# print(l)
# l[1]=200
# print(l)

# t=(10,20,30)
# print(t)
# print(t[1])
# t[1]=100
# print(t)

#insertion and deletion in tuple
# t1=(10,20,30,40)
# print(t1)
# t2=t1[:2]+(25,)+t1[2:]
# print(t2)
# t3=t1[:2]+t1[2:]
# print(t3)

#zip function
# from itertools import zip_longest
# names=["virat","dhoni","gayle","rohith"]
# j_no=[18,7,333,45]
# country=["ind","ind"]
# ipl_team=["rcb","csk"]

# res=list(zip_longest(names,j_no,country,ipl_team,fillvalue="#"))
# print(res)


#list inside tuple
student_info=("vishwas",[78,87,95])
print(student_info)
name,marks=student_info
print(name)
print(marks)