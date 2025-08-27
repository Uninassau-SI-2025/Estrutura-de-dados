"""
TUTORIAL PYTHON - SEÇÃO 5: PROGRAMAÇÃO ORIENTADA A OBJETOS (POO)
==================================================================

O QUE É PROGRAMAÇÃO ORIENTADA A OBJETOS?
----------------------------------------
POO é uma forma de organizar o código criando "objetos" que representam
coisas do mundo real. É como criar um "molde" (classe) para fabricar
objetos (instâncias).

EXEMPLOS DA VIDA REAL:
• Classe "Carro": molde para fabricar carros
• Objeto "meu_carro": um carro específico fabricado
• Atributos: cor, modelo, ano, placa
• Métodos: ligar, desligar, acelerar, frear

NO PYTHON:
• class: Define uma nova classe
• __init__: Construtor (cria o objeto)
• self: Refere-se ao próprio objeto
• Herança: Uma classe pode herdar de outra
• Polimorfismo: Mesmo método, comportamentos diferentes

COMO USAR ESTE ARQUIVO:
• Execute diretamente: python 05_poo.py
• Ou importe em outro arquivo: from 05_poo import demonstrar_poo

ORDEM DE ESTUDO:
Este é o SEXTO arquivo a ser estudado, após 04_funcoes.py

PRÉ-REQUISITOS:
• Conhecimento dos tipos de dados básicos
• Entendimento dos operadores
• Compreensão das estruturas de controle
• Familiaridade com funções
• Compreensão de variáveis e valores

Autor: Material de Aula
Data: 25/08
Versão: 3.0 (Organizado e Comentado para Iniciantes)
"""

# =============================================================================
# SEÇÃO 5: PROGRAMAÇÃO ORIENTADA A OBJETOS
# =============================================================================

