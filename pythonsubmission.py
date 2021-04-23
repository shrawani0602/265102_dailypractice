#merge 2 dictionary
dict1={"1":"abc","2":"def","3":"ghi"}
dict2={"k":"lmn","o":"pqr"}
merge=dict2.update(dict1)
print(dict2)

#convert list into nested dictionary
list1=[134,89,87,99,454]
dict3=temp={}

for i in list1:
    temp[i]={}
    temp=temp[i]
print(dict3)

#to get the next



#input abbrevation
str=input("enter abbrivation:")
if str=="lol":
    print("laughing out loudly")
elif str=="rofl":
    print("rolling on the floor laughing")
elif str=="lmk":
    print("let me know")
elif str=="smh":
    print("shaking my hand")
else :
    print("out of range")

#pizza price
pizza=int(input("Choice"))
if(pizza%2 == 0):
    total=pizza*120
    print(f"total : {total}")
else:
    total=pizza*123
    print(f"total : {total}")
    
    

#complex number
data=int(input("type of data of number :"))
if(data=="0"):
    print("ZERO")
else:
    print(type(data))
    
    
    
#next date
year = int(input("Input a year: "))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


day = int(input("Input a day [1-31]: "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))



#second smallest no. in list
list=[234,45,67,89,223,227,45]
k=sorted(set(list))
print(k[1])



#change position n with n+1
def position(list4, n):
    output= []

    for i in range(len(list4)-n, len(list4)):
        output.append(list4[i])
    for i in range(0, len(list4) - n):
        output.append(list4[i])
    return output

num = 1
list5 = [1, 2, 3, 4, 5, 6]
k=sorted(set(list))
print(k[1])


#max and minimum in set
s=set([1,2,345,5678,8990])
print(max(s))
print(min(s))

#repeated item in tuple
t=2,3,45,3,3,45,6,7,8,6,78,56,90
for i in t:
    l=[]
    if t.count(i)>1:
        print(i)
