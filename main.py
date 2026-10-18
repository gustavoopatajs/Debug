from criar_projeto import criar_estrutura
from auditor import executar_auditoria


def main():
    print("=" * 60)
    print("SISTEMA DE AUDITORIA DE DIRETÓRIOS")
    print("=" * 60)

    print("\nPreparando estrutura do projeto...")
    criar_estrutura()

    print("\nIniciando auditoria...")
    executar_auditoria()


if __name__ == "__main__":
    main()