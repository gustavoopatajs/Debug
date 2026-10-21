# Auditor de Diretórios — Manutenção de Código Legado

Atividade prática de manutenção de um sistema em Python que audita a estrutura de arquivos de um projeto. O sistema original apresentava resultados não confiáveis, e o trabalho consistiu em investigar, depurar e corrigir o código sem reescrevê-lo.

## Objetivo

O auditor deve percorrer todas as pastas e subpastas do projeto e:

- contabilizar os arquivos encontrados;
- calcular o tamanho total, em bytes;
- identificar o maior arquivo, informando tamanho e caminho completo;
- gerar um relatório (`relatorio.txt`);
- registrar as etapas e os problemas em log (`logs/auditoria.log`).

O relatório e o log produzidos pela própria auditoria não podem alterar os resultados das execuções seguintes.

## Estrutura do projeto

```text
.
├── main.py              # ponto de entrada
├── criar_projeto.py     # gera a estrutura de pastas (fornecido, não alterado)
├── auditor.py           # lógica da auditoria (arquivo corrigido)
├── verificador.py       # valida os requisitos (fornecido, não alterado)
├── controllers/  models/  config/  utils/
├── docs/  tests/  temp/  logs/
└── README.md
```

As pastas e os arquivos de exemplo são criados automaticamente pelo `criar_projeto.py` na primeira execução.

## Como executar

Requer Python 3. Execute em uma pasta isolada, que contenha apenas os arquivos da atividade.

```bash
python main.py
python verificador.py
```

O `verificador.py` deve exibir `[OK]` em todos os itens.

## Correções realizadas

Todas as alterações foram feitas em `auditor.py`.

| # | Problema | Correção |
|---|----------|----------|
| 1 | `os.getcwd()` fazia o auditor analisar a pasta de onde o programa era chamado | `os.path.dirname(os.path.abspath(__file__))` |
| 2 | Pasta de logs chamada `log`, mas a estrutura gerada usa `logs` | Nome ajustado para `logs` |
| 3 | Condição invertida: criava a pasta quando ela já existia (`FileExistsError`) | `os.makedirs(..., exist_ok=True)` |
| 4 | Arquivos ignorados pelo nome, em qualquer pasta | Comparação pelo caminho absoluto |
| 5 | Log de erro sem informar qual arquivo falhou | Mensagem com caminho e motivo |
| 6 | `__pycache__` entrava na contagem | Pasta removida da varredura do `os.walk` |
| 7 | Maior arquivo definido por `len(nome_arquivo)` e guardado só pelo nome | Comparação por tamanho em bytes, guardando o caminho completo |
| 8 | `break` encerrava o `os.walk` na primeira pasta | Remoção do `break`, para analisar as subpastas |
| 9 | Relatório aberto em modo `"a"`, acumulando vários blocos | Modo `"w"`, mantendo um relatório único |
| 10 | `except` genérico escondia a causa dos erros | Erro exibido no terminal e `logging.exception` no log |

As verificações com `assert` foram mantidas, conforme orientação do enunciado.

## Conceitos praticados

- Caminhos e diretórios com `os.path` e `os.makedirs`
- Varredura recursiva com `os.walk`
- Tamanho de arquivos com `os.path.getsize`
- Modos de abertura de arquivo (`"w"` e `"a"`)
- Registro de execução com `logging`
- Depuração: leitura de resultados, logs, docstrings e comentários, lembrando que um comentário não descreve necessariamente o comportamento atual do código

## Observações

- `criar_projeto.py` e `verificador.py` foram mantidos exatamente como fornecidos.
- Executar sem exceção não garante resultado correto; os valores e caminhos do relatório também foram conferidos.
- Os totais exibidos pelo relatório dependem dos arquivos existentes na pasta no momento da execução.

## Autor

Gustavo Opata