def demonstrar_poo():
    """
    Função que demonstra todos os conceitos de POO do Python.
    
    Esta função mostra como criar classes, objetos, herança e polimorfismo
    com exemplos práticos e explicações simples.
    """
    
    print("=" * 60)
    print("SEÇÃO 5: PROGRAMAÇÃO ORIENTADA A OBJETOS")
    print("=" * 60)
    
    # =====================================================================
    # 1. CLASSE BÁSICA - CRIANDO UM MOLDE
    # =====================================================================
    print("\n1. CLASSE BÁSICA - CRIANDO UM MOLDE")
    print("-" * 60)
    
    class Pessoa:
        """
        Classe base que representa uma pessoa.
        
        Esta é uma classe pai (superclasse) que define atributos e métodos
        básicos que serão herdados por outras classes.
        
        PENSE ASSIM: É como um "molde" para criar pessoas.
        """
        
        def __init__(self, nome, idade):
            """
            Construtor da classe Pessoa.
            
            O __init__ é chamado automaticamente quando criamos um objeto.
            É como "preparar" o objeto com suas características iniciais.
            
            Args:
                nome (str): Nome da pessoa
                idade (int): Idade da pessoa
            """
            # self.nome = nome: Cria um atributo 'nome' para este objeto
            # self.idade = idade: Cria um atributo 'idade' para este objeto
            self.nome = nome
            self.idade = idade
            print(f"   • Criando pessoa: {nome}, {idade} anos")
        
        def apresentar(self):
            """
            Método que apresenta a pessoa.
            
            Um método é uma função que pertence à classe.
            É como uma "ação" que o objeto pode fazer.
            
            Imprime uma mensagem com o nome e idade da pessoa.
            """
            print(f"   • Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
        
        def fazer_aniversario(self):
            """
            Método que incrementa a idade da pessoa.
            
            Este método modifica um atributo do objeto.
            É como uma "ação" que muda o estado do objeto.
            
            Returns:
                int: Nova idade
            """
            self.idade += 1  # Aumenta a idade em 1
            print(f"   • {self.nome} fez aniversário! Nova idade: {self.idade}")
            return self.idade
    
    print("DEFININDO A CLASSE:")
    print("   • class Pessoa: Define uma nova classe chamada 'Pessoa'")
    print("   • __init__(self, nome, idade): Construtor da classe")
    print("   • self.nome = nome: Cria atributo 'nome' para o objeto")
    print("   • self.idade = idade: Cria atributo 'idade' para o objeto")
    print("   • apresentar(): Método que apresenta a pessoa")
    print("   • fazer_aniversario(): Método que aumenta a idade")
    
    print("\nCOMO FUNCIONA:")
    print("   • class: Palavra-chave para criar uma classe")
    print("   • __init__: Método especial chamado automaticamente")
    print("   • self: Refere-se ao próprio objeto sendo criado")
    print("   • Atributos: Características do objeto (nome, idade)")
    print("   • Métodos: Ações que o objeto pode fazer")
    
    # =====================================================================
    # 2. CRIANDO OBJETOS (INSTÂNCIAS)
    # =====================================================================
    print("\n\n2. CRIANDO OBJETOS (INSTÂNCIAS)")
    print("-" * 60)
    
    print("CRIANDO OBJETOS DA CLASSE PESSOA:")
    print("-" * 40)
    
    # Criando instâncias das classes
    print("   • p1 = Pessoa('Mariana', 28): Cria um objeto pessoa")
    p1 = Pessoa("Mariana", 28)
    
    print("   • Agora temos um objeto 'p1' com nome 'Mariana' e idade 28")
    print("   • p1 é uma 'instância' da classe Pessoa")
    
    print("\nUSANDO OS MÉTODOS DO OBJETO:")
    print("-" * 40)
    
    print("   • p1.apresentar(): Chama o método 'apresentar' do objeto p1")
    p1.apresentar()
    
    print("   • p1.fazer_aniversario(): Chama o método 'fazer_aniversario'")
    p1.fazer_aniversario()
    
    print("\nCOMO FUNCIONA:")
    print("   • Pessoa('Mariana', 28): Chama o construtor __init__")
    print("   • Cria um objeto com nome='Mariana' e idade=28")
    print("   • p1 = ...: Guarda o objeto na variável p1")
    print("   • p1.apresentar(): Executa o método 'apresentar' do objeto p1")
    
    # =====================================================================
    # 3. HERANÇA - UMA CLASSE HERDA DE OUTRA
    # =====================================================================
    print("\n\n3. HERANÇA - UMA CLASSE HERDA DE OUTRA")
    print("-" * 60)
    
    print("Herança permite que uma classe 'herde' atributos e métodos de outra")
    print("É como dizer: 'Aluno é um tipo de Pessoa'")
    print()
    
    class Aluno(Pessoa):
        """
        Classe Aluno que herda de Pessoa.
        
        Esta classe demonstra o conceito de herança, onde Aluno
        herda todos os atributos e métodos da classe Pessoa.
        
        PENSE ASSIM: Aluno é um tipo especial de Pessoa.
        """
        
        def __init__(self, nome, idade, matricula):
            """
            Construtor da classe Aluno.
            
            Args:
                nome (str): Nome do aluno
                idade (int): Idade do aluno
                matricula (str): Número de matrícula
            """
            # Chama o construtor da classe pai (Pessoa)
            # super().__init__(nome, idade): Executa o __init__ da classe Pessoa
            super().__init__(nome, idade)
            self.matricula = matricula
            print(f"   • Criando aluno com matrícula: {matricula}")
        
        def apresentar(self):
            """
            Sobrescreve o método apresentar da classe pai.
            
            Este é um exemplo de polimorfismo, onde o mesmo método
            tem comportamentos diferentes em classes diferentes.
            """
            print(f"   • Olá, sou o aluno {self.nome}, tenho {self.idade} anos e minha matrícula é {self.matricula}.")
        
        def estudar(self, disciplina):
            """
            Método específico da classe Aluno.
            
            Este método só existe na classe Aluno, não na classe Pessoa.
            
            Args:
                disciplina (str): Nome da disciplina
            """
            print(f"   • {self.nome} está estudando {disciplina}.")
    
    print("DEFININDO A CLASSE ALUNO:")
    print("   • class Aluno(Pessoa): Aluno herda de Pessoa")
    print("   • super().__init__(nome, idade): Chama construtor da classe pai")
    print("   • self.matricula = matricula: Adiciona atributo específico")
    print("   • apresentar(): Sobrescreve método da classe pai")
    print("   • estudar(): Método específico da classe Aluno")
    
    print("\nCRIANDO UM ALUNO:")
    print("-" * 40)
    
    print("   • a1 = Aluno('João', 20, '20231234'): Cria um aluno")
    a1 = Aluno("João", 20, "20231234")
    
    print("   • a1.apresentar(): Usa o método sobrescrito")
    a1.apresentar()
    
    print("   • a1.estudar('Python'): Usa método específico do aluno")
    a1.estudar("Python")
    
    print("\nCOMO FUNCIONA A HERANÇA:")
    print("   • Aluno herda nome e idade de Pessoa")
    print("   • Aluno adiciona matrícula (atributo específico)")
    print("   • Aluno pode usar métodos de Pessoa (fazer_aniversario)")
    print("   • Aluno pode sobrescrever métodos (apresentar)")
    print("   • Aluno pode ter métodos próprios (estudar)")
    
    # =====================================================================
    # 4. OUTRA CLASSE QUE HERDA DE PESSOA
    # =====================================================================
    print("\n\n4. OUTRA CLASSE QUE HERDA DE PESSOA")
    print("-" * 60)
    
    class Professor(Pessoa):
        """
        Classe Professor que herda de Pessoa.
        
        Outro exemplo de herança, demonstrando como diferentes
        classes podem herdar da mesma classe base.
        
        PENSE ASSIM: Professor é outro tipo especial de Pessoa.
        """
        
        def __init__(self, nome, idade, disciplina):
            """
            Construtor da classe Professor.
            
            Args:
                nome (str): Nome do professor
                idade (int): Idade do professor
                disciplina (str): Disciplina que leciona
            """
            super().__init__(nome, idade)
            self.disciplina = disciplina
            print(f"   • Criando professor de: {disciplina}")
        
        def apresentar(self):
            """
            Sobrescreve o método apresentar da classe pai.
            """
            print(f"   • Olá, sou o professor {self.nome}, tenho {self.idade} anos e leciono {self.disciplina}.")
        
        def dar_aula(self):
            """
            Método específico da classe Professor.
            """
            print(f"   • {self.nome} está dando aula de {self.disciplina}.")
    
    print("CRIANDO UM PROFESSOR:")
    print("-" * 40)
    
    print("   • prof1 = Professor('Carlos', 45, 'Matemática'): Cria um professor")
    prof1 = Professor("Carlos", 45, "Matemática")
    
    print("   • prof1.apresentar(): Usa o método sobrescrito")
    prof1.apresentar()
    
    print("   • prof1.dar_aula(): Usa método específico do professor")
    prof1.dar_aula()
    
    # =====================================================================
    # 5. DEMONSTRANDO HERANÇA
    # =====================================================================
    print("\n\n5. DEMONSTRANDO HERANÇA")
    print("-" * 60)
    
    print("TODOS OS OBJETOS PODEM USAR MÉTODOS DA CLASSE PESSOA:")
    print("-" * 60)
    
    print("   • p1.fazer_aniversario(): Pessoa faz aniversário")
    p1.fazer_aniversario()
    
    print("   • a1.fazer_aniversario(): Aluno faz aniversário")
    a1.fazer_aniversario()
    
    print("   • prof1.fazer_aniversario(): Professor faz aniversário")
    prof1.fazer_aniversario()
    
    print("\nCOMO FUNCIONA:")
    print("   • Todos herdam o método fazer_aniversario de Pessoa")
    print("   • Cada um tem seu próprio nome e idade")
    print("   • O método funciona igual para todos")
    
    # =====================================================================
    # 6. POLIMORFISMO - MESMO MÉTODO, COMPORTAMENTOS DIFERENTES
    # =====================================================================
    print("\n\n6. POLIMORFISMO - MESMO MÉTODO, COMPORTAMENTOS DIFERENTES")
    print("-" * 60)
    
    def apresentar_pessoa(pessoa):
        """
        Função que demonstra polimorfismo.
        
        Esta função pode receber qualquer objeto que tenha o método 'apresentar',
        demonstrando o conceito de polimorfismo em Python.
        
        Args:
            pessoa: Objeto que deve ter o método 'apresentar'
        """
        print(f"\n   • Função apresentar_pessoa chamada para: {type(pessoa).__name__}")
        pessoa.apresentar()
    
    print("DEMONSTRAÇÃO DE POLIMORFISMO:")
    print("-" * 40)
    print("   • A mesma função funciona com diferentes tipos de objetos:")
    
    apresentar_pessoa(p1)    # Pessoa
    apresentar_pessoa(a1)    # Aluno
    apresentar_pessoa(prof1) # Professor
    
    print("\nCOMO FUNCIONA O POLIMORFISMO:")
    print("   • A função apresentar_pessoa não sabe que tipo de objeto recebe")
    print("   • Só sabe que o objeto tem um método 'apresentar'")
    print("   • Cada objeto executa seu próprio método 'apresentar'")
    print("   • Resultado: Comportamentos diferentes para o mesmo comando")
    
    # =====================================================================
    # RESUMO DA POO
    # =====================================================================
    print("\n\nRESUMO DA PROGRAMAÇÃO ORIENTADA A OBJETOS:")
    print("-" * 60)
    print("CONCEITOS BÁSICOS:")
    print("   • Classe: Molde para criar objetos")
    print("   • Objeto: Instância de uma classe")
    print("   • Atributo: Característica do objeto")
    print("   • Método: Ação que o objeto pode fazer")
    print()
    print("HERANÇA:")
    print("   • Uma classe pode herdar de outra")
    print("   • Herda atributos e métodos")
    print("   • Pode adicionar novos atributos e métodos")
    print("   • Pode sobrescrever métodos herdados")
    print()
    print("POLIMORFISMO:")
    print("   • Mesmo método, comportamentos diferentes")
    print("   • Diferentes classes podem responder ao mesmo comando")
    print("   • Torna o código mais flexível e reutilizável")
    
    print("\n" + "-" * 60)
    print("FIM DA SEÇÃO 5 - PROGRAMAÇÃO ORIENTADA A OBJETOS")
    print("-" * 60)
    
    # =====================================================================
    # PRÓXIMOS PASSOS
    # =====================================================================
    print("\nPRÓXIMOS PASSOS:")
    print("-" * 60)
    print("Agora que você aprendeu POO, continue com:")
    print("• 06_exemplos_avancados.py - Exemplos avançados")
    print()
    print("Execute: python 06_exemplos_avancados.py")

# =============================================================================
# EXECUÇÃO INDEPENDENTE
# =============================================================================

if __name__ == "__main__":
    """
    Este bloco executa quando o arquivo é executado diretamente.
    Permite que cada arquivo funcione independentemente.
    """
    print("🚀 INICIANDO TUTORIAL PYTHON - SEÇÃO 5: PROGRAMAÇÃO ORIENTADA A OBJETOS")
    print("=" * 80)
    print()
    print("Este arquivo pode ser executado independentemente!")
    print("Execute: python 05_poo.py")
    print()
    print("Pressione Enter para começar...")
    
    try:
        input()  # Aguarda o usuário pressionar Enter
        demonstrar_poo()
    except KeyboardInterrupt:
        print("\n\n❌ Tutorial interrompido pelo usuário.")
        print("Execute novamente: python 05_poo.py")
    except Exception as e:
        print(f"\n\n❌ Erro inesperado: {e}")
        print("Verifique se o Python está instalado corretamente.")
