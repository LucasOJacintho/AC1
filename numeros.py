# Programação Orientada a Objetos
# AC01 ADS-EaD - Números especiais
#
# Email Impacta: lucas.jacintho@aluno.faculdadeimpacta.com.br

lista = []
dicio = {}
armstrong = 0
respostas = []
respostas_armstrong = []


###########################################################
def eh_primo(n):
    if n >= 2:
        for number in range(n - 1, 0, -1):
            if n % number == 0 and n != 2:
                return False
            if number == 2 or n == 2:
                return True


###########################################################

def lista_primos(n):
    for contador in range(2, n + 1):
        if eh_primo(contador) == True:
            lista.append(contador)
    return lista


###########################################################

def conta_primos(s):
    for contador in range(0, len(s)):
        if eh_primo(s[contador]) == True:
            dicio[s[contador]] = 0
    for contador in range(0, len(s), 1):
        if eh_primo(s[contador]) == True:
            dicio[s[contador]] += 1

    return dicio


###########################################################

def eh_armstrong(n):
    if n >= 0:
        num = str(n)
        global armstrong
        armstrong = 0
        lista = []

        for contador in range(0, len(num)):
            lista.append(int(num[contador]))
            armstrong += lista[contador] ** len(num)

        num = int(num)
        if num != armstrong:
            return False
        else:
            return True


###########################################################

def eh_quase_armstrong(n):
    eh_armstrong(n)
    if armstrong == n:
        return False
    elif armstrong + 1 == n or armstrong - 1 == n:
        return True


###########################################################

def lista_armstrong(n):
    for contador in range(0, n + 1):
        if eh_armstrong(contador) == True:
            respostas_armstrong.append(contador)
    return respostas_armstrong


###########################################################

def eh_perfeito(n):
    if n >= 2:
        for contador in range(1, n):
            if n % (contador) == 0:
                lista.append(contador)
        if sum(lista) == n:
            lista.clear()
            return True
        else:
            lista.clear()
            return False


###########################################################

def lista_perfeitos(n):
    if n >= 2 and n <= 1000:
        for contador in range(0, n + 1):
            if eh_perfeito(contador) == True:
                respostas.append(contador)
        return respostas
