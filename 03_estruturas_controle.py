"""
TUTORIAL PYTHON - SEÇÃO 3: ESTRUTURAS DE CONTROLE
==================================================

O QUE SÃO ESTRUTURAS DE CONTROLE?
---------------------------------
Estruturas de controle são comandos que permitem controlar o fluxo
do programa. Elas decidem:
• QUANDO executar um código (condições)
• QUANTAS VEZES executar um código (repetições)
• QUAL caminho seguir no programa

É como dar instruções para alguém:
• "Se estiver chovendo, leve guarda-chuva"
• "Repita 5 vezes: faça exercícios"
• "Enquanto não terminar, continue estudando"

COMO USAR ESTE ARQUIVO:
• Execute diretamente: python 03_estruturas_controle.py
• Ou importe em outro arquivo: from 03_estruturas_controle import demonstrar_estruturas_controle

ORDEM DE ESTUDO:
Este é o QUARTO arquivo a ser estudado, após 02_operadores.py

PRÉ-REQUISITOS:
• Conhecimento dos tipos de dados básicos
• Entendimento dos operadores
• Compreensão de variáveis e valores

Autor: Material de Aula
Data: 25/08
Versão: 3.0 (Organizado e Comentado para Iniciantes)
"""

# =============================================================================
# SEÇÃO 3: ESTRUTURAS DE CONTROLE
# =============================================================================

