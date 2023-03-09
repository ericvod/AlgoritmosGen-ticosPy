import random

# Parâmetros do algoritmo genético
tam_população = 50
num_genes = 20
taxa_mutacao = 0.1
geracoes = 10000
dificuldade = 0
taxa_aumento_dificuldade = 0.1

# Criação da população inicial de maneira aleatória
populacao = []
for i in range(tam_população):
    individual = []
    for j in range(num_genes):
        gene = random.randint(0, 1)
        individual.append(gene)
    populacao.append(individual)

# Função fitness
def fitness(individual):
    return sum(individual)

# Algoritmo genético
for gen in range(geracoes):
    # Calcular fitness de cada indivíduo
    pontuacao_individuo_fitness = [fitness(individual) for individual in populacao]
    
    # Imprimir número de sobreviventes e mortos da geração atual
    sobreviventes = sum([pontuacao > dificuldade for pontuacao in pontuacao_individuo_fitness])
    mortos = len(populacao) - sobreviventes
    print("Geração {}: {} sobreviventes, {} mortos".format(gen, sobreviventes, mortos))

    # Verificar se a dificuldade vai aumentar ou não
    if taxa_aumento_dificuldade > random.uniform(0.0, 1.0):
        dificuldade += 0.05
    
    # Se a população inteira morreu, vamos encerrar o algoritmo
    if sobreviventes == 0:
        break
    # Se sobrar apenas 1 indivíduo, ele não poderá se reproduzir, ou seja, vamos encerrar o algoritmo
    if sobreviventes == 1:
        print("Há apenas 1 sobrevivente, não é mais possível a população se reproduzir!")
        break
    
    # Selecionar os indivíduos que sobreviveram para cruzamento
    pais = []
    for i in range(sobreviventes):
        if random.random() < pontuacao_individuo_fitness[i]:
            pais.append(populacao[i])
    
    # Cruzamento e mutação dos indivíduos selecionados
    filhos = []
    while len(filhos) < random.randint(0, tam_população):
        parent1 = random.choice(pais)
        parent2 = random.choice(pais)
        filho = []
        for i in range(num_genes):
            if random.random() < taxa_mutacao:
                gene = random.randint(0, 1)
            else:
                gene = parent1[i] if random.random() < 0.5 else parent2[i]
            filho.append(gene)
        filhos.append(filho)
    
    # Somar população anterior com a nova
    populacao += filhos