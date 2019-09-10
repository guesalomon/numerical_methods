from __future__ import print_function
import numpy as np
import sys
from sympy import *
import numpy as np

def nr(a,b,e,func,y):
    f = lambdify(y, func, 'numpy')
    df = lambdify(y, func.diff(y), 'numpy')
    i = 1
    x_old = (a+b)/2.0
    mat = []
    mat.append(" i |   x    | |xi-x|  | fi(x) | |f(x)| ")
    while True:
        x = x_old - (f(x_old)/df(x_old))
        it = [i,x_old,abs(x_old-x),x,abs(f(x_old))]
        x_old=x
        i+=1
        mat.append(it)
        if (it[-1]<e):
            break
    return mat

def sec(xk,xkum,e,func,y):
    f = lambdify(y, func, 'numpy')
    x_old2 = xk
    x_old = xkum
    mat = []
    mat.append(" i |   x    | |xi-x| |  |f(x)|")
    mat.append([1,xk,0,abs(f(xk))])
    mat.append([2,xkum,0,abs(f(xkum))])
    i = 3
    while True:
        x = (x_old2*f(x_old) - x_old*f(x_old2))/(f(x_old) - f(x_old2))
        it = [i,x,abs(x_old-x),abs(f(x))]
        x_old2 = x_old
        x_old = x
        i+=1
        mat.append(it)
        if (it[-1]<e):
            break
    return mat

def mil(a,b,e,func,y, fif):
    f = lambdify(y, func, 'numpy')
    fi = lambdify(y, fif, 'numpy')
    i = 1
    x_old = (a+b)/2.0
    mat = []
    mat.append(" i |   x    | |xi-x|  | fi(x) | |f(x)| ")
    while True:
        x = fi(x_old)
        it = [i,x_old,abs(x_old-x),x,abs(f(x_old))]
        x_old=x
        i+=1
        mat.append(it)
        if (it[-1]<e):
            break
    return mat

def bis(a,b,e,func,y):
    f = lambdify(y, func, 'numpy')
    i = 1
    mat = []
    mat.append(" i |   a   |    b   |   f(a)  |   f(b)  |    x    |   f(x)  | |f(x)|")
    while True:
        x = (a+b)/2.0
        it = [i,a,b,f(a),f(b),x,f(x),abs(f(x))]
        i+=1
        if f(a)*f(x) < 0:
            b = x
        else:
            a = x
        mat.append(it)
        if (abs(f(x))<e):
            break
    return mat

def pf(a,b,e,func,y):
    f = lambdify(y, func, 'numpy')
    i = 1
    mat = []
    mat.append(" i |   a   |    b   |   f(a)  |   f(b)  |    x    |   f(x)  | |f(x)|")
    while True:
        x = (a*f(b)-b*f(a))/(f(b)-f(a))
        it = [i,a,b,f(a),f(b),x,f(x),abs(f(x))]
        i+=1
        if f(a)*f(x) < 0:
            b = x
        else:
            a = x
        mat.append(it)
        if (abs(f(x))<e):
            break
    return mat

def imprime(res):
    print ("-"*len(res[0]))
    print (res[0])
    print ("-"*len(res[0]))
    for el in res[1:]:
        print ("%2d " % el[0], end="")
        for el2 in el[1:]:
            print("| %.4f " % el2, end="")
        print("\n", end="")
        print("-"*len(res[0]))


if len(sys.argv) < 5:
    print("Use da forma: \n #python m.py <metodo> <f> <a/x0> <b/x1> <eps> <fi(opt)>")
    print("Metodos disponiveis: bis (bissecao), pf (posicao falsa), mil, nr, sec. ")
    exit()

x = Symbol('x')
func = eval(str(sys.argv[2]))
a = float(sys.argv[3])
b = float(sys.argv[4])
e = float(sys.argv[5])
if (sys.argv[1]=='mil'):
    fi =  eval(str(sys.argv[6]))
    res = eval(str(sys.argv[1])+"(a,b,e,func,x,fi)")
else:
    res = eval(str(sys.argv[1])+"(a,b,e,func,x)")
#res = nr(a,b,e,func,x)

imprime(res)

