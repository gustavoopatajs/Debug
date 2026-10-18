import os
import logging


NOME_RELATORIO = "relatorio.txt"
NOME_LOG = "auditoria.log"

# CORREÇÃO 1 (ERRO: os.getcwd())
# getcwd() devolve a pasta de ONDE o comando foi executado, não a pasta do
# projeto. O verificador.py roda o main.py a partir da pasta externa, então
# o auditor acabava analisando a pasta errada (ex.: a Desktop inteira).
# __file__ é o caminho deste arquivo, que não muda conforme o local de
# execução.
PASTA_PROJETO = os.path.dirname(os.path.abspath(__file__))

# CORREÇÃO 2 (ERRO: nome da pasta "log")
# O criar_projeto.py cria a pasta "logs" (com s). O nome precisa coincidir,
# e o verificador.py também procura o log em "logs/auditoria.log".
PASTA_LOGS = os.path.join(PASTA_PROJETO, "logs")

CAMINHO_LOG = os.path.join(
    PASTA_LOGS,
    NOME_LOG
)

CAMINHO_RELATORIO = os.path.join(
    PASTA_PROJETO,
    NOME_RELATORIO
)


def preparar_ambiente():
    """
    Verifica e prepara os diretórios necessários para a auditoria.
    """

    print("Preparando ambiente...")

    # CORREÇÃO 3 (ERRO: condição invertida)
    # O código original era: if os.path.exists(PASTA_LOGS): os.mkdir(...)
    # Ou seja, tentava CRIAR a pasta justamente quando ela JÁ existia, o que
    # gera FileExistsError. makedirs com exist_ok=True cria a pasta se ela
    # não existir e não faz nada se já existir.
    os.makedirs(PASTA_LOGS, exist_ok=True)

    print("Ambiente preparado.")


