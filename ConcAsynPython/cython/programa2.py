import datetime
import computa


def main():
    print('Realizando o processamento matematico com CPython')

    inicio = datetime.datetime.now()
    computa.computar(fim=50_000_000)
    tempo = datetime.datetime.now() - inicio

    print(f'Terminou em {tempo.total_seconds():2.f} segundos.')


if __name__ == '__main__':
    main()
