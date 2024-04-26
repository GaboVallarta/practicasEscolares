
print("que quieres hacer?")
print("1. sumar")
print("2. restar")
print("3. dividir")
print("4. multiplicar")
print("5. elevar")


def elevar(a,b):
    r=a
    for i in range(1,b):
        r=r*a
    return r

print("elige")
x=int(input(""))
while True:
    if x==1:
        a=int(input("primer numero "))
        b=int(input("segundo numero "))

        print(a+b)
        break
    elif x==2:
        a=int(input("primer numero "))
        b=int(input("segundo numero "))

        print(a-b)
        break
    elif x==3:
        a=int(input("primer numero "))
        b=int(input("segundo numero "))

        print(a/b)
        break
    elif x==4:
        a=int(input("primer numero "))
        b=int(input("segundo numero "))

        print(a*b)
        break
    elif x==5:
        a=int(input("primer numero "))
        b=int(input("segundo numero "))
        print(elevar(a,b))
        break
    elif x==0:
        break
    else:
        print("no c puede")
