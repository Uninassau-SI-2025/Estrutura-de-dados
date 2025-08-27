"""
TUTORIAL PYTHON - SEÇÃO 4: FUNÇÕES
===================================

O QUE SÃO FUNÇÕES?
------------------
Funções são blocos de código reutilizáveis que realizam uma tarefa específica.
É como criar uma "receita" que pode ser usada várias vezes.

EXEMPLOS DA VIDA REAL:
• Receita de bolo: ingredientes (parâmetros) → bolo (resultado)
• Máquina de lavar: roupas sujas (entrada) → roupas limpas (saída)
• Calculadora: números (entrada) → resultado (saída)

NO PYTHON:
• def: Define uma nova função
• Parâmetros: Dados que a função recebe
• Return: Valor que a função retorna
• Chamada: Como usar a função

COMO USAR ESTE ARQUIVO:
• Execute diretamente: python 04_funcoes.py
• Ou importe em outro arquivo: from 04_funcoes import demonstrar_funcoes

ORDEM DE ESTUDO:
Este é o QUINTO arquivo a ser estudado, após 03_estruturas_controle.py

PRÉ-REQUISITOS:
• Conhecimento dos tipos de dados básicos
• Entendimento dos operadores
• Compreensão das estruturas de controle
• Familiaridade com variáveis e valores

Autor: Material de Aula
Data: 25/08
Versão: 3.0 (Organizado e Comentado para Iniciantes)
"""

# =============================================================================
# SEÇÃO 4: FUNÇÕES
# =============================================================================

