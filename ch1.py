def rast(func):
    def in_f(U0,Ux,t):
        return U0*t + (func(U0,Ux,t) * t**2)/2
    return in_f




def uscor(U0,Ux,t):
    return ((Ux - U0)/t)
uscor = rast(uscor)
U0 = int(input())
Ux = int(input())
t = int(input())
print(uscor(U0,Ux,t))

