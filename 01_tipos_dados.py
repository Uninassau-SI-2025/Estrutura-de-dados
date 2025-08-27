"""
TUTORIAL PYTHON - SEÇÃO 1: TIPOS DE DADOS BÁSICOS
==================================================

O QUE SÃO TIPOS DE DADOS?
-------------------------
Em programação, os dados que manipulamos têm diferentes "formas" ou "tipos".
Assim como na vida real temos diferentes tipos de objetos (carros, casas, pessoas),
no Python temos diferentes tipos de dados (texto, números, listas, etc.).

Cada tipo de dado tem características específicas e comportamentos próprios.
Entender os tipos de dados é fundamental para programar bem!

COMO USAR ESTE ARQUIVO:
• Execute diretamente: python 01_tipos_dados.py
• Ou importe em outro arquivo: from 01_tipos_dados import demonstrar_tipos_dados

ORDEM DE ESTUDO:
Este é o SEGUNDO arquivo a ser estudado, após 00_funcoes_basicas.py

PRÉ-REQUISITOS:
• Conhecimento das funções básicas (print, comentários, type, etc.)

Autor: Material de Aula
Data: 25/08
Versão: 3.0 (Organizado e Comentado para Iniciantes)
"""

# =============================================================================
# SEÇÃO 1: TIPOS DE DADOS BÁSICOS
# =============================================================================

