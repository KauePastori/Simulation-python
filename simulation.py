import random
import pandas as pd
import matplotlib.pyplot as plt

class Usuario:
    """
    Classe que representa um residente ou estudante no sistema de treinamento cirúrgico.
    """
    def __init__(self, nome, curso, ano_formacao):
        self.nome = nome
        self.curso = curso
        self.ano_formacao = ano_formacao
        self.resultados = []

    def adicionar_resultado(self, modulo, precisao, tempo, erros, complexidade, emocional):
        """
        Adiciona um resultado de um módulo de simulação ao perfil do usuário.
        """
        resultado = {
            "modulo": modulo,
            "precisao": precisao,
            "tempo": tempo,
            "erros": erros,
            "complexidade": complexidade,
            "emocional": emocional
        }
        self.resultados.append(resultado)
        print(f"\n[Módulo '{modulo}'] Resultado adicionado com sucesso para {self.nome}.")

    def fornecer_feedback(self):
        """
        Fornece feedback detalhado sobre o desempenho do usuário em cada módulo de treinamento.
        """
        print(f"\nFeedback para {self.nome} ({self.curso}, {self.ano_formacao}):")
        for resultado in self.resultados:
            print(f"\nMódulo: {resultado['modulo']}")
            print(f"Precisão: {resultado['precisao']}%")
            print(f"Tempo: {resultado['tempo']} segundos")
            print(f"Erros cometidos: {resultado['erros']}")
            print(f"Complexidade: {resultado['complexidade']}/5")
            print(f"Estado emocional: {resultado['emocional']}")
            if resultado['precisao'] >= 90:
                print("Desempenho Excelente!")
            elif 80 <= resultado['precisao'] < 90:
                print("Bom desempenho, mas há espaço para melhoria.")
            else:
                print("Precisão abaixo do esperado. Precisa de mais prática.")
    
    def exibir_resultados(self):
        """
        Exibe todos os resultados acumulados do usuário em formato de tabela e gráficos.
        """
        if not self.resultados:
            print(f"{self.nome} ainda não completou nenhum módulo.")
            return
        
        df = pd.DataFrame(self.resultados)
        print(f"\nResultados de {self.nome}:")
        print(df)
        
        # Exibe gráficos de desempenho
        self._plot_resultados(df)

    def _plot_resultados(self, df):
        """
        Gera gráficos de desempenho do usuário ao longo dos módulos, incluindo o nome do residente.
        """
        fig, ax = plt.subplots(1, 2, figsize=(12, 6))

        # Gráfico de Precisão ao longo dos Módulos
        ax[0].plot(df['modulo'], df['precisao'], marker='o', color='blue')
        ax[0].set_title(f'Precisão ao Longo dos Módulos - {self.nome}')
        ax[0].set_xlabel('Módulo')
        ax[0].set_ylabel('Precisão (%)')
        ax[0].set_ylim([60, 100])

        # Gráfico de Tempo por Módulo
        ax[1].bar(df['modulo'], df['tempo'], color='green')
        ax[1].set_title(f'Tempo de Execução por Módulo - {self.nome}')
        ax[1].set_xlabel('Módulo')
        ax[1].set_ylabel('Tempo (segundos)')
        
        plt.tight_layout()
        plt.show()

class Simulador:
    """
    Classe responsável pela simulação dos módulos de treinamento cirúrgico.
    """
    
    @staticmethod
    def simular_modulo(usuario, modulo, complexidade):
        """
        Simula um módulo de treinamento cirúrgico e armazena os resultados no perfil do usuário.
        """
        # Gera resultados aleatórios para precisão, tempo e erros
        precisao = random.randint(70, 100)
        tempo = random.randint(300, 600)
        erros = random.randint(0, 5)

        # Simula estado emocional baseado na complexidade
        emocional = Simulador._determinar_estado_emocional(complexidade)

        # Adiciona o resultado ao perfil do usuário e fornece feedback
        usuario.adicionar_resultado(modulo, precisao, tempo, erros, complexidade, emocional)
        usuario.fornecer_feedback()

    @staticmethod
    def _determinar_estado_emocional(complexidade):
        """
        Determina o estado emocional do usuário durante o procedimento com base na complexidade.
        """
        if complexidade >= 4:
            return random.choice(["Estressado", "Ansioso", "Calmo"])
        else:
            return random.choice(["Confiante", "Relaxado", "Calmo"])

def menu_visualizacao(usuarios):
    """
    Exibe um menu para escolher qual residente visualizar.
    """
    while True:
        print("\n--- Menu de Visualização de Resultados ---")
        for i, usuario in enumerate(usuarios):
            print(f"{i + 1}. Ver resultados de {usuario.nome}")
        print(f"{len(usuarios) + 1}. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        try:
            opcao = int(opcao)
            if 1 <= opcao <= len(usuarios):
                usuarios[opcao - 1].exibir_resultados()
            elif opcao == len(usuarios) + 1:
                print("Saindo...")
                break
            else:
                print("Opção inválida, tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

def main():
    """
    Função principal para simulação do sistema de treinamento cirúrgico.
    """
    # Criação dos usuários
    residente_1 = Usuario("Gabriel Machado", "Medicina", 2024)
    residente_2 = Usuario("Camila Padalino", "Medicina", 2024)

    # Simulação de módulos
    Simulador.simular_modulo(residente_1, "Sutura Básica", 3)
    Simulador.simular_modulo(residente_1, "Dissecção de Vasos", 4)
    
    Simulador.simular_modulo(residente_2, "Ressecção de Tumor", 5)
    Simulador.simular_modulo(residente_2, "Sutura Avançada", 3)
    
    # Lista de usuários
    usuarios = [residente_1, residente_2]
    
    # Exibe o menu para escolher qual residente visualizar
    menu_visualizacao(usuarios)

if __name__ == "__main__":
    main()
