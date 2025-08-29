def retorna_termos(entrada):
    termos = []
    operador = '/'

    for elem in entrada:
        if elem == '*' or elem == '+' or elem == '-':
            operador = elem
        elif elem.isdigit():
            termos.append(int(elem))

    n1, d1, n2, d2 = termos[0], termos[1], termos[2], termos[3]

    return n1, d1, n2, d2, operador

def operacao(n1, d1, n2, d2, operador):
    numerador = n1 * d2
    denominador = d1 * d2

    if operador == '+':
        numerador += n2 * d1
    if operador == '-':
        numerador -= n2 * d1
    if operador == '*':
        numerador = n1 * n2
    if operador == '/':
        denominador = n2 * d1

    return numerador, denominador

def simplificador(numerador, denominador):
    maior, menor = numerador, denominador
    if maior < menor:
        maior, menor = denominador, numerador

    num_simp = den_simp = 0

    for i in range(abs(menor), 0, -1):
        if numerador % i == 0 and denominador % i == 0:
            num_simp = numerador / i
            den_simp = denominador / i
            break

    return num_simp, den_simp

def main():
    num_casos = int(input())

    for _ in range(num_casos):
        entrada = input().split()

        n1, d1, n2, d2, op = retorna_termos(entrada)
        num, den = operacao(n1, d1, n2, d2, op)
        num_simp, den_simp = simplificador(num, den)

        print(f'{num}/{den} = {num_simp:.0f}/{den_simp:.0f}')

main()
