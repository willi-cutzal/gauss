"""_summary_:
    encontrar factores para trinomios cuadrados.
"""


def divisible(n):
    """_summary_

    Args:
        n (_type_: int): al ingresar un valor, este será divido por su factores.
    
    Returns:
        mcd: lista de resultados
        fact: lista de factores
    """
    mcd = []
    fact = []
    for i in range(2, n+1):
        while n % i == 0:

            mcd.append(n)
            fact.append(i)
            n = n//i
    return mcd, fact
    
print(type(divisible(17017)))
