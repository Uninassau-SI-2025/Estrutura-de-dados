"""
TUTORIAL PYTHON - SEÇÃO 6: EXEMPLOS AVANÇADOS
==============================================

O QUE SÃO EXEMPLOS AVANÇADOS?
-----------------------------
Nesta seção, vamos ver alguns recursos mais avançados do Python que
combinam os conceitos que aprendemos anteriormente.

VAMOS APRENDER:
• Tratamento de erros (try/except)
• List comprehension (criação de listas de forma elegante)
• Outros recursos úteis

PENSE ASSIM: São como "truques" que tornam o código mais elegante
e robusto, mas sempre baseados nos conceitos fundamentais.

COMO USAR ESTE ARQUIVO:
• Execute diretamente: python 06_exemplos_avancados.py
• Ou importe em outro arquivo: from 06_exemplos_avancados import demonstrar_exemplos_avancados

ORDEM DE ESTUDO:
Este é o SÉTIMO e ÚLTIMO arquivo a ser estudado, após 05_poo.py

PRÉ-REQUISITOS:
• Conhecimento de todas as seções anteriores
• Familiaridade com tipos de dados, operadores, estruturas de controle
• Compreensão de funções e POO
• Boa base dos conceitos fundamentais

Autor: Material de Aula
Data: 25/08
Versão: 3.0 (Organizado e Comentado para Iniciantes)
"""

# =============================================================================
# SEÇÃO 6: EXEMPLOS AVANÇADOS
# =============================================================================

