import math
x=2.9
print(round(x))
print(abs(x))
print(math.ceil(x))

is_hot=False
is_cold=False
if is_hot:
    print("hot day")
elif is_cold:
    print("cold day")
else:
    print("normal day")

price=1000000
has_good_credit=False
if has_good_credit:
    down_payment=0.1*price
else:
    down_payment=0.2*price
print(f"DOWNPAYMENT : {down_payment}")

name=input("enter name : ")
l=len(name)
if l<3:
    print("less")
elif l>50:
    print("too large")
else:
    print("alright")

w=int(input("enter weight:"))
u=input("L(bs) or K(g) :")
u=u.upper()
if(u=="K"):
    print(f"weight in pound {w//0.454} pounds")
else:
    print(f"weight in kilogram {w*0.454} kg")

i=0
while(i<=5):
    print(i*"*")
    i=i+1
print("done")

#guess game
secret_count=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input("guess:"))
    guess_count=guess_count+1
    if guess==secret_count:
        print("won")
        break
    else:
        print("lost")

price=[10,34,32]
s=0
for i in price:
    s=s+i
print(s)
i=0
for i in range(20):
    print(i)
for i in range(5,20):
    print(i)
for i in range(5,20,3):
    print(i)

#nested loop
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

n=[5,2,5,2,2]
for i in n:
    print(i*"*")

l=0
list=[12,34,667,445,334]
for i in list:
    if l<i:
        l=i
print(l)
