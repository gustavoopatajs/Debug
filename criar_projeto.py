# ==============================================================
#                         ATENÇÃO
#
#            NÃO ALTERE NENHUMA LINHA DESTE ARQUIVO.
#
# Este programa faz parte da preparação da atividade.
# Ele será executado automaticamente pelo programa principal.
#
# NÃO CORRIJA, NÃO COMPLETE, NÃO APAGUE E NÃO MODIFIQUE
# NENHUMA PARTE DESTE CÓDIGO.
# ==============================================================

import os


PASTA_BASE = os.path.dirname(os.path.abspath(__file__))


DOCUMENTACOES = {

    "controllers": """DOCUMENTAÇÃO PEDAGÓGICA — CONTROLLERS

Em muitos projetos, controllers são responsáveis por receber uma solicitação e coordenar quais partes do sistema deverão atuar para atendê-la.

Um controller pode receber informações, solicitar operações a outras partes da aplicação e determinar qual deverá ser a próxima ação do sistema.

EXEMPLO:
Imagine um sistema acadêmico no qual o usuário solicita o cadastro de um novo aluno. Um controller pode receber os dados informados, encaminhá-los para as partes responsáveis pelo processamento e determinar o que deverá acontecer após o cadastro.

NEM TODA OPERAÇÃO PRECISA DE UM CONTROLLER:
Uma função auxiliar utilizada apenas para formatar uma data, criar um diretório ou verificar a extensão de um arquivo não representa, por si só, uma operação que precise ser organizada como um controller. Dependendo da arquitetura adotada, esse tipo de recurso poderia estar localizado, por exemplo, entre os utilitários do projeto.

A separação em controllers ajuda a evitar que diferentes responsabilidades do sistema fiquem concentradas no mesmo arquivo.

Esta pasta representa uma organização possível. Nem todo projeto utiliza controllers ou uma pasta com esse nome.
""",

    "models": """DOCUMENTAÇÃO PEDAGÓGICA — MODELS

Em muitos projetos, models representam dados e conceitos importantes para o funcionamento do sistema.

Um model pode representar, por exemplo, um aluno, usuário, produto, pedido ou disciplina.

As informações utilizadas pelo sistema podem ter diferentes origens. Elas podem vir de um banco de dados, de arquivos como CSV e planilhas ou de outras fontes utilizadas pela aplicação.

Por exemplo, um model de Aluno poderia representar informações como matrícula, nome e curso, independentemente de esses dados terem sido originalmente obtidos de um banco de dados ou de um arquivo.

Dependendo da arquitetura utilizada, os models também podem possuir regras relacionadas aos dados representados.

Esta pasta foi incluída para demonstrar uma possível separação de responsabilidades encontrada em projetos de software.
""",

    "config": """DOCUMENTAÇÃO PEDAGÓGICA — CONFIG

A pasta config pode ser utilizada para armazenar configurações necessárias ao funcionamento de uma aplicação.

Alguns exemplos são:

- nome ou caminho de arquivos utilizados pelo sistema;
- endereço de um servidor;
- nome de um banco de dados;
- parâmetros utilizados durante a execução;
- definição de diretórios utilizados pela aplicação;
- configurações relacionadas à geração de logs.

Imagine, por exemplo, que um sistema precise saber em qual diretório deverá armazenar seus relatórios. Manter essa informação em uma configuração pode evitar que o mesmo caminho precise ser escrito em diferentes partes do código.

Em projetos reais, configurações podem ser armazenadas de diversas maneiras. Esta pasta representa apenas uma dessas possibilidades.
""",

    "utils": """DOCUMENTAÇÃO PEDAGÓGICA — UTILS

A pasta utils pode reunir recursos auxiliares utilizados por diferentes partes de uma aplicação.

Alguns exemplos são:

- funções para criar diretórios;
- funções para manipular arquivos;
- validações genéricas;
- conversões de valores;
- formatação de textos ou datas;
- funções auxiliares para trabalhar com caminhos.

Neste exercício, o programa utilizado para gerar a estrutura de pastas e arquivos é um exemplo de recurso com características de um utilitário: sua responsabilidade é auxiliar na preparação da estrutura utilizada pelo restante do sistema.

Por uma decisão de organização desta atividade, esse arquivo permanece fora da pasta utils.

É importante evitar transformar utils em um local para qualquer código que não tenha um destino definido.
""",

    "docs": """DOCUMENTAÇÃO PEDAGÓGICA — DOCS

A pasta docs pode armazenar a documentação produzida durante o planejamento, desenvolvimento e manutenção de um projeto.

Durante a Engenharia de Software, por exemplo, a equipe pode produzir materiais para registrar e comunicar como o sistema deverá funcionar.

Entre os documentos que poderiam ser armazenados estão:

- requisitos funcionais e não funcionais;
- diagramas;
- fluxos de processos;
- decisões tomadas durante o projeto;
- especificações;
- instruções de utilização;
- documentação técnica.

Materiais relacionados ao planejamento de um banco de dados também podem fazer parte da documentação do projeto, como representações visuais de entidades, relacionamentos e outras decisões utilizadas na estruturação dos dados.

Isso permite que informações definidas pela equipe durante o desenho dos requisitos, dos fluxos, do software e dos dados não permaneçam apenas na memória dos desenvolvedores.

Nesta atividade, alguns arquivos e subdiretórios também foram colocados nesta pasta para permitir a exploração de uma estrutura com diferentes níveis de profundidade.
""",

    "tests": """DOCUMENTAÇÃO PEDAGÓGICA — TESTS

A pasta tests normalmente é utilizada para armazenar testes relacionados ao funcionamento do sistema.

Testes ajudam a verificar automaticamente se determinadas partes do programa continuam apresentando o comportamento esperado após alterações no código.

Nesta atividade, não será necessário desenvolver uma estrutura profissional de testes automatizados.

A pasta está presente principalmente para apresentar sua finalidade e compor o projeto utilizado durante a auditoria.
""",

    "temp": """DOCUMENTAÇÃO PEDAGÓGICA — TEMP

Uma pasta temporária pode ser utilizada para armazenar arquivos necessários apenas durante determinadas etapas de processamento.

Em aplicações reais, arquivos temporários podem precisar ser removidos, substituídos ou ignorados depois de determinada operação.

Nesta atividade, a pasta temp faz parte da estrutura utilizada para exercitar a auditoria de arquivos.
""",

    "logs": """DOCUMENTAÇÃO PEDAGÓGICA — LOGS

A pasta logs é destinada aos registros produzidos durante a execução de uma aplicação.

Logs podem registrar o início e o término de operações, avisos, erros e outras informações úteis para acompanhamento e investigação de problemas.

Nesta atividade, o próprio auditor deverá produzir registros de sua execução nesta pasta.

O arquivo de log gerado pelo auditor não deverá ser contabilizado como um arquivo pertencente à estrutura original analisada.
"""
}


