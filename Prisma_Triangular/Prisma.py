import math
import os
import textwrap
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

ROOT_PATH = Path(os.getcwd())


def menu():
    menu = """\n
    ================ MENU ================
    [v]\tCalcular Volume do Prisma
    [m]\tCalcular Média
    [d]\tCalcular Desvio Padrão
    [g]\tGerar Gráfico de Distribuição Normal
    [c]\tLimpar TXT

    [q]\tSair
    => """

    return input(textwrap.dedent(menu))


def calcular_volume_prisma():
    h = float(input("Insira a altura do prisma: "))
    b = float(input("Insira a base do triângulo: "))
    c = float(input("Insira o comprimento do prisma: "))

    v = (b * h * c) / 2
    print(f"Volume do prisma triangular: {v}")

    with open(ROOT_PATH / "historicoPrisma.txt", "a") as arquivo:
        arquivo.write(f"Altura :{h}\tBase :{b}\tComprimento :{c}\tVolume :{v}\n")


def ler_dados():
    alturas = []
    bases = []
    comprimentos = []
    volumes = []

    # Abrir o arquivo de histórico
    with open(ROOT_PATH / "historicoPrisma.txt", "r") as arquivo:
        for linha in arquivo:
            # Ignorar linhas que contêm "Media" ou "Desvio"
            if "Media" in linha or "Desvio" in linha:
                continue

            # Separar os campos da linha
            partes = linha.split("\t")

            # Extrair altura, base, comprimento e volume
            altura_str = partes[0].split(":")[1].strip()
            base_str = partes[1].split(":")[1].strip()
            comprimento_str = partes[2].split(":")[1].strip()
            volume_str = partes[3].split(":")[1].strip()

            # Converter strings para float e adicionar às respectivas listas
            alturas.append(float(altura_str))
            bases.append(float(base_str))
            comprimentos.append(float(comprimento_str))
            volumes.append(float(volume_str))

    return alturas, bases, comprimentos, volumes


def calcular_media_prisma(tipo_media):
    alturas, bases, comprimentos, volumes = ler_dados()

    if tipo_media == "altura":
        return sum(alturas) / len(alturas) if alturas else 0
    elif tipo_media == "base":
        return sum(bases) / len(bases) if bases else 0
    elif tipo_media == "comprimento":
        return sum(comprimentos) / len(comprimentos) if comprimentos else 0
    elif tipo_media == "volume":
        return sum(volumes) / len(volumes) if volumes else 0
    else:
        return "Opção inválida!"


def calcular_media_menu():
    print("\nEscolha qual média deseja calcular:")
    print("1 - Altura")
    print("2 - Base")
    print("3 - Comprimento")
    print("4 - Volume")

    opcao = input("Digite o número da opção: ")

    if opcao in ["1", "2", "3", "4"]:
        # Calcular todas as médias
        media_altura = calcular_media_prisma("altura")
        media_base = calcular_media_prisma("base")
        media_comprimento = calcular_media_prisma("comprimento")
        media_volume = calcular_media_prisma("volume")

        # Salvar todas as médias no arquivo
        with open(ROOT_PATH / "historicoPrisma.txt", "a") as arquivo:
            arquivo.write(
                f"Media Altura :{media_altura}\tMedia Base :{media_base}\tMedia Comprimento :{media_comprimento}\tMedia Volume :{media_volume}\n"
            )

        # Mostrar a média escolhida pelo usuário
        if opcao == "1":
            print(f"Média das alturas: {media_altura}")
        elif opcao == "2":
            print(f"Média das bases: {media_base}")
        elif opcao == "3":
            print(f"Média dos comprimentos: {media_comprimento}")
        elif opcao == "4":
            print(f"Média dos volumes: {media_volume}")
    else:
        print("Opção inválida!")


def calcular_desvio_padrao(valores):
    if len(valores) < 2:
        return 0  # Não é possível calcular desvio padrão para menos de 2 valores

    media = sum(valores) / len(valores)
    soma_quadrados = sum((x - media) ** 2 for x in valores)
    variancia = soma_quadrados / (len(valores) - 1)  # n-1 para amostral
    return math.sqrt(variancia)


def calcular_desvios_padrao_prisma():
    alturas, bases, comprimentos, volumes = ler_dados()

    desvio_padrao_altura = calcular_desvio_padrao(alturas)
    desvio_padrao_base = calcular_desvio_padrao(bases)
    desvio_padrao_comprimento = calcular_desvio_padrao(comprimentos)
    desvio_padrao_volume = calcular_desvio_padrao(volumes)

    print(f"Desvio padrão das alturas: {desvio_padrao_altura}")
    print(f"Desvio padrão das bases: {desvio_padrao_base}")
    print(f"Desvio padrão dos comprimentos: {desvio_padrao_comprimento}")
    print(f"Desvio padrão dos volumes: {desvio_padrao_volume}")

    with open(ROOT_PATH / "historicoPrisma.txt", "a") as arquivo:
        arquivo.write(
            f"Desvio padrão Altura: {desvio_padrao_altura}\t"
            f"Desvio padrão Base: {desvio_padrao_base}\t"
            f"Desvio padrão Comprimento: {desvio_padrao_comprimento}\t"
            f"Desvio padrão Volume: {desvio_padrao_volume}\n"
        )


def gerar_grafico_distribuicao_normal(volumes):
    # Calcula a média e o desvio padrão dos volumes
    media = np.mean(volumes)
    desvio_padrao = np.std(volumes)

    # Cria os dados para o gráfico de distribuição normal
    x = np.linspace(min(volumes), max(volumes), 100)
    y = norm.pdf(x, media, desvio_padrao)

    # Plota o gráfico
    plt.plot(x, y, label="Distribuição Normal")
    plt.hist(volumes, bins=10, density=True, alpha=0.6, color="b", label="Volumes")

    # Adiciona título e labels
    plt.title("Distribuição Normal dos Volumes do Prisma")
    plt.xlabel("Volume")
    plt.ylabel("Frequência")

    # Exibe a legenda
    plt.legend()

    # Mostra o gráfico
    plt.show()


def clean_txt():
    confirmacao = input("Tem certeza que deseja limpar o arquivo (S/N)? ").lower()
    if confirmacao == "s":
        open(ROOT_PATH / "historicoPrisma.txt", "w").close()
        print("Arquivo limpo com sucesso!")
    else:
        print("Operação cancelada.")


def main():
    while True:
        opcao = menu()

        if opcao == "v":
            calcular_volume_prisma()

        elif opcao == "m":
            calcular_media_menu()

        elif opcao == "d":
            calcular_desvios_padrao_prisma()

        elif opcao == "g":
            alturas, bases, comprimentos, volumes = ler_dados()
            if volumes:
                gerar_grafico_distribuicao_normal(volumes)
            else:
                print("Não há volumes suficientes para gerar o gráfico.")

        elif opcao == "c":
            clean_txt()

        elif opcao == "q":
            break

        else:
            print("Insira uma opção válida!")


if __name__ == "__main__":
    main()
