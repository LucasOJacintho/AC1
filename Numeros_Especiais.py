n = int(input('Digite um valor igual ou maior que 2: '))

def eh_primo(n):
    c = (n-1)

    while (c>=2):
        if (n%c==0):
            break
        else:
            c-=1

    if c>=2:
        print ('Não é primo!')
        print ('Ele é divisível por: ', c)
        return False

    else:
        print ('É primo!')
        return True

if n>=2:
    eh_primo(n)
