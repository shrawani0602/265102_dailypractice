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
