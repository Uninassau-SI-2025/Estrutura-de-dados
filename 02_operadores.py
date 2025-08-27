"""
TUTORIAL PYTHON - SEÇÃO 2: OPERADORES
======================================

O QUE SÃO OPERADORES?
---------------------
Operadores são símbolos especiais que realizam operações em dados.
É como usar uma calculadora: + para somar, - para subtrair, etc.

No Python, temos vários tipos de operadores:
• Aritméticos: para fazer contas matemáticas
• De comparação: para comparar valores
• Lógicos: para combinar condições
• De atribuição: para guardar valores

COMO USAR ESTE ARQUIVO:
• Execute diretamente: python 02_operadores.py
• Ou importe em outro arquivo: from 02_operadores import demonstrar_operadores

ORDEM DE ESTUDO:
Este é o TERCEIRO arquivo a ser estudado, após 01_tipos_dados.py

PRÉ-REQUISITOS:
• Conhecimento dos tipos de dados básicos
• Entendimento de variáveis e valores

Autor: Material de Aula
Data: 25/08
Versão: 3.0 (Organizado e Comentado para Iniciantes)
"""

# =============================================================================
# SEÇÃO 2: OPERADORES
# =============================================================================

def demonstrar_operadores():
    """
    Função que demonstra todos os tipos de operadores do Python.
    
    Esta função mostra como usar cada tipo de operador com exemplos
    práticos e explicações simples.
    """
    
    print("=" * 60)
    print("SEÇÃO 2: OPERADORES")
    print("=" * 60)
    
    # =====================================================================
    # 1. OPERADORES ARITMÉTICOS - FAZER CONTAS MATEMÁTICAS
    # =====================================================================
    print("\n1. OPERADORES ARITMÉTICOS - FAZER CONTAS MATEMÁTICAS")
    print("-" * 60)
    
    # Vamos usar duas variáveis para demonstrar os operadores
    a, b = 10, 3
    print(f"Vamos usar: a = {a} e b = {b}")
    print()
    
    # Soma: +
    print(f"Soma: {a} + {b} = {a + b}")
    print("   • O símbolo + soma dois números")
    print("   • Exemplo: 10 + 3 = 13")
    
    # Subtração: -
    print(f"\nSubtração: {a} - {b} = {a - b}")
    print("   • O símbolo - subtrai o segundo número do primeiro")
    print("   • Exemplo: 10 - 3 = 7")
    
    # Multiplicação: *
    print(f"\nMultiplicação: {a} * {b} = {a * b}")
    print("   • O símbolo * multiplica dois números")
    print("   • Exemplo: 10 * 3 = 30")
    
    # Divisão: /
    print(f"\nDivisão: {a} / {b} = {a / b}")
    print("   • O símbolo / divide o primeiro número pelo segundo")
    print("   • Exemplo: 10 / 3 = 3.333... (sempre retorna decimal)")
    
    # Divisão inteira: //
    print(f"\nDivisão inteira: {a} // {b} = {a // b}")
    print("   • O símbolo // divide e retorna apenas a parte inteira")
    print("   • Exemplo: 10 // 3 = 3 (ignora a parte decimal)")
    
    # Resto da divisão (módulo): %
    print(f"\nResto da divisão: {a} % {b} = {a % b}")
    print("   • O símbolo % retorna o resto da divisão")
    print("   • Exemplo: 10 % 3 = 1 (10 dividido por 3 = 3, resto 1)")
    
    # Potência: **
    print(f"\nPotência: {a} ** {b} = {a ** b}")
    print("   • O símbolo ** eleva o primeiro número à potência do segundo")
    print("   • Exemplo: 10 ** 3 = 1000 (10³ = 10 × 10 × 10)")
    
    # =====================================================================
    # 2. OPERADORES DE COMPARAÇÃO - COMPARAR VALORES
    # =====================================================================
    print("\n\n2. OPERADORES DE COMPARAÇÃO - COMPARAR VALORES")
    print("-" * 60)
    
    print("Os operadores de comparação retornam True ou False")
    print("True = Verdadeiro, False = Falso")
    print()
    
    # Maior que: >
    print(f"Maior que: {a} > {b} = {a > b}")
    print("   • O símbolo > verifica se o primeiro é maior que o segundo")
    print("   • 10 > 3 é True porque 10 é maior que 3")
    
    # Menor que: <
    print(f"\nMenor que: {a} < {b} = {a < b}")
    print("   • O símbolo < verifica se o primeiro é menor que o segundo")
    print("   • 10 < 3 é False porque 10 não é menor que 3")
    
    # Maior ou igual: >=
    print(f"\nMaior ou igual: {a} >= {b} = {a >= b}")
    print("   • O símbolo >= verifica se o primeiro é maior OU igual ao segundo")
    print("   • 10 >= 3 é True porque 10 é maior que 3")
    
    # Menor ou igual: <=
    print(f"\nMenor ou igual: {a} <= {b} = {a <= b}")
    print("   • O símbolo <= verifica se o primeiro é menor OU igual ao segundo")
    print("   • 10 <= 3 é False porque 10 não é menor nem igual a 3")
    
    # Igual: ==
    print(f"\nIgual: {a} == {b} = {a == b}")
    print("   • O símbolo == verifica se os valores são iguais")
    print("   • 10 == 3 é False porque 10 não é igual a 3")
    print("   • IMPORTANTE: == compara valores, = atribui valores")
    
    # Diferente: !=
    print(f"\nDiferente: {a} != {b} = {a != b}")
    print("   • O símbolo != verifica se os valores são diferentes")
    print("   • 10 != 3 é True porque 10 é diferente de 3")
    
    # =====================================================================
    # 3. OPERADORES LÓGICOS - COMBINAR CONDIÇÕES
    # =====================================================================
    print("\n\n3. OPERADORES LÓGICOS - COMBINAR CONDIÇÕES")
    print("-" * 60)
    
    print("Os operadores lógicos combinam condições True/False")
    print("São muito usados em decisões: 'se está chovendo E tenho guarda-chuva'")
    print()
    
    # AND - Todas as condições devem ser True
    print("AND - Todas as condições devem ser True:")
    print(f"   True and False = {True and False}")
    print("   • AND só retorna True se AMBAS as condições forem True")
    print("   • Exemplo: 'Está chovendo E tenho guarda-chuva'")
    print("   • Se uma das condições for False, o resultado é False")
    
    print(f"\n   True and True = {True and True}")
    print("   • Aqui ambas são True, então o resultado é True")
    
    # OR - Pelo menos uma condição deve ser True
    print(f"\nOR - Pelo menos uma condição deve ser True:")
    print(f"   True or False = {True or False}")
    print("   • OR retorna True se PELO MENOS UMA condição for True")
    print("   • Exemplo: 'Está chovendo OU tenho guarda-chuva'")
    print("   • Se pelo menos uma for True, o resultado é True")
    
    print(f"\n   False or False = {False or False}")
    print("   • Aqui ambas são False, então o resultado é False")
    
    # NOT - Inverte o valor
    print(f"\nNOT - Inverte o valor:")
    print(f"   not True = {not True}")
    print("   • NOT inverte o valor: True vira False, False vira True")
    print("   • Exemplo: 'não está chovendo' (inverte 'está chovendo')")
    
    # =====================================================================
    # 4. OPERADORES DE ATRIBUIÇÃO - GUARDAR VALORES
    # =====================================================================
    print("\n\n4. OPERADORES DE ATRIBUIÇÃO - GUARDAR VALORES")
    print("-" * 60)
    
    print("Os operadores de atribuição guardam valores em variáveis")
    print("O símbolo = é o operador básico de atribuição")
    print()
    
    # Atribuição básica: =
    x = 10
    print(f"Atribuição básica: x = 10")
    print(f"   Valor inicial de x: {x}")
    
    # Atribuição com soma: +=
    x += 5  # Equivale a: x = x + 5
    print(f"\nAtribuição com soma: x += 5")
    print(f"   x += 5 significa: x = x + 5")
    print(f"   Resultado: x = {x}")
    
    # Atribuição com subtração: -=
    x -= 3  # Equivale a: x = x - 3
    print(f"\nAtribuição com subtração: x -= 3")
    print(f"   x -= 3 significa: x = x - 3")
    print(f"   Resultado: x = {x}")
    
    # Atribuição com multiplicação: *=
    x *= 2  # Equivale a: x = x * 2
    print(f"\nAtribuição com multiplicação: x *= 2")
    print(f"   x *= 2 significa: x = x * 2")
    print(f"   Resultado: x = {x}")
    
    # Atribuição com divisão: /=
    x /= 4  # Equivale a: x = x / 4
    print(f"\nAtribuição com divisão: x /= 4")
    print(f"   x /= 4 significa: x = x / 4")
    print(f"   Resultado: x = {x}")
    
    # Atribuição com resto: %=
    x %= 3  # Equivale a: x = x % 3
    print(f"\nAtribuição com resto: x %= 3")
    print(f"   x %= 3 significa: x = x % 3")
    print(f"   Resultado: x = {x}")
    
    # Atribuição com potência: **=
    x **= 2  # Equivale a: x = x ** 2
    print(f"\nAtribuição com potência: x **= 2")
    print(f"   x **= 2 significa: x = x ** 2")
    print(f"   Resultado: x = {x}")
    
    # =====================================================================
    # RESUMO DOS OPERADORES
    # =====================================================================
    print("\n\nRESUMO DOS OPERADORES:")
    print("-" * 60)
    print("ARITMÉTICOS:")
    print("   + (soma), - (subtração), * (multiplicação)")
    print("   / (divisão), // (divisão inteira), % (resto), ** (potência)")
    print()
    print("COMPARAÇÃO:")
    print("   > (maior), < (menor), >= (maior ou igual)")
    print("   <= (menor ou igual), == (igual), != (diferente)")
    print()
    print("LÓGICOS:")
    print("   and (E), or (OU), not (NÃO)")
    print()
    print("ATRIBUIÇÃO:")
    print("   = (atribui), += (soma e atribui), -= (subtrai e atribui)")
    print("   *= (multiplica e atribui), /= (divide e atribui)")
    
    print("\n" + "-" * 60)
    print("FIM DA SEÇÃO 2 - OPERADORES")
    print("-" * 60)
    
    # =====================================================================
    # PRÓXIMOS PASSOS
    # =====================================================================
    print("\nPRÓXIMOS PASSOS:")
    print("-" * 60)
    print("Agora que você aprendeu os operadores, continue com:")
    print("• 03_estruturas_controle.py - Estruturas de controle")
    print("• 04_funcoes.py - Funções")
    print("• 05_poo.py - Programação Orientada a Objetos")
    print("• 06_exemplos_avancados.py - Exemplos avançados")
    print()
    print("Execute: python 03_estruturas_controle.py")

# =============================================================================
# EXECUÇÃO INDEPENDENTE
# =============================================================================

if __name__ == "__main__":
    """
    Este bloco executa quando o arquivo é executado diretamente.
    Permite que cada arquivo funcione independentemente.
    """
    print("🚀 INICIANDO TUTORIAL PYTHON - SEÇÃO 2: OPERADORES")
    print("=" * 80)
    print()
    print("Este arquivo pode ser executado independentemente!")
    print("Execute: python 02_operadores.py")
    print()
    print("Pressione Enter para começar...")
    
    try:
        input()  # Aguarda o usuário pressionar Enter
        demonstrar_operadores()
    except KeyboardInterrupt:
        print("\n\n❌ Tutorial interrompido pelo usuário.")
        print("Execute novamente: python 02_operadores.py")
    except Exception as e:
        print(f"\n\n❌ Erro inesperado: {e}")
        print("Verifique se o Python está instalado corretamente.")