SUBDOCUMENTACOES = {

    os.path.join("controllers", "relatorios"):
    """DOCUMENTAÇÃO PEDAGÓGICA — RELATÓRIOS

Esta subpasta representa uma possível subdivisão interna da camada de controllers.

Em projetos maiores, uma mesma área pode possuir subdivisões para facilitar a organização de arquivos relacionados.

Ela também foi incluída nesta atividade para demonstrar que uma auditoria de diretórios não pode considerar apenas o primeiro nível de pastas.
""",

    os.path.join("models", "historico"):
    """DOCUMENTAÇÃO PEDAGÓGICA — HISTÓRICO

Esta pasta foi criada principalmente para fins pedagógicos.

Ela representa uma situação em que determinado projeto mantém arquivos antigos ou históricos separados dos arquivos atualmente utilizados.

Sua presença também permite observar o comportamento do auditor em estruturas que possuem mais de um nível de diretórios.
""",

    os.path.join("docs", "referencias"):
    """DOCUMENTAÇÃO PEDAGÓGICA — REFERÊNCIAS

Esta subpasta representa um espaço destinado a materiais de referência relacionados à documentação do projeto.

Em um projeto real, a forma de armazenar esses materiais dependerá das necessidades da equipe.

Nesta atividade, a pasta também contribui para a criação de uma estrutura de diretórios com diferentes níveis de profundidade.
""",

    os.path.join("docs", "referencias", "exemplos"):
    """DOCUMENTAÇÃO PEDAGÓGICA — EXEMPLOS

Esta pasta representa um nível adicional de organização dos materiais de referência.

Ela foi criada principalmente para fins pedagógicos, permitindo verificar se ferramentas que analisam diretórios conseguem alcançar arquivos localizados em níveis mais profundos da estrutura.
""",

    os.path.join("temp", "processados"):
    """DOCUMENTAÇÃO PEDAGÓGICA — PROCESSADOS

Esta pasta foi criada para fins pedagógicos e representa um possível local temporário para arquivos que já passaram por determinada etapa de processamento.

Nesta atividade, sua presença também permite observar como o programa se comporta diante de diretórios que podem possuir poucos arquivos ou permanecer vazios.
"""
}


