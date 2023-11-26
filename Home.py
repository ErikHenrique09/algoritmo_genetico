import streamlit as st
from uteis.funcs import *
from main import gera_grade


def gerar_visu_grade(df_period):
    dias_semana = ["SEGUNDA", "TERÇA", "QUARTA", "QUINTA", "SEXTA"]
    times = ["M1", "M2", "M3", "M4", "M5", "T1", "T2", "T3", "T4", "T5"]
    inicio = [horarios[time][0] for time in times]
    fim = [horarios[time][1] for time in times]

    df = pd.DataFrame(index=times, columns=['inicio', 'fim'] + dias_semana)
    df['inicio'] = inicio
    df['fim'] = fim

    # preenchendo
    for index, row in df_period.iterrows():
        df[row['dia']].loc[row['horario']] = row['disciplina']

    df.fillna('', inplace=True)

    return df


def process(GENERATIONS, POPULATION_SIZE, MUTATION_RATE, SELECT_METHOD, CROSS_METHOD):
    best, best_gen, plot, infos = gera_grade(POPULATION_SIZE, MUTATION_RATE, GENERATIONS, SELECT_METHOD, CROSS_METHOD)

    col2.write("Em relação aos erros do melhor individuo")
    for error in infos.keys():
        if 'T' in error:
            col2.write(f"- {penalizacoes[error]['descricao']}: {infos[error]}")

    col2.write(f"Erro Total: {infos['final_score']}")

    col2.write(f"Continue rolando o site para obter mais informações.")

    df = pd.DataFrame.from_dict(best, orient='index').reset_index(drop=False).rename(columns={'index':'disciplina'})

    plots = pd.DataFrame(plot)

    df['tempo'] = df['horario'].apply(lambda x: f"{horarios[x[0]][0]} - {horarios[x[0]][1]}")
    df['dia'] = df["horario"].apply(lambda y: y[1])
    df['horario'] = df['horario'].apply(lambda x: x[0])
    df.rename(columns={'Unnamed: 0': 'disciplina'}, inplace=True)

    # Gerando os dados
    df[['disciplina', 'periodo', 'disc_desc']].sort_values(['periodo', 'disciplina']).to_csv('./data/disciplinas.csv')
    pd.DataFrame(df['professor'].sort_values().unique(), columns=['PROFESSORES']).to_csv('./data/professores.csv')

    periodos = []
    profs_disc = []
    for i in range(1, 5):
        d = df.query('periodo == @i')
        periodos.append(gerar_visu_grade(d))

        d = d[['professor', 'disciplina','disc_desc']].sort_values('disciplina')
        profs_disc.append(d)

    return periodos, profs_disc, plots


st.set_page_config(layout='wide')

col1, col2 = st.columns([0.5,0.5],gap='small')
col1.title("Projeto 2 - Algoritmos Geneticos")
col2.title("Analise do melhor individuo")

formatacao_justify = """<p style="text-align: justify;">{}</p>"""

txt1 = """
    O trabalho consiste em implementar um algoritmo genético para montar a grade horários
do curso de Ciência da Computação do campus Santa Helena do 1º ao 4º período. O algoritmo 
gera uma distribuição de disciplinas onde não existam os seguintes conflitos: 

- Um professor ministrar diferentes disciplinas no mesmo dia e horário.
- Disciplinas de um mesmo periodo sendo ministradas em um mesmo dia e horario.

Tambem foi realizada uma tentativa de implementar um conceito de preferencia nas materias
em que cada professor ira ministrar, mas isso é mais uma opção do que uma regra ou lei.

"""

col1, col2 = st.columns([0.5,0.5], gap='medium')

# =======================================================================================================================

col1.write(formatacao_justify.format(txt1), unsafe_allow_html=True)
col3, col4, col5 = col1.columns([0.3,0.3,0.3],gap='small')
col6, col7, col8 = col1.columns([0.3,0.3,0.3],gap='small')

GENERATIONS = col3.selectbox('Gerações: ',[100, 300, 500, 1000, 1500])
POPULATION_SIZE = col4.selectbox('Individuos por Geração: ',[10, 30, 50, 100, 150, 500, 1000])
MUTATION_RATE = col5.selectbox('Taxa de Mutação: ',[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
CROSS_METHOD = col6.selectbox('Metodo de Crossover', ['single_point','multipoint'])
SELECT_METHOD = col8.selectbox('Metodo de Seleção', ['tournament','kbest','truncation'])

if col1.button("Executar",use_container_width=True):
    periodos, profs_dics, plots = process(GENERATIONS, POPULATION_SIZE, MUTATION_RATE, SELECT_METHOD, CROSS_METHOD)

    st.header("Score do Algoritmo Genetico com o passar das gerações")
    plt.figure(figsize=(25,5))
    plt.plot(plots['generation'],plots['score'], color='k')
    plt.ylabel('Score')
    plt.xlabel('Generations')
    plt.title("Grafico do score do algoritmo com o passar das gerações")

    st.pyplot(plt)

    for i in range(1,5):
        col3, col4 = st.columns([0.5,0.5])

        col3.header(f"Grade do periodo {i}")
        col3.table(periodos[i-1])
        col4.header(f"Professores do periodo {i}")
        col4.table(profs_dics[i-1])
else:
    txt = """Ao executar o algoritmo esta area sera preenchida com as informações de erro do mesmo, e logo abaixo 
    teremos os periodos com os professores que ficarão com cada disciplina e seus respectivos horarios.
    
Algumas dicas:
- Taxas de mutação alta podem danificar nossos individuos
- Caso escolha uma quantidade alta de gerações o algoritmo pode demorar
- Caso escolha uma quantidade alta de individuos o algoritmo pode demora
    
OBS: Provavelmente o unico erro sera de professores nao ministrar a materia de preferencia mas não julguei esse ponto como
algo critico e sim apenas uma preferencia do professor.
    """

    col2.write(formatacao_justify.format(txt), unsafe_allow_html=True)



# =======================================================================================================================
col1, col2 = st.columns([0.5,0.5])

with col1:
    st.header('Disciplinas consideradas')
    disciplinas = pd.read_csv('./data/disciplinas.csv').drop("Unnamed: 0", axis=1)
    st.table(disciplinas)

with col2:
    st.header('Professores')
    disciplinas = pd.read_csv('./data/professores.csv').drop("Unnamed: 0", axis=1)
    st.table(disciplinas)














