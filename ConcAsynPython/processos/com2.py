"""
Uso de Queue como comunicacao entre processo, pode ser realizado o controle de unlock e
lock na comunicacao.

Ou seja enquanto estiver executando um processo o outro tem que aguardar ate
o mesmo finalizar.
"""

import multiprocessing


def ping(queue):
    queue.send('Geek')


def pong(queue):
    msg = queue.recv()
    print(f'{msg} University')


def main():
    queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=ping, args=(queue,))
    p2 = multiprocessing.Process(target=pong, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
