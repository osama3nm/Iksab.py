import datetime
now = datetime.datetime.now()
print(now)
print(now.day)
print(now.month)
print(now.date())
bdate = datetime.date(1990, 1, 1)
print((now.date() - bdate).days)




list1= [1,5,4,10,8,9]
list2 = [10,1,5,9,8,10]
s1 = set(list1)
s2 = set(list2)
print(s1|s2)  # union
print(s1&s2)  # intersection
print(s1-s2)  # difference
print(s2-s1)  # difference


