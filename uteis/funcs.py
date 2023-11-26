import random

from uteis.modules import *
from uteis.estruturas import *


def generate_population(size):
    population = []
    profs = list(professores.keys())
    hrs = list(horarios.keys())

    for _ in range(size):
        individuo = deepcopy(disciplinas)
        for key_disc in individuo.keys():
            individuo[key_disc]['professor'] = random.choice(profs)
            individuo[key_disc]['horario'] = [random.choice(hrs), random.choice(dias_semana)]

        population.append(individuo)

    # Gera a população de tamanho size e cada individuo tem o mesmo tamanho de lenght(Padrão)
    return population


def best_evaluate(individual):
    infos = {}
    penalization = 0
    # print(disciplinas)
    profs = dict()
    for disc in individual.keys():
        if individual[disc]['professor'] not in profs.keys():
            profs[individual[disc]['professor']] = {disc: ""}

        profs[individual[disc]['professor']][disc] = individual[disc]["horario"]

    discs = dict()
    for disc in individual.keys():
        if disc not in discs.keys():
            discs[disc] = {"periodo": "", "horario": ""}

        discs[disc]["horario"] = individual[disc]["horario"]
        discs[disc]["periodo"] = individual[disc]["periodo"]
    aux = 0
    # =================================================================================
    # Penalizando materias diferentes no mesmo horario
    for prof in profs.keys():
        aulas = list(profs[prof].values())
        # print(aulas)
        for aula in aulas:
            if aulas.count(aula) > 1:
                # print(f"Professor: {(aulas.count(aula)-1)*penalizacoes['T1']['pontuacao']}")
                penalization += (aulas.count(aula) - 1) * penalizacoes['T1']['pontuacao']

    print(f"Depois de Penalizando materias diferentes no mesmo horario: {penalization - aux}")
    infos['T1'] = penalization - aux
    aux = penalization
    # ==================================================================================
    # Penalizando materias de um mesmo periodo em um mesmo horario e dia
    periodo_disc = {}
    for disc in discs.keys():
        if discs[disc]['periodo'] not in periodo_disc.keys():
            periodo_disc[discs[disc]['periodo']] = []

        periodo_disc[discs[disc]['periodo']].append(discs[disc]['horario'])

    for p in periodo_disc.keys():
        # print(p)
        # print(periodo_disc[p])

        for d in periodo_disc[p]:
            # print(f"{d}: {periodo_disc[p].count(d)}")
            if periodo_disc[p].count(d) > 1:
                penalization += (periodo_disc[p].count(d) - 1) * penalizacoes['T2']['pontuacao']

    print(f"depois de Penalizando materias de um mesmo periodo em um mesmo horario e dia: {penalization-aux}")
    infos['T2'] = penalization - aux
    aux = penalization

    # ==================================================================================
    # Penalizando professores ministrarem mais de 3 materias
    for prof in profs.keys():
        if len(profs[prof].keys()) > 3:
            penalization += len(profs[prof].keys()) * penalizacoes['T3']['pontuacao']

    print(f"depois de Penalizando professores ministrarem mais de 3 materias {penalization - aux}")
    infos['T3'] = penalization - aux
    aux = penalization

    # ===================================================================================
    # Penalizando disciplinas em periodos errados
    for discs in individual.keys():
        if individual[discs]['periodo'] != disciplinas[discs]['periodo']:
            penalization += penalizacoes['T4']['pontuacao']

    print(f"depois de Penalizando disciplinas em periodos errados {penalization - aux}")
    infos['T4'] = penalization - aux
    aux = penalization

    # ===================================================================================
    # Penalizando professores ministrarem materias que nao são de sua preferencia

    for prof in profs.keys():
        for disc in profs[prof].keys():
            if disc not in professores[prof]['preferencias']:
                penalization += penalizacoes['T5']['pontuacao']

    print(f"depois de Penalizando professores ministrarem materias que nao são de sua preferencia {penalization - aux}")
    infos['T5'] = penalization - aux
    aux = penalization

    # ====================================================================================
    infos['final_score'] = penalization
    print(f"Pontuação final: {penalization}")

    return infos


