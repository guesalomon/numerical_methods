_________________________________________________________________

Antes de rodar o programa:
_________________________________________________________________

Necessita-se de Python instalado e PIP também. No terminal execute:

    #python -m pip install sympy

O comando acima instala a biblioteca "sympy" utilizada para derivações em python e funções trigonométricas.

_________________________________________________________________

Para executar o programa:
_________________________________________________________________

Para executar, basta informar os seguintes campos abaixo no terminal, no mesmo diretório que se encontrar o executável:

    #python m.py <metodo> <f> <a/x0> <b/x1> <eps> <fi(opt)>

Metodos disponiveis: bis, pf (posicao falsa), mil, nr, sec. 

Obs.:
i) O ultimo parametro fi sera utilizado somente para o metodo MIL (Iteracao Linear);
ii) No metodo da secante a e b são x_k-1 e x_k, respectivamente;

_________________________________________________________________

Exemplos de uso:
_________________________________________________________________

Exemplo de cada metodo para x³-9x+3=0, ε=10⁻²:

    #python m.py mil x**3-9*x+3 0 1 0.01 '(x**3+3)/9'
    #python m.py sec x**3-9*x+3 0 1 0.01
    #python m.py bis x**3-9*x+3 0 1 0.01 
    #python m.py pf x**3-9*x+3 0 1 0.01 
    #python m.py nr x**3-9*x+3 0 1 0.01

