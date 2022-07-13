import multiprocessing

"""
Processos x Threads

Multiprocessamento para melhorar o desenpenho de resposta do Python e driblar o 
GIL para nao cair em Lock nas threads 
"""
print(f'Iniciando o processo com o nome: {multiprocessing.current_process().name}')


def faz_algo(valor):
    print(f'Fazendo algo com o {valor}')


def main():
    pc = multiprocessing.Process(target=faz_algo, args=('Passaro',), name='Processo Geek')

    print(f'Iniciando o processo com o nome: {pc.name}')

    pc.start()
    pc.join()


if __name__ == '__main__':
    main()