def evaluate(individual):
    penalization = 0
    #print(disciplinas)
    profs = dict()
    for disc in individual.keys():
        if individual[disc]['professor'] not in profs.keys():
            profs[individual[disc]['professor']] = {disc:""}

        profs[individual[disc]['professor']][disc] = individual[disc]["horario"]

    discs = dict()
    for disc in individual.keys():
        if disc not in discs.keys():
            discs[disc] = {"periodo":"","horario":""}

        discs[disc]["horario"] = individual[disc]["horario"]
        discs[disc]["periodo"] = individual[disc]["periodo"]
    aux = 0
    # =================================================================================
    # Penalizando materias diferentes no mesmo horario
    for prof in profs.keys():
        aulas = list(profs[prof].values())
        #print(aulas)
        for aula in aulas:
            if aulas.count(aula) > 1:
                #print(f"Professor: {(aulas.count(aula)-1)*penalizacoes['T1']['pontuacao']}")
                penalization += (aulas.count(aula)-1)*penalizacoes['T1']['pontuacao']

    #print(f"Depois de Penalizando materias diferentes no mesmo horario: {penalization - aux}")
    aux = penalization
    # ==================================================================================
    # Penalizando materias de um mesmo periodo em um mesmo horario e dia
    periodo_disc = {}
    for disc in discs.keys():
        if discs[disc]['periodo'] not in periodo_disc.keys():
            periodo_disc[discs[disc]['periodo']] = []

        periodo_disc[discs[disc]['periodo']].append(discs[disc]['horario'])

    for p in periodo_disc.keys():
        #print(p)
        #print(periodo_disc[p])

        for d in periodo_disc[p]:
            #print(f"{d}: {periodo_disc[p].count(d)}")
            if periodo_disc[p].count(d) > 1:
                penalization += (periodo_disc[p].count(d)-1)*penalizacoes['T2']['pontuacao']

    #print(f"depois de Penalizando materias de um mesmo periodo em um mesmo horario e dia: {penalization-aux}")
    aux = penalization

    # ==================================================================================
    # Penalizando professores ministrarem mais de 3 materias
    for prof in profs.keys():
        if len(profs[prof].keys()) > 3:
            penalization += len(profs[prof].keys()) * penalizacoes['T3']['pontuacao']

    #print(f"depois de Penalizando professores ministrarem mais de 3 materias {penalization - aux}")
    aux = penalization

    # ===================================================================================
    # Penalizando disciplinas em periodos errados
    for discs in individual.keys():
        if individual[discs]['periodo'] != disciplinas[discs]['periodo']:
            penalization += penalizacoes['T4']['pontuacao']

    #print(f"depois de Penalizando disciplinas em periodos errados {penalization - aux}")
    aux = penalization

    # ===================================================================================
    # Penalizando professores ministrarem materias que nao são de sua preferencia


    for prof in profs.keys():
        #print(prof)
        #print(profs[prof].keys())
        #break
        for disc in profs[prof].keys():
            #print(disc)
            #break

            if disc not in professores[prof]['preferencias']:
                penalization += penalizacoes['T5']['pontuacao']

    #print(f"depois de Penalizando professores ministrarem materias que nao são de sua preferencia {penalization - aux}")
    aux = penalization

    # ====================================================================================
    #print(f"Pontuação final: {penalization}")

    return penalization


def crossing(fathers, method='single_point'):
    """ O cruzamento entre os pais/melhores individuos da geração passada para formar
     novos individuos com caracteristicas boas

     metodos de crossover:
        - single_point
        - multi_point
    """
    # É melhor trabbalhar assim
    genes = disciplinas.keys()

    # Escolhe um ponto de crossover aleatório
    crossover_point = random.choice(list(genes))

    if method == 'single_point':
        # Realiza o crossover
        child1 = {gene: fathers[0][gene] if gene < crossover_point else fathers[2][gene] for gene in genes}
        child2 = {gene: fathers[1][gene] if gene < crossover_point else fathers[1][gene] for gene in genes}

        return [child1, child2]

    if method == 'multipoint':
        # Escolhe vários pontos de crossover aleatórios
        crossover_points = sorted(random.sample(genes, k=random.randint(1, len(genes) - 1)))

        # Realiza o crossover
        child1 = {}
        child2 = {}
        for i in range(len(crossover_points)):
            if i % 2 == 0:
                child1.update(
                    {gene: fathers[0][gene] if gene < crossover_points[i] else fathers[1][gene] for gene in genes})
                child2.update(
                    {gene: fathers[1][gene] if gene < crossover_points[i] else fathers[0][gene] for gene in genes})
            else:
                child1.update(
                    {gene: fathers[1][gene] if gene < crossover_points[i] else fathers[0][gene] for gene in genes})
                child2.update(
                    {gene: fathers[0][gene] if gene < crossover_points[i] else fathers[1][gene] for gene in genes})

        return [child1, child2]


def mutate(individuals, mutation_rate):

    profs = list(professores.keys())
    hrs = list(horarios.keys())

    for individual in individuals:
        for discs in individual.keys():
            if random.random() < mutation_rate:

                individual[discs]['professor'] = random.choice(profs)
                individual[discs]['horario'] = [random.choice(hrs), random.choice(dias_semana)]

    return individuals


def select(population, k, method='tournament', threshold=0.3):
    """Esta seleção aplica o conceito de pesos para cada individuo, fornece a quantidade de individuos e
    seleciona k individuos, metodos de seleção:

    - tournament: torneio e seleciona os k melhores
    - truncation: pega os 30% melhores e sorteia k individuos
    - kbest: seleciona os k melhores individuos
    """

    if method == 'tournament':
        # Seleciona k indivíduos aleatórios da população
        tournament_participants = random.sample(population, k)

        # Ordena os participantes do torneio com base na função de avaliação
        tournament_participants.sort(key=lambda ind: evaluate(ind), reverse=True)

        # Retorna o rank 3 do torneio
        return tournament_participants[0:k+1]

    elif method == 'truncation':
        # Ordena a população com base na função de avaliação
        population.sort(key=lambda ind: evaluate(ind), reverse=True)

        # Calcula o número de indivíduos a serem mantidos
        num_selected = int(len(population) * threshold)

        # Seleciona os melhores indivíduos
        selected_individuals = population[:num_selected]

        # Escolhe aleatoriamente entre os melhores (para adicionar diversidade)
        selected_individual = random.choices(selected_individuals,k=k)

        return selected_individual

    elif method == 'kbest':
        # Retorna os k melhores avaliados
        return random.choices(population, k=k, weights=[100/100+evaluate(individual) for individual in population])

