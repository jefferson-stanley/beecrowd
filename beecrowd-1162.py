def ordena_vagoes(vagoes, L):
    list_vagoes = []

    for elem in vagoes:
        list_vagoes.append(int(elem))

    swap = 0

    for i in range(L):
        for j in range(0, L - i - 1):
            temp = list_vagoes[j]

            if list_vagoes[j] > list_vagoes[j + 1]:
                list_vagoes[j] = list_vagoes[j + 1]
                list_vagoes[j + 1] = temp
                swap += 1

    return swap


def main():
    swaps = []
    num_testes = int(input())

    for _ in range(num_testes):
        L = int(input())
        vagoes = input().split()

        swaps.append(ordena_vagoes(vagoes, L))

    for elem in swaps:
        print(f'Optimal train swapping takes {elem} swaps.')


main()