def criar_texto(caminho, conteudo):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)


def criar_binario(caminho, tamanho):
    with open(caminho, "wb") as arquivo:
        arquivo.write(b"0" * tamanho)


def criar_estrutura():

    for pasta, documentacao in DOCUMENTACOES.items():

        caminho_pasta = os.path.join(PASTA_BASE, pasta)

        os.makedirs(
            caminho_pasta,
            exist_ok=True
        )

        criar_texto(
            os.path.join(caminho_pasta, "doc.txt"),
            documentacao
        )

    for pasta, documentacao in SUBDOCUMENTACOES.items():

        caminho_pasta = os.path.join(PASTA_BASE, pasta)

        os.makedirs(
            caminho_pasta,
            exist_ok=True
        )

        criar_texto(
            os.path.join(caminho_pasta, "doc.txt"),
            documentacao
        )

    # Controllers
    criar_texto(
        os.path.join(
            PASTA_BASE,
            "controllers",
            "usuario_controller.py"
        ),
        "# Controller de usuários\n"
    )

    criar_texto(
        os.path.join(
            PASTA_BASE,
            "controllers",
            "produto_controller.py"
        ),
        "# Controller de produtos\n"
    )

    criar_texto(
        os.path.join(
            PASTA_BASE,
            "controllers",
            "relatorios",
            "relatorio_controller.py"
        ),
        "# Controller de relatórios\n"
    )

    # Models
    criar_texto(
        os.path.join(
            PASTA_BASE,
            "models",
            "usuario.py"
        ),
        "# Model de usuário\n"
    )

    criar_texto(
        os.path.join(
            PASTA_BASE,
            "models",
            "produto.py"
        ),
        "# Model de produto\n"
    )

    criar_binario(
        os.path.join(
            PASTA_BASE,
            "models",
            "historico",
            "produto_antigo.py"
        ),
        120000
    )

    # Config
    criar_texto(
        os.path.join(
            PASTA_BASE,
            "config",
            "configuracao.txt"
        ),
        "ambiente=desenvolvimento\n"
    )

    # Utils
    criar_texto(
        os.path.join(
            PASTA_BASE,
            "utils",
            "arquivos.py"
        ),
        "# Funções auxiliares para arquivos\n"
    )

    criar_texto(
        os.path.join(
            PASTA_BASE,
            "utils",
            "validacao.py"
        ),
        "# Funções auxiliares de validação\n"
    )

    # Docs
    criar_texto(
        os.path.join(
            PASTA_BASE,
            "docs",
            "requisitos.txt"
        ),
        "Requisitos iniciais do sistema.\n"
    )

    criar_texto(
        os.path.join(
            PASTA_BASE,
            "docs",
            "manual.txt"
        ),
        "Documentação inicial do sistema.\n"
    )

    # Arquivo realmente maior, localizado profundamente
    criar_binario(
        os.path.join(
            PASTA_BASE,
            "docs",
            "referencias",
            "exemplos",
            "base_referencia.dat"
        ),
        819200
    )

    # Tests
    criar_texto(
        os.path.join(
            PASTA_BASE,
            "tests",
            "teste_usuario.txt"
        ),
        "Teste de usuário.\n"
    )

    criar_texto(
        os.path.join(
            PASTA_BASE,
            "tests",
            "teste_produto.txt"
        ),
        "Teste de produto.\n"
    )

    criar_texto(
        os.path.join(
            PASTA_BASE,
            "tests",
            "vazio.txt"
        ),
        ""
    )

    # Temp
    criar_texto(
        os.path.join(
            PASTA_BASE,
            "temp",
            "cache.tmp"
        ),
        "cache temporário\n"
    )

    # Arquivo grande e fácil de encontrar.
    # Pode produzir uma falsa impressão de que a auditoria funcionou.
    criar_binario(
        os.path.join(
            PASTA_BASE,
            "temp",
            "backup_local.dat"
        ),
        512000
    )

    print("Estrutura do projeto preparada.")


# ==============================================================
# NÃO ALTERE ESTE ARQUIVO.
# ==============================================================