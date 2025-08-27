"""
TUTORIAL PYTHON - SEÇÃO 0: FUNÇÕES BÁSICAS
===========================================

O QUE SÃO FUNÇÕES BÁSICAS?
--------------------------
Funções básicas são comandos fundamentais que todo programa Python usa.
São como "ferramentas essenciais" que sempre estarão disponíveis.

VAMOS APRENDER:
• print() - Para mostrar informações na tela
• Comentários - Para explicar o código
• input() - Para receber dados do usuário
• len() - Para contar elementos
• type() - Para ver o tipo de dados

PENSE ASSIM: São como as "letras do alfabeto" da programação.
Sem elas, não conseguimos fazer nada!

COMO USAR ESTE ARQUIVO:
• Execute diretamente: python 00_funcoes_basicas.py
• Ou importe em outro arquivo: from 00_funcoes_basicas import demonstrar_funcoes_basicas

ORDEM DE ESTUDO:
Este é o PRIMEIRO arquivo a ser estudado, antes de todos os outros!

Autor: Material de Aula
Data: 25/08
Versão: 3.0 (Organizado e Comentado para Iniciantes)
"""

# =============================================================================
# SEÇÃO 0: FUNÇÕES BÁSICAS
# =============================================================================

def demonstrar_funcoes_basicas():
    """
    Função que demonstra as funções básicas mais importantes do Python.
    
    Esta função mostra como usar print, comentários, input e outras
    funções essenciais com exemplos práticos e explicações simples.
    """
    
    print("=" * 60)
    print("SEÇÃO 0: FUNÇÕES BÁSICAS")
    print("=" * 60)
    
    # =====================================================================
    # 1. PRINT() - MOSTRAR INFORMAÇÕES NA TELA
    # =====================================================================
    print("\n1. PRINT() - MOSTRAR INFORMAÇÕES NA TELA")
    print("-" * 60)
    
    print("O QUE É PRINT?")
    print("   • print() é uma função que mostra texto na tela")
    print("   • É como 'falar' com quem está usando o programa")
    print("   • Sem print(), o programa funciona mas não mostra nada")
    print()
    
    print("EXEMPLOS BÁSICOS:")
    print("-" * 40)
    
    # Exemplo simples
    print("   • print('Olá, mundo!'):")
    print("Olá, mundo!")
    
    # Exemplo com variável
    nome = "João"
    print(f"   • print(f'Olá, {nome}!'):")
    print(f"Olá, {nome}!")
    
    # Exemplo com múltiplos itens
    idade = 25
    cidade = "São Paulo"
    print(f"   • print('Nome:', nome, 'Idade:', idade, 'Cidade:', cidade):")
    print("Nome:", nome, "Idade:", idade, "Cidade:", cidade)
    
    print("\nCOMO FUNCIONA:")
    print("   • print() sempre mostra o que está entre parênteses")
    print("   • f'texto {variavel}' permite incluir variáveis no texto")
    print("   • Podemos passar vários itens separados por vírgula")
    
    # =====================================================================
    # 2. COMENTÁRIOS - EXPLICAR O CÓDIGO
    # =====================================================================
    print("\n\n2. COMENTÁRIOS - EXPLICAR O CÓDIGO")
    print("-" * 60)
    
    print("O QUE SÃO COMENTÁRIOS?")
    print("   • Comentários são notas que explicam o código")
    print("   • O Python ignora comentários (não executa)")
    print("   • São essenciais para entender o código depois")
    print()
    
    print("TIPOS DE COMENTÁRIOS:")
    print("-" * 40)
    
    # Comentário de uma linha (usa #)
    print("   • Comentário de uma linha:")
    print("   • # Este é um comentário de uma linha")
    
    # Comentário de múltiplas linhas (usa ''' ou """)
    print("\n   • Comentário de múltiplas linhas:")
    print("   • ''' Este comentário")
    print("   • pode ter várias linhas '''")
    
    # Comentário inline (na mesma linha do código)
    x = 10  # x recebe o valor 10
    print(f"\n   • Comentário inline: x = 10  # x recebe o valor 10")
    print(f"   • Resultado: x = {x}")
    
    print("\nCOMO FUNCIONA:")
    print("   • # Comenta apenas uma linha")
    print("   • ''' ou \"\"\" comentam várias linhas")
    print("   • Comentários não afetam o funcionamento do programa")
    print("   • São essenciais para documentar o código")
    
    # =====================================================================
    # 3. INPUT() - RECEBER DADOS DO USUÁRIO
    # =====================================================================
    print("\n\n3. INPUT() - RECEBER DADOS DO USUÁRIO")
    print("-" * 60)
    
    print("O QUE É INPUT?")
    print("   • input() permite que o usuário digite algo")
    print("   • O programa 'espera' até o usuário pressionar Enter")
    print("   • É como fazer uma pergunta e esperar a resposta")
    print()
    
    print("EXEMPLOS DE INPUT:")
    print("-" * 40)
    
    # Input simples
    print("   • input('Digite seu nome: '):")
    print("   • (Simulando entrada do usuário: 'Maria')")
    # nome_usuario = input("Digite seu nome: ")  # Comentado para não parar o programa
    nome_usuario = "Maria"  # Simulando a entrada
    print(f"   • Nome digitado: {nome_usuario}")
    
    # Input com mensagem explicativa
    print("\n   • input('Digite sua idade: '):")
    print("   • (Simulando entrada do usuário: '30')")
    # idade_usuario = input("Digite sua idade: ")  # Comentado para não parar o programa
    idade_usuario = "30"  # Simulando a entrada
    print(f"   • Idade digitada: {idade_usuario}")
    
    print("\nCOMO FUNCIONA:")
    print("   • input('mensagem') mostra a mensagem e espera digitação")
    print("   • O que for digitado fica guardado na variável")
    print("   • input() sempre retorna uma string (texto)")
    print("   • Para números, precisamos converter: int(input()) ou float(input())")
    
    # =====================================================================
    # 4. LEN() - CONTAR ELEMENTOS
    # =====================================================================
    print("\n\n4. LEN() - CONTAR ELEMENTOS")
    print("-" * 60)
    
    print("O QUE É LEN?")
    print("   • len() conta quantos elementos existem em algo")
    print("   • Funciona com strings, listas, dicionários, etc.")
    print("   • É como contar quantas letras tem uma palavra")
    print()
    
    print("EXEMPLOS DE LEN:")
    print("-" * 40)
    
    # Contando caracteres em uma string
    palavra = "Python"
    print(f"   • palavra = '{palavra}'")
    print(f"   • len(palavra) = {len(palavra)}")
    
    # Contando itens em uma lista
    frutas = ["maçã", "banana", "laranja"]
    print(f"\n   • frutas = {frutas}")
    print(f"   • len(frutas) = {len(frutas)}")
    
    # Contando chaves em um dicionário
    pessoa = {"nome": "João", "idade": 25, "cidade": "SP"}
    print(f"\n   • pessoa = {pessoa}")
    print(f"   • len(pessoa) = {len(pessoa)}")
    
    print("\nCOMO FUNCIONA:")
    print("   • len(string) conta os caracteres")
    print("   • len(lista) conta os itens")
    print("   • len(dicionario) conta as chaves")
    print("   • len() sempre retorna um número inteiro")
    
    # =====================================================================
    # 5. TYPE() - VER O TIPO DE DADOS
    # =====================================================================
    print("\n\n5. TYPE() - VER O TIPO DE DADOS")
    print("-" * 60)
    
    print("O QUE É TYPE?")
    print("   • type() mostra qual é o tipo de um dado")
    print("   • É essencial para entender o que estamos trabalhando")
    print("   • Ajuda a debugar problemas no código")
    print()
    
    print("EXEMPLOS DE TYPE:")
    print("-" * 40)
    
    # Verificando tipos diferentes
    texto = "Olá"
    numero = 42
    decimal = 3.14
    verdadeiro = True
    
    print(f"   • texto = '{texto}'")
    print(f"   • type(texto) = {type(texto)}")
    
    print(f"\n   • numero = {numero}")
    print(f"   • type(numero) = {type(numero)}")
    
    print(f"\n   • decimal = {decimal}")
    print(f"   • type(decimal) = {type(decimal)}")
    
    print(f"\n   • verdadeiro = {verdadeiro}")
    print(f"   • type(verdadeiro) = {type(verdadeiro)}")
    
    print("\nCOMO FUNCIONA:")
    print("   • type() sempre retorna o tipo do dado")
    print("   • str = string (texto)")
    print("   • int = inteiro (número sem vírgula)")
    print("   • float = decimal (número com vírgula)")
    print("   • bool = booleano (True ou False)")
    
    # =====================================================================
    # 6. OUTRAS FUNÇÕES ÚTEIS
    # =====================================================================
    print("\n\n6. OUTRAS FUNÇÕES ÚTEIS")
    print("-" * 60)
    
    print("STR() - CONVERTER PARA STRING:")
    print("-" * 40)
    
    numero_para_texto = 123
    texto_convertido = str(numero_para_texto)
    print(f"   • numero_para_texto = {numero_para_texto}")
    print(f"   • str(numero_para_texto) = '{texto_convertido}'")
    print(f"   • type(texto_convertido) = {type(texto_convertido)}")
    
    print("\nINT() - CONVERTER PARA INTEIRO:")
    print("-" * 40)
    
    texto_para_numero = "456"
    numero_convertido = int(texto_para_numero)
    print(f"   • texto_para_numero = '{texto_para_numero}'")
    print(f"   • int(texto_para_numero) = {numero_convertido}")
    print(f"   • type(numero_convertido) = {type(numero_convertido)}")
    
    print("\nFLOAT() - CONVERTER PARA DECIMAL:")
    print("-" * 40)
    
    texto_para_decimal = "7.89"
    decimal_convertido = float(texto_para_decimal)
    print(f"   • type(texto_para_decimal) = {type(texto_para_decimal)}")
    print(f"   • float(texto_para_decimal) = {decimal_convertido}")
    print(f"   • type(decimal_convertido) = {type(decimal_convertido)}")
    
    # =====================================================================
    # RESUMO DAS FUNÇÕES BÁSICAS
    # =====================================================================
    print("\n\nRESUMO DAS FUNÇÕES BÁSICAS:")
    print("-" * 60)
    print("SAÍDA:")
    print("   • print() - Mostra informações na tela")
    print()
    print("ENTRADA:")
    print("   • input() - Recebe dados do usuário")
    print()
    print("INFORMAÇÕES:")
    print("   • len() - Conta elementos")
    print("   • type() - Mostra o tipo de dados")
    print()
    print("CONVERSÕES:")
    print("   • str() - Converte para string")
    print("   • int() - Converte para inteiro")
    print("   • float() - Converte para decimal")
    print()
    print("COMENTÁRIOS:")
    print("   • # - Comentário de uma linha")
    print("   • ''' ou \"\"\" - Comentário de múltiplas linhas")
    
    print("\n" + "-" * 60)
    print("FIM DA SEÇÃO 0 - FUNÇÕES BÁSICAS")
    print("-" * 60)
    
    # =====================================================================
    # PRÓXIMOS PASSOS
    # =====================================================================
    print("\nPRÓXIMOS PASSOS:")
    print("-" * 60)
    print("Agora que você aprendeu as funções básicas, continue com:")
    print("• 01_tipos_dados.py - Tipos de dados básicos")
    print("• 02_operadores.py - Operadores")
    print("• 03_estruturas_controle.py - Estruturas de controle")
    print("• 04_funcoes.py - Funções")
    print("• 05_poo.py - Programação Orientada a Objetos")
    print("• 06_exemplos_avancados.py - Exemplos avançados")
    print()
    print("Execute: python 01_tipos_dados.py")

# =============================================================================
# EXECUÇÃO INDEPENDENTE
# =============================================================================

if __name__ == "__main__":
    """
    Este bloco executa quando o arquivo é executado diretamente.
    Permite que cada arquivo funcione independentemente.
    """
    print("🚀 INICIANDO TUTORIAL PYTHON - SEÇÃO 0: FUNÇÕES BÁSICAS")
    print("=" * 80)
    print()
    print("Este arquivo pode ser executado independentemente!")
    print("Execute: python 00_funcoes_basicas.py")
    print()
    print("Pressione Enter para começar...")
    
    try:
        input()  # Aguarda o usuário pressionar Enter
        demonstrar_funcoes_basicas()
    except KeyboardInterrupt:
        print("\n\n❌ Tutorial interrompido pelo usuário.")
        print("Execute novamente: python 00_funcoes_basicas.py")
    except Exception as e:
        print(f"\n\n❌ Erro inesperado: {e}")
        print("Verifique se o Python está instalado corretamente.")