def demonstrar_tipos_dados():
    """
    Função que demonstra todos os tipos de dados básicos do Python.
    
    Esta função é como uma "aula prática" onde mostramos cada tipo
    de dado e explicamos o que ele é.
    """
    
    print("=" * 60)
    print("SEÇÃO 1: TIPOS DE DADOS BÁSICOS")
    print("=" * 60)
    
    # =====================================================================
    # 1. STRING (str) - TEXTO
    # =====================================================================
    print("\n1. STRING (str) - TEXTO")
    print("-" * 40)
    
    # String é uma sequência de caracteres (letras, números, símbolos)
    # Pode ser criada com aspas simples '' ou duplas ""
    nome = "João Silva"
    cidade = 'São Paulo'
    
    print(f"String: '{nome}' - Tipo: {type(nome)}")
    print(f"String: '{cidade}' - Tipo: {type(cidade)}")
    print("• Strings são usadas para armazenar texto")
    print("• Podem conter letras, números, espaços e símbolos")
    print("• São imutáveis (não podem ser alteradas depois de criadas)")
    
    # =====================================================================
    # 2. INTEIRO (int) - NÚMEROS INTEIROS
    # =====================================================================
    print("\n2. INTEIRO (int) - NÚMEROS INTEIROS")
    print("-" * 40)
    
    # Inteiro são números sem parte decimal
    # Podem ser positivos, negativos ou zero
    idade = 28
    temperatura = -5
    quantidade = 0
    
    print(f"Inteiro: {idade} - Tipo: {type(idade)}")
    print(f"Inteiro negativo: {temperatura} - Tipo: {type(temperatura)}")
    print(f"Zero: {quantidade} - Tipo: {type(quantidade)}")
    print("• Inteiros são números sem vírgula")
    print("• Podem ser positivos, negativos ou zero")
    print("• São usados para contagens, idades, quantidades, etc.")
    
    # =====================================================================
    # 3. FLOAT - NÚMEROS DECIMAIS
    # =====================================================================
    print("\n3. FLOAT - NÚMEROS DECIMAIS")
    print("-" * 40)
    
    # Float são números com parte decimal
    # Usam ponto (.) como separador decimal
    saldo_conta = 1500.75
    altura = 1.75
    pi = 3.14159
    
    print(f"Float: {saldo_conta} - Tipo: {type(saldo_conta)}")
    print(f"Float: {altura} - Tipo: {type(altura)}")
    print(f"Float: {pi} - Tipo: {type(pi)}")
    print("• Floats são números com vírgula decimal")
    print("• Usam ponto (.) como separador (não vírgula)")
    print("• São usados para preços, medidas, cálculos científicos, etc.")
    
    # =====================================================================
    # 4. BOOLEAN (bool) - VALORES LÓGICOS
    # =====================================================================
    print("\n4. BOOLEAN (bool) - VALORES LÓGICOS")
    print("-" * 40)
    
    # Boolean só pode ter dois valores: True (Verdadeiro) ou False (Falso)
    # São muito usados em decisões e condições
    is_admin = False
    esta_chovendo = True
    tem_estoque = True
    
    print(f"Boolean: {is_admin} - Tipo: {type(is_admin)}")
    print(f"Boolean: {esta_chovendo} - Tipo: {type(esta_chovendo)}")
    print(f"Boolean: {tem_estoque} - Tipo: {type(tem_estoque)}")
    print("• Boolean só pode ser True ou False")
    print("• True = Verdadeiro, False = Falso")
    print("• São usados para decisões: 'se está chovendo, leve guarda-chuva'")
    
    # =====================================================================
    # 5. LISTA (list) - COLEÇÃO ORDENADA
    # =====================================================================
    print("\n5. LISTA (list) - COLEÇÃO ORDENADA")
    print("-" * 40)
    
    # Lista é uma coleção de itens em uma ordem específica
    # Os itens podem ser de tipos diferentes
    # Listas são mutáveis (podem ser alteradas)
    lista_produtos = ["Notebook", "Mouse", "Teclado", "Monitor"]
    lista_mista = ["texto", 123, 45.67, True]
    
    print(f"Lista: {lista_produtos} - Tipo: {type(lista_produtos)}")
    print(f"Lista mista: {lista_mista} - Tipo: {type(lista_mista)}")
    print("• Listas são coleções ordenadas de itens")
    print("• Podem conter diferentes tipos de dados")
    print("• São mutáveis (podem ser alteradas)")
    print("• Usam colchetes [] para criar")
    print("• São muito úteis para armazenar múltiplos valores")
    
    # =====================================================================
    # 6. DICIONÁRIO (dict) - COLEÇÃO CHAVE-VALOR
    # =====================================================================
    print("\n6. DICIONÁRIO (dict) - COLEÇÃO CHAVE-VALOR")
    print("-" * 40)
    
    # Dicionário é uma coleção de pares chave-valor
    # Cada item tem uma chave (nome) e um valor associado
    # É como um dicionário real: palavra (chave) -> significado (valor)
    dicionario_produtos = {
        "Notebook": 1500.75,
        "Mouse": 25.99,
        "Teclado": 49.99,
        "Monitor": 299.99
    }
    
    dicionario_pessoa = {
        "nome": "Maria",
        "idade": 25,
        "cidade": "Rio de Janeiro",
        "ativo": True
    }
    
    print(f"Dicionário produtos: {dicionario_produtos} - Tipo: {type(dicionario_produtos)}")
    print(f"Dicionário pessoa: {dicionario_pessoa} - Tipo: {type(dicionario_pessoa)}")
    print("• Dicionários são coleções de pares chave-valor")
    print("• Cada item tem um nome (chave) e um valor")
    print("• Usam chaves {} para criar")
    print("• São muito úteis para organizar dados relacionados")
    print("• Exemplo: 'nome' é a chave, 'Maria' é o valor")
    
    # =====================================================================
    # 7. TUPLA (tuple) - COLEÇÃO IMUTÁVEL
    # =====================================================================
    print("\n7. TUPLA (tuple) - COLEÇÃO IMUTÁVEL")
    print("-" * 40)
    
    # Tupla é como uma lista, mas não pode ser alterada (imutável)
    # Usa parênteses () para criar
    coordenadas = (10, 20)
    cores_rgb = (255, 128, 0)
    
    print(f"Tupla: {coordenadas} - Tipo: {type(coordenadas)}")
    print(f"Tupla RGB: {cores_rgb} - Tipo: {type(cores_rgb)}")
    print("• Tuplas são como listas, mas não podem ser alteradas")
    print("• Usam parênteses () para criar")
    print("• São úteis para dados que não devem mudar")
    print("• Exemplo: coordenadas de um ponto, cores RGB")
    
    # =====================================================================
    # 8. CONJUNTO (set) - COLEÇÃO DE ELEMENTOS ÚNICOS
    # =====================================================================
    print("\n8. CONJUNTO (set) - COLEÇÃO DE ELEMENTOS ÚNICOS")
    print("-" * 40)
    
    # Conjunto é uma coleção que não permite elementos duplicados
    # Não mantém ordem específica
    cores = {"vermelho", "azul", "verde", "azul"}  # "azul" será duplicado
    numeros = {1, 2, 3, 3, 4, 5, 5}  # Números duplicados serão removidos
    
    print(f"Conjunto cores: {cores} - Tipo: {type(cores)}")
    print(f"Conjunto números: {numeros} - Tipo: {type(numeros)}")
    print("• Conjuntos não permitem elementos duplicados")
    print("• Não mantêm ordem específica")
    print("• Usam chaves {} para criar (como dicionários)")
    print("• São úteis para remover duplicatas")
    print("• Exemplo: lista de usuários únicos, cores disponíveis")
    
    print("\n" + "-" * 60)
    print("FIM DA SEÇÃO 1 - TIPOS DE DADOS BÁSICOS")
    print("-" * 60)
    
    # =====================================================================
    # PRÓXIMOS PASSOS
    # =====================================================================
    print("\nPRÓXIMOS PASSOS:")
    print("-" * 60)
    print("Agora que você aprendeu os tipos de dados, continue com:")
    print("• 02_operadores.py - Operadores")
    print("• 03_estruturas_controle.py - Estruturas de controle")
    print("• 04_funcoes.py - Funções")
    print("• 05_poo.py - Programação Orientada a Objetos")
    print("• 06_exemplos_avancados.py - Exemplos avançados")
    print()
    print("Execute: python 02_operadores.py")

# =============================================================================
# EXECUÇÃO INDEPENDENTE
# =============================================================================

if __name__ == "__main__":
    """
    Este bloco executa quando o arquivo é executado diretamente.
    Permite que cada arquivo funcione independentemente.
    """
    print("🚀 INICIANDO TUTORIAL PYTHON - SEÇÃO 1: TIPOS DE DADOS BÁSICOS")
    print("=" * 80)
    print()
    print("Este arquivo pode ser executado independentemente!")
    print("Execute: python 01_tipos_dados.py")
    print()
    print("Pressione Enter para começar...")
    
    try:
        input()  # Aguarda o usuário pressionar Enter
        demonstrar_tipos_dados()
    except KeyboardInterrupt:
        print("\n\n❌ Tutorial interrompido pelo usuário.")
        print("Execute novamente: python 01_tipos_dados.py")
    except Exception as e:
        print(f"\n\n❌ Erro inesperado: {e}")
        print("Verifique se o Python está instalado corretamente.")
