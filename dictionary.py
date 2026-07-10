# student={'name':"abc",
#           'age':23,
#           'address':"AP"}
# print(student)

# emp={'name':'abc',
#       'age':40,
#       'sal':15000}
# print(emp)
# emp['exp']=3
# print(emp['age'])
# for i in emp:
#     print(i)
# for i in emp:
#     print(emp[i])

# #builtin function
# for i in emp.keys():
#     print(i)
# for i in emp.values():
#     print(i)
# for i in emp.items():
#     print(i)   

# student={'name':'abhi',
#          'age':23,
#         'phno':{'mob':158448545,'ll':55658656},
#         'address':{'res':'banglore','per':'gulbarga'}
#         }
# print(student)
# print(student['name'])
# print(student['phno']['mob'])
# print(student['address']['per'])

# cricketer={
#     'name':'dhoni',
#     'age':43
# }
# print(cricketer)
# c1=cricketer
# c2=cricketer.copy()
# print(c1)
# print(c2)
# print(cricketer)
# cricketer['age']=44
# print(cricketer)
# print(c1)
# print(c2)

#deep copy in nesteed dict
# import copy
# heroine={
#     'name':'samantha',
#     'age':36,
#     'bf':{'name1':'rahul',
#           'name2':'nehru'}
# }
# print(heroine)
# h1=heroine.copy()#deep copy
# h2=copy.deepcopy(heroine)#deep copy nested
# print(heroine)
# print(h1)
# print(h2)
# heroine['bf']['name3']='pavan'
# print(heroine)
# print(h1)
# print(h2)

#zip function
id=[101,102,103,104]
name=['nagu','badhri','krishna','rukmini']
res1=dict(zip(id,name))
print(res1)

mob=[95,63,79,143]
addr=['thailand','nigeria','russia','india']
# res2=dict(zip(id,name,mob,addr))
# print(res2)

data=list(zip(name,mob,addr))
info=dict(zip(id,data))
print(info)