def demonstrar_exemplos_avancados():
    """
    Função que demonstra recursos avançados do Python.
    
    Esta função mostra tratamento de erros, list comprehension e outros
    recursos com exemplos práticos e explicações simples.
    """
    
    print("=" * 60)
    print("SEÇÃO 6: EXEMPLOS AVANÇADOS")
    print("=" * 60)
    
    # =====================================================================
    # 1. TRATAMENTO DE ERROS - try/except
    # =====================================================================
    print("\n1. TRATAMENTO DE ERROS - try/except")
    print("-" * 60)
    
    print("O QUE É TRATAMENTO DE ERROS?")
    print("   • É como 'preparar' o programa para situações problemáticas")
    print("   • Evita que o programa pare de funcionar quando algo dá errado")
    print("   • Permite tratar o erro de forma elegante")
    print()
    
    def dividir_numeros(a, b):
        """
        Função que demonstra tratamento de erros.
        
        Args:
            a (int/float): Numerador
            b (int/float): Denominador
        
        Returns:
            float: Resultado da divisão ou mensagem de erro
        """
        try:
            # Tenta executar este código
            resultado = a / b
            return resultado
        except ZeroDivisionError:
            # Se der erro de divisão por zero, executa este código
            return "Erro: Divisão por zero não é permitida"
        except TypeError:
            # Se der erro de tipo, executa este código
            return "Erro: Ambos os valores devem ser números"
        except Exception as e:
            # Se der qualquer outro erro, executa este código
            return f"Erro inesperado: {e}"
    
    print("EXEMPLOS DE TRATAMENTO DE ERROS:")
    print("-" * 40)
    
    print("   • Caso normal: 10 / 2")
    resultado1 = dividir_numeros(10, 2)
    print(f"     Resultado: {resultado1}")
    
    print("   • Caso problemático: 10 / 0 (divisão por zero)")
    resultado2 = dividir_numeros(10, 0)
    print(f"     Resultado: {resultado2}")
    
    print("   • Caso problemático: 10 / 'a' (tipo incorreto)")
    resultado3 = dividir_numeros(10, 'a')
    print(f"     Resultado: {resultado3}")
    
    print("\nCOMO FUNCIONA O try/except:")
    print("   • try: Tenta executar o código (pode dar erro)")
    print("   • except: Se der erro, executa este código")
    print("   • ZeroDivisionError: Erro específico de divisão por zero")
    print("   • TypeError: Erro de tipo de dado incorreto")
    print("   • Exception: Qualquer outro erro não previsto")
    
    # =====================================================================
    # 2. LIST COMPREHENSION - CRIANDO LISTAS DE FORMA ELEGANTE
    # =====================================================================
    print("\n\n2. LIST COMPREHENSION - CRIANDO LISTAS DE FORMA ELEGANTE")
    print("-" * 60)
    
    print("O QUE É LIST COMPREHENSION?")
    print("   • É uma forma mais elegante e rápida de criar listas")
    print("   • Substitui loops tradicionais em uma única linha")
    print("   • É mais 'pythônico' (estilo característico do Python)")
    print()
    
    # Lista de números para trabalhar
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"   • Lista original: {numeros}")
    
    print("\nEXEMPLO 1: NÚMEROS PARES (FORMA TRADICIONAL)")
    print("-" * 50)
    
    # Forma tradicional com loop for
    pares_tradicional = []
    for num in numeros:
        if num % 2 == 0:
            pares_tradicional.append(num)
    
    print(f"   • Números pares (tradicional): {pares_tradicional}")
    print("   • Código: 4 linhas com loop for")
    
    print("\nEXEMPLO 1: NÚMEROS PARES (LIST COMPREHENSION)")
    print("-" * 50)
    
    # Forma com list comprehension
    pares_comprehension = [num for num in numeros if num % 2 == 0]
    
    print(f"   • Números pares (comprehension): {pares_comprehension}")
    print("   • Código: 1 linha elegante!")
    
    print("\nCOMO FUNCIONA A LIST COMPREHENSION:")
    print("   • [num for num in numeros if num % 2 == 0]")
    print("   • num: O que colocar na lista")
    print("   • for num in numeros: Para cada número na lista")
    print("   • if num % 2 == 0: Só se o número for par")
    print("   • Resultado: Lista com apenas números pares")
    
    print("\nEXEMPLO 2: QUADRADOS DOS NÚMEROS")
    print("-" * 50)
    
    # Criando lista com quadrados dos números
    quadrados = [num**2 for num in numeros]
    print(f"   • Quadrados dos números: {quadrados}")
    print("   • Código: [num**2 for num in numeros]")
    print("   • num**2: Eleva cada número ao quadrado")
    
    print("\nEXEMPLO 3: NÚMEROS MAIORES QUE 5")
    print("-" * 50)
    
    # Filtrando números maiores que 5
    maiores_que_5 = [num for num in numeros if num > 5]
    print(f"   • Números maiores que 5: {maiores_que_5}")
    print("   • Código: [num for num in numeros if num > 5]")
    
    print("\nEXEMPLO 4: STRINGS EM MAIÚSCULO")
    print("-" * 50)
    
    # Trabalhando com strings
    frutas = ["maçã", "banana", "laranja", "uva"]
    frutas_maiusculo = [fruta.upper() for fruta in frutas]
    print(f"   • Frutas originais: {frutas}")
    print(f"   • Frutas em maiúsculo: {frutas_maiusculo}")
    print("   • Código: [fruta.upper() for fruta in frutas]")
    
    # =====================================================================
    # 3. OUTROS RECURSOS ÚTEIS
    # =====================================================================
    print("\n\n3. OUTROS RECURSOS ÚTEIS")
    print("-" * 60)
    
    print("ENUMERATE - NUMERAR ITENS DE UMA LISTA:")
    print("-" * 50)
    
    # enumerate adiciona números aos itens
    cores = ["vermelho", "azul", "verde", "amarelo"]
    print(f"   • Lista de cores: {cores}")
    
    print("   • Forma tradicional:")
    for i in range(len(cores)):
        print(f"     {i}: {cores[i]}")
    
    print("   • Com enumerate (mais elegante):")
    for i, cor in enumerate(cores):
        print(f"     {i}: {cor}")
    
    print("   • enumerate(cores, 1) - começando em 1:")
    for i, cor in enumerate(cores, 1):
        print(f"     {i}: {cor}")
    
    print("\nZIP - COMBINAR DUAS LISTAS:")
    print("-" * 50)
    
    # zip combina duas listas
    nomes = ["João", "Maria", "Pedro"]
    idades = [25, 30, 35]
    
    print(f"   • Nomes: {nomes}")
    print(f"   • Idades: {idades}")
    
    print("   • Combinando com zip:")
    for nome, idade in zip(nomes, idades):
        print(f"     {nome} tem {idade} anos")
    
    print("\nFILTER - FILTRAR ITENS:")
    print("-" * 50)
    
    # filter filtra itens baseado em uma condição
    def eh_par(numero):
        """Função que verifica se um número é par"""
        return numero % 2 == 0
    
    numeros_pares = list(filter(eh_par, numeros))
    print(f"   • Números originais: {numeros}")
    print(f"   • Números pares (filter): {numeros_pares}")
    print("   • Código: list(filter(eh_par, numeros))")
    
    print("\nMAP - APLICAR FUNÇÃO A TODOS OS ITENS:")
    print("-" * 50)
    
    # map aplica uma função a todos os itens
    numeros_dobrados = list(map(lambda x: x * 2, numeros))
    print(f"   • Números originais: {numeros}")
    print(f"   • Números dobrados (map): {numeros_dobrados}")
    print("   • Código: list(map(lambda x: x * 2, numeros))")
    
    print("\nLAMBDA - FUNÇÕES ANÔNIMAS:")
    print("-" * 50)
    
    # lambda cria funções simples em uma linha
    print("   • Função tradicional:")
    def dobrar(x):
        return x * 2
    
    print(f"     dobrar(5) = {dobrar(5)}")
    
    print("   • Função lambda (equivalente):")
    dobrar_lambda = lambda x: x * 2
    print(f"     dobrar_lambda(5) = {dobrar_lambda(5)}")
    
    print("   • Lambda direto:")
    resultado_lambda = (lambda x: x * 2)(5)
    print(f"     (lambda x: x * 2)(5) = {resultado_lambda}")
    
    # =====================================================================
    # 4. EXEMPLO PRÁTICO COMBINANDO VÁRIOS CONCEITOS
    # =====================================================================
    print("\n\n4. EXEMPLO PRÁTICO COMBINANDO VÁRIOS CONCEITOS")
    print("-" * 60)
    
    print("Vamos criar um sistema simples de gerenciamento de produtos")
    print("que combina vários conceitos que aprendemos:")
    print()
    
    # Lista de produtos (dicionários)
    produtos = [
        {"nome": "Notebook", "preco": 1500.75, "categoria": "eletrônicos"},
        {"nome": "Mouse", "preco": 25.99, "categoria": "eletrônicos"},
        {"nome": "Livro", "preco": 45.50, "categoria": "livros"},
        {"nome": "Caneta", "preco": 2.99, "categoria": "papelaria"},
        {"nome": "Monitor", "preco": 299.99, "categoria": "eletrônicos"}
    ]
    
    print("PRODUTOS DISPONÍVEIS:")
    for i, produto in enumerate(produtos, 1):
        print(f"   {i}. {produto['nome']} - R$ {produto['preco']:.2f} ({produto['categoria']})")
    
    print("\nANÁLISES COM LIST COMPREHENSION:")
    print("-" * 50)
    
    # Produtos da categoria eletrônicos
    eletronicos = [p for p in produtos if p['categoria'] == 'eletrônicos']
    print(f"   • Produtos eletrônicos: {len(eletronicos)} itens")
    
    # Produtos com preço maior que 100
    produtos_caros = [p for p in produtos if p['preco'] > 100]
    print(f"   • Produtos caros (>R$ 100): {len(produtos_caros)} itens")
    
    # Nomes dos produtos em maiúsculo
    nomes_maiusculo = [p['nome'].upper() for p in produtos]
    print(f"   • Nomes em maiúsculo: {nomes_maiusculo}")
    
    # Preço total dos produtos
    preco_total = sum(p['preco'] for p in produtos)
    print(f"   • Preço total: R$ {preco_total:.2f}")
    
    # Produto mais caro
    produto_mais_caro = max(produtos, key=lambda p: p['preco'])
    print(f"   • Produto mais caro: {produto_mais_caro['nome']} - R$ {produto_mais_caro['preco']:.2f}")
    
    # =====================================================================
    # RESUMO DOS EXEMPLOS AVANÇADOS
    # =====================================================================
    print("\n\nRESUMO DOS EXEMPLOS AVANÇADOS:")
    print("-" * 60)
    print("TRATAMENTO DE ERROS:")
    print("   • try/except: Evita que o programa pare por erros")
    print("   • Trata erros específicos de forma elegante")
    print("   • Torna o programa mais robusto")
    print()
    print("LIST COMPREHENSION:")
    print("   • Cria listas de forma mais elegante")
    print("   • Substitui loops tradicionais")
    print("   • Código mais limpo e 'pythônico'")
    print()
    print("RECURSOS ÚTEIS:")
    print("   • enumerate: Numera itens de listas")
    print("   • zip: Combina duas listas")
    print("   • filter: Filtra itens baseado em condições")
    print("   • map: Aplica função a todos os itens")
    print("   • lambda: Funções simples em uma linha")
    
    print("\n" + "-" * 60)
    print("FIM DA SEÇÃO 6 - EXEMPLOS AVANÇADOS")
    print("-" * 60)
    
    # =====================================================================
    # CONCLUSÃO FINAL
    # =====================================================================
    print("\nPARABÉNS! 🎉")
    print("-" * 60)
    print("Você completou todo o tutorial de Python!")
    print()
    print("O QUE VOCÊ APRENDEU:")
    print("✓ 00_funcoes_basicas.py - Funções básicas (print, comentários, etc.)")
    print("✓ 01_tipos_dados.py - Tipos de dados básicos")
    print("✓ 02_operadores.py - Operadores")
    print("✓ 03_estruturas_controle.py - Estruturas de controle")
    print("✓ 04_funcoes.py - Funções")
    print("✓ 05_poo.py - Programação Orientada a Objetos")
    print("✓ 06_exemplos_avancados.py - Exemplos avançados")
    print()
    print("PRÓXIMOS PASSOS:")
    print("• Pratique os conceitos com exercícios")
    print("• Crie pequenos projetos para aplicar o conhecimento")
    print("• Explore a documentação oficial do Python")
    print("• Continue aprendendo com recursos online")
    print()
    print("Lembre-se: A prática é fundamental para aprender programação!")
    print("Continue explorando e experimentando com Python.")

# =============================================================================
# EXECUÇÃO INDEPENDENTE
# =============================================================================

if __name__ == "__main__":
    """
    Este bloco executa quando o arquivo é executado diretamente.
    Permite que cada arquivo funcione independentemente.
    """
    print("🚀 INICIANDO TUTORIAL PYTHON - SEÇÃO 6: EXEMPLOS AVANÇADOS")
    print("=" * 80)
    print()
    print("Este arquivo pode ser executado independentemente!")
    print("Execute: python 06_exemplos_avancados.py")
    print()
    print("Pressione Enter para começar...")
    
    try:
        input()  # Aguarda o usuário pressionar Enter
        demonstrar_exemplos_avancados()
    except KeyboardInterrupt:
        print("\n\n❌ Tutorial interrompido pelo usuário.")
        print("Execute novamente: python 06_exemplos_avancados.py")
    except Exception as e:
        print(f"\n\n❌ Erro inesperado: {e}")
        print("Verifique se o Python está instalado corretamente.")
