from uteis.modules import *
from uteis.funcs import *


# Resolvendo o problema da geração de grades
def gera_grade(POPULATION_SIZE, MUTATION_RATE, GENERATIONS, selection_method, cross_method):
    # Contadores
    ini = time.time()
    top_fitness = 10000000000
    top_individual = ''
    # Algoritmo acontece por n epocas
    gen = []

    # Inicializar a população
    population = generate_population(POPULATION_SIZE)
    plot = []
    for generations in range(GENERATIONS):
        if top_fitness == 0:
            return top_individual

        #print(generations)

        new_generation = []
        # Gerar a nova geração com os melhores individuos da outra população, vindos da função de seleção
        while len(new_generation) < POPULATION_SIZE and top_fitness != 0:
            # Pega aleatoriamente os 2 melhores individuos
            individuals = select(population, k=3, method=selection_method)

            # Crossover
            new_individuals = crossing(individuals,method=cross_method)

            # Aplica mutação, caso caia neles
            new_individuals = mutate(new_individuals, mutation_rate=MUTATION_RATE)

            # insere os novos individuos gerados na nova população
            for new_individual in new_individuals:
                new_generation.append(new_individual)

            # Não é necessario remover os melhores individuos da população pois o random cuida disso

        if len(new_generation) == POPULATION_SIZE:
            population = deepcopy(new_generation)

        # Responsável por encontrar o melhor indivíduo da população atual com base em sua aptidão
        best_individual = deepcopy(min(population, key=evaluate))
        best_fitness = evaluate(best_individual)

        if top_fitness > best_fitness:
            top_fitness = best_fitness
            top_generation = generations
            top_individual = deepcopy(best_individual)

        #print(f"Erro do melhor individuo da geração: {best_fitness}")
        plot.append({"generation": generations, "score": best_fitness})

    fim = time.time()
    print(f"tempo: {fim-ini}")
    #print(f"Erro do melhor individuo de todas as gerações: {top_fitness}")
    infos = best_evaluate(top_individual)

    return top_individual, top_generation, plot, infos


#POPULATION_SIZE = 100
#MUTATION_RATE = 0.8
#GENERATIONS = 1000
#
## Teste controlado
##i = generate_population(1)[0]
##evaluate(i)
##exit(90)
#
#best, best_gen, plot, infos = gera_grade(POPULATION_SIZE, MUTATION_RATE, GENERATIONS)
#best_gen = best[1]
#best = best[0]
#
#
#print('-='*60)
#print("Avaliando o melhor")
#print(f"Geração {best_gen}")
#
#best_evaluate(best)
#print('-='*60)
#
## Transforma o dicionário em um DataFrame
#df = pd.DataFrame.from_dict(best, orient='index')
#df2 = pd.DataFrame(plot)
#
#df['tempo'] = df['horario'].apply(lambda x: f"{horarios[x[0]][0]} - {horarios[x[0]][1]}")
#df['dia'] = df["horario"].apply(lambda y: y[1])
#df['horario'] =  df['horario'].apply(lambda x: x[0])
#
#print(best)
#df.to_csv('C:/Users/erikd/DataScience/teste.csv')
#df2.to_csv('C:/Users/erikd/DataScience/infos.csv')