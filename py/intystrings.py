

def intastr(a=int):
    s=str(a)
    return s


def straint(s=str):
    a=int(s)
    return a


def asciiInt(a=int):
    a+=48
    return a



x=int(input("escribe el numero "))

print("el codigo es ",asciiInt(x))