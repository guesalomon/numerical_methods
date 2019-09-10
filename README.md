#Numerical Methods
##Before executing the code:

It is necessary to have python installed, and also PIP. On the terminal of commands, type:

```
python -m pip install sympy
```

The command above installs "sympy" library for Python, as this code uses it for derivative and trigonometric calcuations.

##For executing the program:

You need to type the fields below to execute the program on terminal (on the same directory the code is in):
```
python m.py <method> <f> <a/x0> <b/x1> <eps> <fi(opt)>
```

Available methods: bis, pf, mil, nr, sec.
Relation of methods:
- bis: Bissection Method;
- pf: False Position Method (Regula Falsi);
- mil: Fixed Point Iteration Method;
- nr: Newton_Rhapson Method;
- sec: Secant Method;

Obs.:
- The last "fi" parameter will only be used for the Fixed Point Iteration Method;
- On the secant method, a and b are x_k-1 and x_k, respectively;

##Use cases:

Example of every described method solving x³-9x+3=0, ε=10⁻²:
```
python m.py mil x**3-9*x+3 0 1 0.01 '(x**3+3)/9'
python m.py sec x**3-9*x+3 0 1 0.01
python m.py bis x**3-9*x+3 0 1 0.01
python m.py pf x**3-9*x+3 0 1 0.01
python m.py nr x**3-9*x+3 0 1 0.01
```

PS.: When using parenthesis be sure to use single quotes around the whole formula. Exponentiation in Python is made by using double * (Ex.: a² equal to a**2).
