# Programas para Cálculo de Volume, Média e Desvio Padrão

Estes programas foram desenvolvidos para auxiliar em uma atividade acadêmica de física que envolvia a medição e análise de desvios padrão de várias medidas de cilindros e prismas. 

# Calculador de Volume de Cilindro com Análise Estatística

Este programa foi desenvolvido para calcular o volume de um cilindro e realizar análises estatísticas sobre as medidas coletadas, incluindo médias e desvios padrão. O programa salva os cálculos e análises em um arquivo de texto e permite ao usuário realizar diversas operações através de um menu interativo.

## Funcionalidades

1. **Calcular o Volume de um Cilindro**: Insira a altura e o diâmetro para calcular o volume e salvar no histórico.
2. **Calcular Médias**: Calcule a média das alturas, diâmetros e volumes.
3. **Calcular Desvios Padrão**: Calcule o desvio padrão das alturas, diâmetros e volumes.
4. **Limpar Histórico**: Apague o conteúdo do arquivo de histórico.
5. **Sair do Programa**: Encerre a execução do programa.

## Arquivo de Histórico

O arquivo `historicoCilindro.txt` é utilizado para armazenar:
- Dados dos cálculos de volume.
- Médias das alturas, diâmetros e volumes.
- Desvios padrão das alturas, diâmetros e volumes.

## Como Utilizar

1. **Clone o Repositorio**
    ```sh
    git clone https://github.com/rickrocca/Fisica.git
    ```
2. **Navegue até o diretório do projeto**
    ```sh
    cd Fisica/Cilindro
    ```

3. **Executar o Programa**: Execute o script Python utilizando o seguinte comando:
    ```bash
    python Cilindro.py
    ```

4. **Menu de Opções**: O programa oferece um menu interativo com as seguintes opções:
    - `[v]` - Calcular Volume: Solicita a altura e o diâmetro do cilindro, calcula o volume e salva no arquivo de histórico.
    - `[m]` - Calcular Média: Permite escolher entre calcular a média das alturas, diâmetros ou volumes.
    - `[d]` - Calcular Desvio Padrão: Calcula e exibe o desvio padrão das alturas, diâmetros e volumes.
    - `[c]` - Limpar TXT: Limpa o conteúdo do arquivo de histórico após confirmação.
    - `[q]` - Sair: Encerra o programa.

## Funções Principais

### `calcular_volume_cilindro()`
Calcula o volume do cilindro com base na altura e diâmetro fornecidos e salva no arquivo `historicoCilindro.txt`.

### `ler_dados()`
Lê os dados do arquivo `historicoCilindro.txt`, ignorando linhas que contêm "Media" ou "Desvio", e retorna listas com alturas, diâmetros e volumes.

### `calcular_media(tipo_media)`
Calcula a média das medidas especificadas (altura, diâmetro ou volume).

### `calcular_media_menu()`
Permite ao usuário escolher qual média calcular (altura, diâmetro ou volume), calcula e exibe a média selecionada, e salva todas as médias no arquivo de histórico.

### `calcular_desvio_padrao(valores)`
Calcula o desvio padrão para uma lista de valores fornecidos.

### `calcular_desvios_padrao()`
Calcula e exibe o desvio padrão das alturas, diâmetros e volumes, e salva no arquivo de histórico.

### `clean_txt()`
Limpa o conteúdo do arquivo `historicoCilindro.txt` após confirmação do usuário.

## Requisitos

- Python 3.x

## Exemplo de Execução

Ao executar o programa, o menu será exibido. Você pode selecionar uma das opções digitando a letra correspondente e seguindo as instruções fornecidas.

# Calculador de Volume de Prisma com Análise Estatística

Este programa foi desenvolvido para calcular o volume de um prisma triangular e realizar análises estatísticas sobre as medidas coletadas, incluindo médias e desvios padrão. O programa salva os cálculos e análises em um arquivo de texto e permite ao usuário realizar diversas operações através de um menu interativo.

## Funcionalidades

1. **Calcular o Volume de um Prisma Triangular**: Insira a altura, a base do triângulo e o comprimento do prisma para calcular o volume e salvar no histórico.
2. **Calcular Médias**: Calcule a média das alturas, bases, comprimentos e volumes.
3. **Calcular Desvios Padrão**: Calcule o desvio padrão das alturas, bases, comprimentos e volumes.
4. **Limpar Histórico**: Apague o conteúdo do arquivo de histórico.
5. **Sair do Programa**: Encerre a execução do programa.

## Arquivo de Histórico

O arquivo `historicoPrisma.txt` é utilizado para armazenar:
- Dados dos cálculos de volume.
- Médias das alturas, bases, comprimentos e volumes.
- Desvios padrão das alturas, bases, comprimentos e volumes.

## Como Utilizar
1. **Clone o Repositorio**
    ```sh
    git clone https://github.com/rickrocca/Fisica.git
    ```
2. **Navegue até o diretório do projeto**
    ```sh
    cd Fisica/Prisma_Triangular
    ```
3. **Executar o Programa**: Execute o script Python utilizando o seguinte comando:
    ```bash
    python Prisma.py
    ```

4. **Menu de Opções**: O programa oferece um menu interativo com as seguintes opções:
    - `[v]` - Calcular Volume do Prisma: Solicita a altura, a base e o comprimento do prisma, calcula o volume e salva no arquivo de histórico.
    - `[m]` - Calcular Média: Permite escolher entre calcular a média das alturas, bases, comprimentos ou volumes.
    - `[d]` - Calcular Desvio Padrão: Calcula e exibe o desvio padrão das alturas, bases, comprimentos e volumes.
    - `[c]` - Limpar TXT: Limpa o conteúdo do arquivo de histórico após confirmação.
    - `[q]` - Sair: Encerra o programa.

## Funções Principais

### `calcular_volume_prisma()`
Calcula o volume do prisma triangular com base na altura, base e comprimento fornecidos e salva no arquivo `historicoPrisma.txt`.

### `ler_dados()`
Lê os dados do arquivo `historicoPrisma.txt`, ignorando linhas que contêm "Media" ou "Desvio", e retorna listas com alturas, bases, comprimentos e volumes.

### `calcular_media_prisma(tipo_media)`
Calcula a média das medidas especificadas (altura, base, comprimento ou volume).

### `calcular_media_menu()`
Permite ao usuário escolher qual média calcular (altura, base, comprimento ou volume), calcula e exibe a média selecionada, e salva todas as médias no arquivo de histórico.

### `calcular_desvio_padrao(valores)`
Calcula o desvio padrão para uma lista de valores fornecidos.

### `calcular_desvios_padrao_prisma()`
Calcula e exibe o desvio padrão das alturas, bases, comprimentos e volumes, e salva no arquivo de histórico.

### `clean_txt()`
Limpa o conteúdo do arquivo `historicoPrisma.txt` após confirmação do usuário.

# Todo
Adicionar uma função que gere um gráfico que represente a distribuição normal.