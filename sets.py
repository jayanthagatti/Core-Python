# s1={1,2,3,4,5,6,7}
# print(s1)
# print(type(s1))

# s2={1,2,3,1,2,5,6}
# print(s2)
# s3={}
# print(type(s3))

# s5={10,20,30,40}
# print(s5[0])
# print(s5[:3])

# a=set()
# for i in range(5):
#     print("enter a num")
#     data=int(input())
#     a.add(data)
# print(a)
# a.update([60,70,80])
# print(a)
# a.discard(70)
# print(a)

# s={10,20,30,40}
# for i,j in enumerate(s):
#     print(i,j)

#union and intersection
# s1={1,2,3,4}
# s2={3,4,5,6}
# s3=s1.union(s2)
# print(s3)

# s4=s1.intersection(s2)
# print(s4)

# s5=s1.difference(s2)
# print(s5)
# s6=s2.difference(s1)
# print(s6)
# s7=s1.symmetric_difference(s2)
# print(s7)

#subset and superset
# s1={1,2,3,4}
# s2={1,2}
# print(s1.issubset(s2))
# print(s1.issuperset(s2))
# print(s2.issuperset(s1))
# print(s2.issubset(s1))

#disjoint set
# s1={1,2,3,4}
# s2={3,4,5,6}
# s3={5,6,7,8}
# print(s1.isdisjoint(s2))
# print(s2.isdisjoint(s3))
# print(s1.isdisjoint(s3))

#frozenset
# s1={1,2,3,4}
# s2=frozenset([10,20,30,40])
# print(s1)
# print(s2)
# s1.add(5)
# print(s1)
# s2.add(50)
# print(s2)

# s1={1,2,3,[4,5,6],7}
# print(s1)

s2={1,2,3,(4,5,6),7}
print(s2)

# s1={1,2,3,{4,5,6},7}
# print(s1)

t=(10,20,("nagu","bro"),30)
print(t)
print(t[3])
print(t[2][1])
