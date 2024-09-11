import math
import os
import textwrap
from pathlib import Path

ROOT_PATH = Path(os.getcwd())
PI = 3.14


def menu():
    menu = """\n
    ================ MENU ================
    [v]\tCalcular Volume
    [m]\tCalcular Media
    [d]\tCalcular Desvio Padrão
    
    [c]\tLimpar TXT

    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def calcular_volume_cilindro():
    h = float(input("Insira a altura: "))
    d = float(input("Insira o diametro: "))

    v = (PI / 4) * (d * d) * h
    print(f"Volume: {v}")

    with open(ROOT_PATH / "historicoCilindro.txt", "a") as arquivo:
        arquivo.write(f"Altura :{h}\tDiametro :{d}\tVolume :{v}\n")


def ler_dados():
    alturas = []
    diametros = []
    volumes = []

    # Abrir o arquivo de histórico
    with open(ROOT_PATH / "historicoCilindro.txt", "r") as arquivo:
        for linha in arquivo:

            # Ignorar linhas que contêm "Media" ou "Desvio"
            if "Media" in linha or "Desvio" in linha:
                continue

            # Separar os campos da linha
            partes = linha.split("\t")

            # Extrair altura, diâmetro e volume
            altura_str = partes[0].split(":")[1].strip()
            diametro_str = partes[1].split(":")[1].strip()
            volume_str = partes[2].split(":")[1].strip()

            # Converter strings para float e adicionar às respectivas listas
            alturas.append(float(altura_str))
            diametros.append(float(diametro_str))
            volumes.append(float(volume_str))

    return alturas, diametros, volumes


def calcular_media(tipo_media):
    alturas, diametros, volumes = ler_dados()

    if tipo_media == "altura":
        return sum(alturas) / len(alturas) if alturas else 0
    elif tipo_media == "diametro":
        return sum(diametros) / len(diametros) if diametros else 0
    elif tipo_media == "volume":
        return sum(volumes) / len(volumes) if volumes else 0
    else:
        return "Opção inválida!"


def calcular_media_menu():
    print("\nEscolha qual média deseja calcular:")
    print("1 - Altura")
    print("2 - Diâmetro")
    print("3 - Volume")

    opcao = input("Digite o número da opção: ")

    if opcao in ["1", "2", "3"]:
        # Calcular todas as médias
        media_altura = calcular_media("altura")
        media_diametro = calcular_media("diametro")
        media_volume = calcular_media("volume")

        # Salvar todas as médias no arquivo
        with open(ROOT_PATH / "historicoCilindro.txt", "a") as arquivo:
            arquivo.write(
                f"Media Altura :{media_altura}\tMedia Diametro :{media_diametro}\tMedia Volume :{media_volume}\n"
            )

        # Mostrar a média escolhida pelo usuário
        if opcao == "1":
            print(f"Média das alturas: {media_altura}")
        elif opcao == "2":
            print(f"Média dos diâmetros: {media_diametro}")
        elif opcao == "3":
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


def calcular_desvios_padrao():
    alturas, diametros, volumes = ler_dados()

    desvio_padrao_altura = calcular_desvio_padrao(alturas)
    desvio_padrao_diametro = calcular_desvio_padrao(diametros)
    desvio_padrao_volume = calcular_desvio_padrao(volumes)

    print(f"Desvio padrão das alturas: {desvio_padrao_altura}")
    print(f"Desvio padrão dos diâmetros: {desvio_padrao_diametro}")
    print(f"Desvio padrão dos volumes: {desvio_padrao_volume}")

    with open(ROOT_PATH / "historicoCilindro.txt", "a") as arquivo:
        arquivo.write(
            f"Desvio padrão Altura: {desvio_padrao_altura}\t"
            f"Desvio padrão Diâmetro: {desvio_padrao_diametro}\t"
            f"Desvio padrão Volume: {desvio_padrao_volume}\n"
        )


def clean_txt():
    confirmacao = input("Tem certeza que deseja limpar o arquivo (S/N)? ").lower()
    if confirmacao == "s":
        open(ROOT_PATH / "historicoCilindro.txt", "w").close()
        print("Arquivo limpo com sucesso!")
    else:
        print("Operação cancelada.")


def main():
    while True:
        opcao = menu()

        if opcao == "v":
            calcular_volume_cilindro()
        elif opcao == "m":
            calcular_media_menu()

        elif opcao == "d":
            calcular_desvios_padrao()

        elif opcao == "c":
            clean_txt()

        elif opcao == "q":
            break
        else:
            print("Insira uma opção válida!")


if __name__ == "__main__":
    main()
