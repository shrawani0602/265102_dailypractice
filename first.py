print("hello world")
print(24*7)

week_days = 7
day_hours = 24
week_hours = week_days * day_hours
print(week_hours)

print(week_days,day_hours,week_hours)

#to run shell py -3.8  to exit: exit()

#data types
print("******DATA TYPES*****")
a = 10
b = "abc"
c = 12.5
print(a+a)
print(b+b)
print(c+c)
#print(a+b) error int+str not possible
print(a+c)
#print(b+c) error

#LIST

l=[12,13,45]
print(l)

k=list(range(1,10))
print(k)

k=list(range(1,10,3))
print(k)

#k=list[1,12.3,"shd"] error different data type
#print(k)
#RANGE
#list(range(1,10)) - [1,2,3,4,5,6,7,8,9]  list(range(1,10,2))-[1,3,5,7,9]

l=[12,45.5,"tftyf"]
print(l)
#dir(list) will display all the things that can be done in list
#dir(__builtins__)

name1="abc"
age=20
is_new=True
print(name1)
print(age)
print(is_new)

name2=input("what is your name? ")
color=input("your favourite color? ")
print(name2 + " likes "+ color +" color.")

pound=float(input("weight in pound?"))
kilo=pound*0.454
print(kilo)

print("pytho's for beginner.")
print('python for "beginner".')

course=''' hey
this is shrawani
welcome to
python course.'''

course="python for begineers"
print("1"+course[0:7])
print("2"+course[0:])
print("3"+course[4:10])
print("4"+course[-6:-1])
print("5"+course[-1:-6])
print("6"+course[:-1])
print("7"+course[-1:-6:-2])

print("7"+course[-5])
another=course[:]
print(another)
print("8"+course[1:-1])

#formated strings
first="shrawani"
last="singh"
print(f"{first} {last} is a coder.")

#strings
course2="Python for beginners."
print(len(course2))
print(course2.upper())
print(course2.lower())
############print(course.find("P"))
###########print(course2.replace("beginners ", "advanced"))
print(course2.title())

print(10*3)
print(10/3)
print(10//3)
print(10**3)