def demonstrar_funcoes():
    """
    Função que demonstra todos os conceitos de funções do Python.
    
    Esta função mostra como criar e usar diferentes tipos de funções
    com exemplos práticos e explicações simples.
    """
    
    print("=" * 60)
    print("SEÇÃO 4: FUNÇÕES")
    print("=" * 60)
    
    # =====================================================================
    # 1. FUNÇÃO SIMPLES SEM PARÂMETROS
    # =====================================================================
    print("\n1. FUNÇÃO SIMPLES SEM PARÂMETROS")
    print("-" * 60)
    
    def saudacao():
        """
        Função simples sem parâmetros.
        
        Esta função imprime uma mensagem de boas-vindas.
        É um exemplo básico de como definir uma função em Python.
        """
        print("   • Olá! Bem-vindo(a) ao curso de Python.")
    
    print("DEFININDO A FUNÇÃO:")
    print("   • def saudacao(): Define uma função chamada 'saudacao'")
    print("   • () vazio significa que não recebe parâmetros")
    print("   • print(...): O que a função faz quando é chamada")
    
    print("\nCHAMANDO A FUNÇÃO:")
    print("   • saudacao() - Executa o código dentro da função")
    saudacao()
    
    print("\nCOMO FUNCIONA:")
    print("   • def: Palavra-chave para definir uma função")
    print("   • saudacao: Nome da função (você escolhe)")
    print("   • (): Parênteses para parâmetros (vazio neste caso)")
    print("   • : Dois pontos indicam o início do código da função")
    print("   • Código indentado: Faz parte da função")
    
    # =====================================================================
    # 2. FUNÇÃO COM PARÂMETROS E RETORNO
    # =====================================================================
    print("\n\n2. FUNÇÃO COM PARÂMETROS E RETORNO")
    print("-" * 60)
    
    def soma(a, b):
        """
        Função que soma dois números.
        
        Args:
            a (int/float): Primeiro número
            b (int/float): Segundo número
        
        Returns:
            int/float: Soma dos dois números
        """
        resultado = a + b
        return resultado
    
    print("DEFININDO A FUNÇÃO:")
    print("   • def soma(a, b): Define função 'soma' com dois parâmetros")
    print("   • a, b: Parâmetros que a função recebe")
    print("   • resultado = a + b: Faz a soma")
    print("   • return resultado: Retorna o valor calculado")
    
    print("\nUSANDO A FUNÇÃO:")
    print("   • resultado = soma(5, 3): Chama a função e guarda o resultado")
    resultado = soma(5, 3)
    print(f"   • Resultado da soma: {resultado}")
    
    print("\nCOMO FUNCIONA:")
    print("   • Parâmetros: São como variáveis que recebem valores")
    print("   • a = 5, b = 3: Quando chamamos soma(5, 3)")
    print("   • return: Envia o valor de volta para quem chamou a função")
    print("   • resultado = ...: Guarda o valor retornado")
    
    # =====================================================================
    # 3. FUNÇÃO COM PARÂMETRO COM VALOR PADRÃO
    # =====================================================================
    print("\n\n3. FUNÇÃO COM PARÂMETRO COM VALOR PADRÃO")
    print("-" * 60)
    
    def apresentar(nome, idade=18):
        """
        Função com parâmetro com valor padrão.
        
        Args:
            nome (str): Nome da pessoa
            idade (int, optional): Idade da pessoa. Padrão é 18.
        """
        print(f"   • Nome: {nome}, Idade: {idade}")
    
    print("DEFININDO A FUNÇÃO:")
    print("   • def apresentar(nome, idade=18):")
    print("   • nome: Parâmetro obrigatório")
    print("   • idade=18: Parâmetro com valor padrão (18)")
    
    print("\nUSANDO A FUNÇÃO:")
    print("   • apresentar('João'): Usa idade padrão (18)")
    apresentar("João")  # Usa idade padrão (18)
    
    print("   • apresentar('Maria', 25): Especifica idade")
    apresentar("Maria", 25)  # Especifica idade
    
    print("\nCOMO FUNCIONA:")
    print("   • Parâmetros com = têm valores padrão")
    print("   • Se não especificarmos, usa o valor padrão")
    print("   • Se especificarmos, usa o valor que passamos")
    
    # =====================================================================
    # 4. FUNÇÃO QUE RETORNA MÚLTIPLOS VALORES
    # =====================================================================
    print("\n\n4. FUNÇÃO QUE RETORNA MÚLTIPLOS VALORES")
    print("-" * 60)
    
    def operacoes(a, b):
        """
        Função que retorna múltiplos valores.
        
        Args:
            a (int/float): Primeiro número
            b (int/float): Segundo número
        
        Returns:
            tuple: (soma, subtracao, multiplicacao, divisao)
        """
        soma = a + b
        subtracao = a - b
        multiplicacao = a * b
        
        # Tratamento de erro para divisão por zero
        if b != 0:
            divisao = a / b
        else:
            divisao = "Erro: divisão por zero"
        
        return soma, subtracao, multiplicacao, divisao
    
    print("DEFININDO A FUNÇÃO:")
    print("   • Calcula 4 operações matemáticas")
    print("   • return soma, subtracao, multiplicacao, divisao")
    print("   • Retorna múltiplos valores separados por vírgula")
    
    print("\nUSANDO A FUNÇÃO:")
    print("   • s, sub, mult, div = operacoes(10, 2)")
    print("   • Cada variável recebe um valor retornado")
    s, sub, mult, div = operacoes(10, 2)
    print(f"   • Soma: {s}")
    print(f"   • Subtração: {sub}")
    print(f"   • Multiplicação: {mult}")
    print(f"   • Divisão: {div}")
    
    print("\nCOMO FUNCIONA:")
    print("   • return pode retornar vários valores")
    print("   • s, sub, mult, div = ...: Desempacota os valores")
    print("   • s recebe o primeiro valor, sub o segundo, etc.")
    
    # =====================================================================
    # 5. FUNÇÃO COM PARÂMETROS VARIÁVEIS (*args)
    # =====================================================================
    print("\n\n5. FUNÇÃO COM PARÂMETROS VARIÁVEIS (*args)")
    print("-" * 60)
    
    def listar_nomes(*nomes):
        """
        Função com parâmetros variáveis (*args).
        
        Args:
            *nomes: Quantidade variável de nomes
        """
        print(f"   • Lista de nomes recebidos ({len(nomes)} nomes):")
        for i, nome in enumerate(nomes, 1):
            print(f"     {i}. {nome}")
    
    print("DEFININDO A FUNÇÃO:")
    print("   • def listar_nomes(*nomes):")
    print("   • *nomes: Aceita qualquer quantidade de nomes")
    print("   • len(nomes): Conta quantos nomes foram passados")
    
    print("\nUSANDO A FUNÇÃO:")
    print("   • listar_nomes('Ana', 'Bruno', 'Carlos'): 3 nomes")
    listar_nomes("Ana", "Bruno", "Carlos")
    
    print("   • listar_nomes('Fernanda'): 1 nome")
    listar_nomes("Fernanda")
    
    print("\nCOMO FUNCIONA:")
    print("   • *args: Aceita qualquer quantidade de parâmetros")
    print("   • Os parâmetros viram uma lista dentro da função")
    print("   • enumerate(nomes, 1): Numera os itens começando em 1")
    
    # =====================================================================
    # 6. FUNÇÃO COM PARÂMETROS NOMEADOS (**kwargs)
    # =====================================================================
    print("\n\n6. FUNÇÃO COM PARÂMETROS NOMEADOS (**kwargs)")
    print("-" * 60)
    
    def exibir_dados(**dados):
        """
        Função com parâmetros nomeados (**kwargs).
        
        Args:
            **dados: Dicionário de dados nomeados
        """
        print(f"   • Dados recebidos ({len(dados)} itens):")
        for chave, valor in dados.items():
            print(f"     {chave}: {valor}")
    
    print("DEFININDO A FUNÇÃO:")
    print("   • def exibir_dados(**dados):")
    print("   • **dados: Aceita parâmetros nomeados")
    print("   • dados.items(): Percorre chave e valor")
    
    print("\nUSANDO A FUNÇÃO:")
    print("   • exibir_dados(nome='Lucas', idade=30, cidade='São Paulo')")
    exibir_dados(nome="Lucas", idade=30, cidade="São Paulo")
    
    print("   • exibir_dados(produto='Notebook', preco=3500, estoque=12)")
    exibir_dados(produto="Notebook", preco=3500, estoque=12)
    
    print("\nCOMO FUNCIONA:")
    print("   • **kwargs: Aceita parâmetros nomeados")
    print("   • nome='Lucas': nome é a chave, 'Lucas' é o valor")
    print("   • Dentro da função, vira um dicionário")
    
    # =====================================================================
    # 7. FUNÇÃO COM PARÂMETROS OPCIONAIS
    # =====================================================================
    print("\n\n7. FUNÇÃO COM PARÂMETROS OPCIONAIS")
    print("-" * 60)
    
    def saudacao_personalizada(mensagem="Olá", nome=None):
        """
        Função com parâmetros opcionais.
        
        Args:
            mensagem (str, optional): Mensagem de saudação. Padrão é "Olá".
            nome (str, optional): Nome da pessoa. Padrão é None.
        """
        if nome:
            print(f"   • {mensagem}, {nome}!")
        else:
            print(f"   • {mensagem}!")
    
    print("DEFININDO A FUNÇÃO:")
    print("   • def saudacao_personalizada(mensagem='Olá', nome=None):")
    print("   • mensagem='Olá': Valor padrão")
    print("   • nome=None: Valor padrão None (nada)")
    print("   • if nome: Verifica se nome foi fornecido")
    
    print("\nUSANDO A FUNÇÃO:")
    print("   • saudacao_personalizada(): Usa valores padrão")
    saudacao_personalizada()
    
    print("   • saudacao_personalizada('Bem-vindo'): Especifica mensagem")
    saudacao_personalizada("Bem-vindo")
    
    print("   • saudacao_personalizada('Bom dia', 'Gabriel'): Especifica ambos")
    saudacao_personalizada("Bom dia", "Gabriel")
    
    print("\nCOMO FUNCIONA:")
    print("   • Parâmetros opcionais têm valores padrão")
    print("   • None significa 'nada' ou 'vazio'")
    print("   • if nome: Só executa se nome não for None")
    
    # =====================================================================
    # RESUMO DAS FUNÇÕES
    # =====================================================================
    print("\n\nRESUMO DAS FUNÇÕES:")
    print("-" * 60)
    print("DEFINIÇÃO:")
    print("   • def nome_funcao(parametros):")
    print("   • Código da função (indentado)")
    print("   • return valor (opcional)")
    print()
    print("TIPOS DE PARÂMETROS:")
    print("   • Obrigatórios: nome_funcao(a, b)")
    print("   • Com padrão: nome_funcao(a, b=10)")
    print("   • Variáveis: nome_funcao(*args)")
    print("   • Nomeados: nome_funcao(**kwargs)")
    print()
    print("RETORNO:")
    print("   • return valor: Retorna um valor")
    print("   • return a, b: Retorna múltiplos valores")
    print("   • Sem return: Retorna None")
    
    print("\n" + "-" * 60)
    print("FIM DA SEÇÃO 4 - FUNÇÕES")
    print("-" * 60)
    
    # =====================================================================
    # PRÓXIMOS PASSOS
    # =====================================================================
    print("\nPRÓXIMOS PASSOS:")
    print("-" * 60)
    print("Agora que você aprendeu sobre funções, continue com:")
    print("• 05_poo.py - Programação Orientada a Objetos")
    print("• 06_exemplos_avancados.py - Exemplos avançados")
    print()
    print("Execute: python 05_poo.py")

# =============================================================================
# EXECUÇÃO INDEPENDENTE
# =============================================================================

if __name__ == "__main__":
    """
    Este bloco executa quando o arquivo é executado diretamente.
    Permite que cada arquivo funcione independentemente.
    """
    print("🚀 INICIANDO TUTORIAL PYTHON - SEÇÃO 4: FUNÇÕES")
    print("=" * 80)
    print()
    print("Este arquivo pode ser executado independentemente!")
    print("Execute: python 04_funcoes.py")
    print()
    print("Pressione Enter para começar...")
    
    try:
        input()  # Aguarda o usuário pressionar Enter
        demonstrar_funcoes()
    except KeyboardInterrupt:
        print("\n\n❌ Tutorial interrompido pelo usuário.")
        print("Execute novamente: python 04_funcoes.py")
    except Exception as e:
        print(f"\n\n❌ Erro inesperado: {e}")
        print("Verifique se o Python está instalado corretamente.")
