import os
import subprocess
import sys


PASTA_PROJETO = os.path.dirname(
    os.path.abspath(__file__)
)

CAMINHO_MAIN = os.path.join(
    PASTA_PROJETO,
    "main.py"
)

CAMINHO_RELATORIO = os.path.join(
    PASTA_PROJETO,
    "relatorio.txt"
)

CAMINHO_LOG = os.path.join(
    PASTA_PROJETO,
    "logs",
    "auditoria.log"
)


def resultado(descricao, correto):

    if correto:
        print(f"[OK] {descricao}")

    else:
        print(f"[ERRO] {descricao}")


def calcular_resultado_esperado():

    quantidade = 0
    tamanho_total = 0

    maior_caminho = ""
    maior_tamanho = 0

    for pasta_atual, subpastas, arquivos in os.walk(
        PASTA_PROJETO
    ):

        if "__pycache__" in subpastas:
            subpastas.remove("__pycache__")

        for nome in arquivos:

            caminho = os.path.join(
                pasta_atual,
                nome
            )

            if caminho == CAMINHO_RELATORIO:
                continue

            if caminho == CAMINHO_LOG:
                continue

            tamanho = os.path.getsize(
                caminho
            )

            quantidade += 1
            tamanho_total += tamanho

            if tamanho > maior_tamanho:

                maior_tamanho = tamanho
                maior_caminho = caminho

    return (
        quantidade,
        tamanho_total,
        maior_caminho,
        maior_tamanho
    )


def executar_sistema():

    pasta_externa = os.path.dirname(
        PASTA_PROJETO
    )

    return subprocess.run(
        [
            sys.executable,
            CAMINHO_MAIN
        ],
        cwd=pasta_externa,
        capture_output=True,
        text=True
    )


def ler_relatorio():

    if not os.path.exists(
        CAMINHO_RELATORIO
    ):
        return ""

    with open(
        CAMINHO_RELATORIO,
        "r",
        encoding="utf-8"
    ) as arquivo:

        return arquivo.read()


def main():

    print("=" * 60)
    print("VERIFICAÇÃO DO PROJETO")
    print("=" * 60)

    (
        quantidade,
        tamanho_total,
        maior_caminho,
        maior_tamanho
    ) = calcular_resultado_esperado()

    execucao = executar_sistema()

    resultado(
        "Execução do programa",
        execucao.returncode == 0
    )

    texto = ler_relatorio()

    resultado(
        "Geração do relatório",
        texto != ""
    )

    resultado(
        "Quantidade de arquivos",
        f"Quantidade de arquivos: {quantidade}"
        in texto
    )

    resultado(
        "Tamanho total dos arquivos",
        f"Tamanho total: {tamanho_total} bytes"
        in texto
    )

    resultado(
        "Identificação do maior arquivo",
        os.path.basename(maior_caminho)
        in texto
    )

    resultado(
        "Tamanho do maior arquivo",
        f"Tamanho do maior arquivo: "
        f"{maior_tamanho} bytes"
        in texto
    )

    resultado(
        "Caminho do maior arquivo",
        maior_caminho in texto
    )

    resultado(
        "Arquivo de log",
        os.path.exists(CAMINHO_LOG)
    )

    resultado(
        "Relatório único",
        texto.count(
            "RELATÓRIO DE AUDITORIA"
        ) == 1
    )

    print("=" * 60)


if __name__ == "__main__":
    main()