def demonstrar_estruturas_controle():
    """
    Função que demonstra todas as estruturas de controle do Python.
    
    Esta função mostra como usar if/elif/else, while, for e controle
    de fluxo com exemplos práticos e explicações simples.
    """
    
    print("=" * 60)
    print("SEÇÃO 3: ESTRUTURAS DE CONTROLE")
    print("=" * 60)
    
    # =====================================================================
    # 1. ESTRUTURA CONDICIONAL - TOMAR DECISÕES
    # =====================================================================
    print("\n1. ESTRUTURA CONDICIONAL - TOMAR DECISÕES")
    print("-" * 60)
    
    print("As estruturas condicionais permitem que o programa tome decisões")
    print("baseadas em condições (True ou False)")
    print()
    
    # Estrutura básica: if, elif, else
    print("ESTRUTURA BÁSICA: if, elif, else")
    print("-" * 40)
    
    idade = 18
    print(f"Exemplo com idade: {idade} anos")
    
    if idade < 18:
        print("   • if idade < 18: Se a idade for menor que 18")
        print("   • Resultado: Menor de idade")
    elif idade == 18:
        print("   • elif idade == 18: Senão, se a idade for exatamente 18")
        print("   • Resultado: Tem exatamente 18 anos")
    else:
        print("   • else: Senão (se nenhuma das condições acima for verdadeira)")
        print("   • Resultado: Maior de idade")
    
    print("\nCOMO FUNCIONA:")
    print("   • if: 'Se esta condição for verdadeira, execute este código'")
    print("   • elif: 'Senão, se esta outra condição for verdadeira, execute este código'")
    print("   • else: 'Senão (se nenhuma condição for verdadeira), execute este código'")
    
    # Exemplo com múltiplas condições
    print("\nEXEMPLO COM MÚLTIPLAS CONDIÇÕES:")
    print("-" * 40)
    
    nota = 85
    print(f"Exemplo com nota: {nota}")
    
    if nota >= 90:
        conceito = "A"
        print(f"   • Nota {nota} >= 90: Conceito {conceito}")
    elif nota >= 80:
        conceito = "B"
        print(f"   • Nota {nota} >= 80: Conceito {conceito}")
    elif nota >= 70:
        conceito = "C"
        print(f"   • Nota {nota} >= 70: Conceito {conceito}")
    elif nota >= 60:
        conceito = "D"
        print(f"   • Nota {nota} >= 60: Conceito {conceito}")
    else:
        conceito = "F"
        print(f"   • Nota {nota} < 60: Conceito {conceito}")
    
    print(f"   • Resultado final: Nota {nota} = Conceito {conceito}")
    
    # =====================================================================
    # 2. ESTRUTURA DE REPETIÇÃO - while
    # =====================================================================
    print("\n\n2. ESTRUTURA DE REPETIÇÃO - while")
    print("-" * 60)
    
    print("O while executa um código ENQUANTO uma condição for verdadeira")
    print("É como dizer: 'Enquanto não terminar, continue fazendo'")
    print()
    
    print("EXEMPLO SIMPLES:")
    print("-" * 40)
    
    # Loop while - executa enquanto a condição for verdadeira
    contador = 0
    print("   • Iniciamos com contador = 0")
    print("   • while contador < 5: Enquanto o contador for menor que 5")
    
    while contador < 5:
        print(f"     - Contador: {contador}")
        contador += 1  # Aumenta o contador em 1
        print(f"     - Após incremento: contador = {contador}")
    
    print("   • Loop while finalizado! (contador não é mais < 5)")
    
    print("\nCOMO FUNCIONA O while:")
    print("   • Verifica a condição (contador < 5)")
    print("   • Se for True: executa o código dentro do while")
    print("   • No final, volta a verificar a condição")
    print("   • Repete até a condição ser False")
    print("   • IMPORTANTE: Sempre deve haver uma forma de sair do loop!")
    
    # =====================================================================
    # 3. ESTRUTURA DE REPETIÇÃO - for
    # =====================================================================
    print("\n\n3. ESTRUTURA DE REPETIÇÃO - for")
    print("-" * 60)
    
    print("O for itera sobre uma sequência (lista, string, range, etc.)")
    print("É como dizer: 'Para cada item nesta lista, faça algo'")
    print()
    
    print("EXEMPLO COM LISTA:")
    print("-" * 40)
    
    # Loop for - itera sobre uma sequência
    frutas = ["maçã", "banana", "laranja", "uva"]
    print(f"   • Lista de frutas: {frutas}")
    print("   • for fruta in frutas: Para cada fruta na lista frutas")
    
    for fruta in frutas:
        print(f"     - Fruta: {fruta}")
    
    print("   • Loop for finalizado!")
    
    print("\nEXEMPLO COM range():")
    print("-" * 40)
    
    # Utilizando range() no for
    print("   • range(5) gera: 0, 1, 2, 3, 4")
    print("   • for i in range(5): Para cada número de 0 a 4")
    
    for i in range(5):  # range(5) gera: 0, 1, 2, 3, 4
        print(f"     - Valor de i: {i}")
    
    print("\nEXEMPLO COM range(2, 10, 2):")
    print("-" * 40)
    
    # Range com início, fim e passo
    print("   • range(2, 10, 2): Inicia em 2, vai até 9, passo 2")
    print("   • Gera: 2, 4, 6, 8")
    
    for i in range(2, 10, 2):  # Inicia em 2, vai até 9, passo 2
        print(f"     - Número par: {i}")
    
    print("\nCOMO FUNCIONA O for:")
    print("   • Pega o primeiro item da sequência")
    print("   • Executa o código para esse item")
    print("   • Pega o próximo item")
    print("   • Repete até não haver mais itens")
    print("   • Não precisa se preocupar com contadores!")
    
    # =====================================================================
    # 4. CONTROLE DE FLUXO - break e continue
    # =====================================================================
    print("\n\n4. CONTROLE DE FLUXO - break e continue")
    print("-" * 60)
    
    print("break e continue permitem controlar melhor os loops")
    print("• break: Para o loop completamente")
    print("• continue: Pula para a próxima iteração")
    print()
    
    print("EXEMPLO COM break:")
    print("-" * 40)
    
    # break - interrompe o loop completamente
    print("   • for numero in range(10): Para cada número de 0 a 9")
    print("   • if numero == 7: Se o número for 7")
    print("   • break: Para o loop completamente")
    
    for numero in range(10):
        if numero == 7:
            print(f"     - Número 7 encontrado! Parando o loop com break.")
            break
        print(f"     - Número: {numero}")
    
    print("   • Loop interrompido pelo break!")
    
    print("\nEXEMPLO COM continue:")
    print("-" * 40)
    
    # continue - pula para a próxima iteração
    print("   • for numero in range(10): Para cada número de 0 a 9")
    print("   • if numero % 2 == 0: Se o número for par")
    print("   • continue: Pula para o próximo número")
    print("   • Só imprime números ímpares")
    
    for numero in range(10):
        if numero % 2 == 0:
            print(f"     - Número par encontrado, pulando com continue: {numero}")
            continue
        print(f"     - Número ímpar: {numero}")
    
    print("\nDIFERENÇA ENTRE break E continue:")
    print("   • break: Para o loop completamente, não executa mais nada")
    print("   • continue: Pula apenas esta iteração, continua com a próxima")
    
    # =====================================================================
    # RESUMO DAS ESTRUTURAS DE CONTROLE
    # =====================================================================
    print("\n\nRESUMO DAS ESTRUTURAS DE CONTROLE:")
    print("-" * 60)
    print("CONDICIONAIS:")
    print("   • if: Se uma condição for verdadeira")
    print("   • elif: Senão, se outra condição for verdadeira")
    print("   • else: Senão (se nenhuma condição for verdadeira)")
    print()
    print("REPETIÇÃO:")
    print("   • while: Repete enquanto uma condição for verdadeira")
    print("   • for: Repete para cada item em uma sequência")
    print()
    print("CONTROLE DE FLUXO:")
    print("   • break: Para o loop completamente")
    print("   • continue: Pula para a próxima iteração")
    
    print("\n" + "-" * 60)
    print("FIM DA SEÇÃO 3 - ESTRUTURAS DE CONTROLE")
    print("-" * 60)
    
    # =====================================================================
    # PRÓXIMOS PASSOS
    # =====================================================================
    print("\nPRÓXIMOS PASSOS:")
    print("-" * 60)
    print("Agora que você aprendeu as estruturas de controle, continue com:")
    print("• 04_funcoes.py - Funções")
    print("• 05_poo.py - Programação Orientada a Objetos")
    print("• 06_exemplos_avancados.py - Exemplos avançados")
    print()
    print("Execute: python 04_funcoes.py")

# =============================================================================
# EXECUÇÃO INDEPENDENTE
# =============================================================================

if __name__ == "__main__":
    """
    Este bloco executa quando o arquivo é executado diretamente.
    Permite que cada arquivo funcione independentemente.
    """
    print("🚀 INICIANDO TUTORIAL PYTHON - SEÇÃO 3: ESTRUTURAS DE CONTROLE")
    print("=" * 80)
    print()
    print("Este arquivo pode ser executado independentemente!")
    print("Execute: python 03_estruturas_controle.py")
    print()
    print("Pressione Enter para começar...")
    
    try:
        input()  # Aguarda o usuário pressionar Enter
        demonstrar_estruturas_controle()
    except KeyboardInterrupt:
        print("\n\n❌ Tutorial interrompido pelo usuário.")
        print("Execute novamente: python 03_estruturas_controle.py")
    except Exception as e:
        print(f"\n\n❌ Erro inesperado: {e}")
        print("Verifique se o Python está instalado corretamente.")
