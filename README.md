# Sistema de Treinamento Cirúrgico Virtual

## Introdução

Este projeto visa criar um sistema de treinamento cirúrgico em um ambiente virtual para residentes de medicina. A proposta é simular diferentes tipos de procedimentos cirúrgicos, fornecendo um feedback detalhado sobre o desempenho dos usuários em termos de precisão, tempo de execução e erros cometidos. O sistema oferece módulos de treinamento com níveis de complexidade variados, permitindo que os residentes desenvolvam suas habilidades de forma progressiva.

O objetivo principal é facilitar o aprendizado e a prática dos estudantes de medicina, garantindo que possam simular procedimentos cirúrgicos em um ambiente controlado e acessível, mesmo fora do ambiente hospitalar.

## Metodologia

O sistema foi desenvolvido utilizando Python, com uma estrutura orientada a objetos para simular os módulos de treinamento. O projeto inclui as seguintes funcionalidades:

- **Criação de perfis de usuários (residentes)**: Cada usuário tem um perfil com nome, curso e ano de formação.
- **Simulação de procedimentos cirúrgicos**: A simulação inclui a execução de diferentes módulos, como "Sutura Básica" e "Ressecção de Tumor", com resultados de precisão, tempo e erros.
- **Feedback em tempo real**: Após cada procedimento, o sistema oferece feedback detalhado, avaliando o desempenho do residente com base nos resultados.
- **Gráficos de desempenho**: O sistema exibe gráficos para ilustrar a precisão e o tempo gasto em cada módulo.
- **Menu interativo**: O usuário pode selecionar qual residente visualizar através de um menu interativo, tornando o sistema mais dinâmico.

### Estrutura do Código

O código foi organizado da seguinte forma:
- `Usuario`: Classe que representa o residente e armazena seus resultados.
- `Simulador`: Classe que executa as simulações de treinamento, gerando resultados e fornecendo feedback.
- `menu_visualizacao`: Função que permite ao usuário escolher qual residente visualizar através de um menu.

### Bibliotecas Utilizadas

O projeto utiliza as seguintes bibliotecas:
- `random`: Para gerar resultados aleatórios simulando a performance dos usuários.
- `pandas`: Para estruturar os dados de resultados em formato de tabela.
- `matplotlib`: Para gerar gráficos de desempenho visualmente claros.

## Resultados

A simulação permitiu que dois residentes, Gabriel Machado e Camila Padalino, realizassem diferentes procedimentos cirúrgicos. O sistema gerou gráficos de desempenho que mostram a evolução de cada residente em termos de precisão e tempo. Abaixo estão exemplos dos resultados gerados:

- **Precisão**: O gráfico de precisão ao longo dos módulos mostra a melhoria ou declínio do desempenho do residente.
- **Tempo**: O gráfico de tempo ilustra a rapidez com que o residente executou cada procedimento.

## Conclusão

Este sistema representa uma ferramenta poderosa para o treinamento de residentes em um ambiente controlado e simulado. A integração de feedback imediato e a visualização dos dados em gráficos ajuda os usuários a identificar áreas de melhoria, enquanto o menu interativo torna a experiência mais acessível. Com futuras melhorias, o sistema poderá ser expandido para incluir mais tipos de procedimentos e métricas de desempenho.

## Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/KauePastori/Simulation-python.git