def configurar_log():
    """
    Configura o arquivo utilizado para registrar a execução.
    """

    logging.basicConfig(
        filename=CAMINHO_LOG,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logging.info("Programa iniciado.")


def deve_ignorar_arquivo(caminho):
    """
    Retorna True quando um arquivo produzido pela própria auditoria
    (relatório e log) não deve participar dos cálculos.
    """

    # CORREÇÃO 4 (MELHORIA: comparar pelo caminho completo)
    # Antes, só o NOME era comparado, então qualquer "relatorio.txt" ou
    # "auditoria.log" em QUALQUER pasta seria ignorado. Agora só os dois
    # arquivos gerados pela própria auditoria são ignorados.
    caminho = os.path.abspath(caminho)

    if caminho == os.path.abspath(CAMINHO_RELATORIO):
        return True

    if caminho == os.path.abspath(CAMINHO_LOG):
        return True

    return False


def obter_tamanho(caminho):
    """
    Retorna o tamanho, em bytes, do arquivo informado.
    """

    try:
        return os.path.getsize(caminho)

    except OSError as erro:

        # CORREÇÃO 5 (ERRO: log sem informação útil)
        # A mensagem antiga não dizia QUAL arquivo falhou nem o motivo.
        logging.error(
            f"Não foi possível obter o tamanho de {caminho}: {erro}"
        )

        return 0


def analisar_diretorios():
    """
    Percorre todos os diretórios e subdiretórios do projeto e retorna
    a quantidade de arquivos, o tamanho total, o caminho do maior
    arquivo e o tamanho dele.
    """

    quantidade_arquivos = 0
    tamanho_total = 0

    maior_arquivo = ""
    maior_tamanho = 0

    logging.info(
        "Iniciando análise dos diretórios."
    )

    for pasta_atual, subpastas, arquivos in os.walk(
        PASTA_PROJETO
    ):

        # CORREÇÃO 6 (ERRO: __pycache__ era contado)
        # O Python cria essa pasta ao importar os módulos. Os arquivos .pyc
        # dentro dela não fazem parte do projeto e alteravam a contagem e o
        # tamanho total. Removê-la da lista "subpastas" faz o os.walk não
        # entrar nela (o verificador.py faz o mesmo).
        if "__pycache__" in subpastas:
            subpastas.remove("__pycache__")

        logging.info(
            f"Analisando diretório: {pasta_atual}"
        )

        for nome_arquivo in arquivos:

            caminho_completo = os.path.join(
                pasta_atual,
                nome_arquivo
            )

            if deve_ignorar_arquivo(caminho_completo):
                continue

            quantidade_arquivos += 1

            tamanho = obter_tamanho(
                caminho_completo
            )

            tamanho_total += tamanho

            # CORREÇÃO 7 (ERRO: comparava o tamanho do NOME do arquivo)
            # O código antigo era: if len(nome_arquivo) > maior_tamanho
            # len(nome_arquivo) conta as letras do nome, não os bytes do
            # arquivo. Além disso, guardava só o nome. O correto é comparar
            # o tamanho em bytes e guardar o caminho completo, que é o que
            # o enunciado pede.
            if tamanho > maior_tamanho:

                maior_tamanho = tamanho
                maior_arquivo = caminho_completo

        # CORREÇÃO 8 (ERRO: break no fim do loop)
        # Havia um "break" aqui que encerrava o os.walk depois da primeira
        # pasta (a raiz). As subpastas nunca eram analisadas, inclusive a
        # que contém o maior arquivo real. O break foi removido.

    logging.info(
        "Análise dos diretórios finalizada."
    )

    return (
        quantidade_arquivos,
        tamanho_total,
        maior_arquivo,
        maior_tamanho
    )


def validar_resultados(
    quantidade_arquivos,
    tamanho_total
):
    """
    Verifica condições mínimas esperadas antes da geração
    do relatório.
    """

    # As verificações abaixo foram mantidas de propósito: o enunciado
    # pede para investigar a causa quando falharem, e não removê-las.
    assert quantidade_arquivos > 0, \
        "Nenhum arquivo foi encontrado durante a auditoria."

    assert tamanho_total >= 0, \
        "O tamanho total dos arquivos não pode ser negativo."

    logging.info(
        "Validações internas concluídas."
    )


def gerar_relatorio(
    quantidade_arquivos,
    tamanho_total,
    maior_arquivo,
    maior_tamanho
):
    """
    Grava em arquivo os resultados obtidos durante a auditoria.
    O relatório é sobrescrito a cada execução.
    """

    logging.info(
        "Gerando relatório."
    )

    # CORREÇÃO 9 (ERRO: modo "a" acrescentava ao final do arquivo)
    # A cada execução um novo relatório era somado ao anterior, deixando
    # vários blocos "RELATÓRIO DE AUDITORIA" no mesmo arquivo. O modo "w"
    # sobrescreve o arquivo, mantendo um único relatório.
    with open(
        CAMINHO_RELATORIO,
        "w",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(
            "RELATÓRIO DE AUDITORIA\n"
        )

        arquivo.write(
            "=" * 50 + "\n"
        )

        arquivo.write(
            f"Quantidade de arquivos: "
            f"{quantidade_arquivos}\n"
        )

        arquivo.write(
            f"Tamanho total: "
            f"{tamanho_total} bytes\n"
        )

        arquivo.write(
            f"Maior arquivo: "
            f"{maior_arquivo}\n"
        )

        arquivo.write(
            f"Tamanho do maior arquivo: "
            f"{maior_tamanho} bytes\n"
        )

        arquivo.write(
            "=" * 50 + "\n"
        )

    logging.info(
        "Relatório gerado."
    )


def executar_auditoria():
    """
    Coordena as etapas necessárias para executar a auditoria.
    """

    try:

        preparar_ambiente()
        configurar_log()

        print("Analisando arquivos...")

        (
            quantidade_arquivos,
            tamanho_total,
            maior_arquivo,
            maior_tamanho
        ) = analisar_diretorios()

        validar_resultados(
            quantidade_arquivos,
            tamanho_total
        )

        gerar_relatorio(
            quantidade_arquivos,
            tamanho_total,
            maior_arquivo,
            maior_tamanho
        )

        print()
        print("Auditoria concluída.")

        print(
            f"Arquivos encontrados: "
            f"{quantidade_arquivos}"
        )

        print(
            f"Tamanho total: "
            f"{tamanho_total} bytes"
        )

        print(
            f"Maior arquivo: "
            f"{maior_arquivo}"
        )

        print(
            f"Tamanho: "
            f"{maior_tamanho} bytes"
        )

        logging.info(
            "Programa finalizado com sucesso."
        )

    except Exception as erro:

        # CORREÇÃO 10 (ERRO: a causa do erro era escondida)
        # A mensagem genérica antiga escondeu os erros das correções 2 e 3.
        # Agora o erro aparece no terminal e logging.exception grava a causa
        # e o traceback completo no arquivo de log.
        print(
            f"Não foi possível concluir a auditoria: {erro}"
        )

        logging.exception(
            "Erro durante a execução."
        )