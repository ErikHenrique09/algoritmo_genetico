# Isso aqui ja garante que :
# nao terão duas disciplinas repetidas
# não terão dois professores dando a mesma materia


disciplinas = {
    "CC21C":  {"periodo": 1,"prereq": [""],               "professor": "", "horario": ["", ""], "disc_desc": "Fundamentos De Programação"},
    "CC21D":  {"periodo": 1,"prereq": [""],               "professor": "", "horario": ["", ""], "disc_desc": "Introdução A Ciência Da Computação"},
    "F1221E": {"periodo": 1,"prereq": [""],               "professor": "", "horario": ["", ""], "disc_desc": "Fundamentos De Eletricidade"},
    "MA221A": {"periodo": 1,"prereq": [""],               "professor": "", "horario": ["", ""], "disc_desc": "Cálculo Diferencial E Integral 1"},
    "MA221B": {"periodo": 1,"prereq": [""],               "professor": "", "horario": ["", ""], "disc_desc": "Geometria Analítica E Álgebra Linear"},
    "MA221F": {"periodo": 1,"prereq": [""],               "professor": "", "horario": ["", ""], "disc_desc": "Lógica Matemática"},
    "CC22B":  {"periodo": 2,"prereq": ["MA221F"],         "professor": "", "horario": ["", ""], "disc_desc": "Circuitos Digitais"},
    "CC22C":  {"periodo": 2,"prereq": ["CC21C"],          "professor": "", "horario": ["", ""], "disc_desc": "Linguagem De Programação Estruturada"},
    "CC22D":  {"periodo": 2,"prereq": [""],               "professor": "", "horario": ["", ""], "disc_desc": "Fundamentos De Banco De Dados"},
    "ED222E": {"periodo": 2,"prereq": [""],               "professor": "", "horario": ["", ""], "disc_desc": "Comunicação Linguistica"},
    "MA222A": {"periodo": 2,"prereq": ["MA221A"],         "professor": "", "horario": ["", ""], "disc_desc": "Cálculo Diferencial E Integral 2"},
    "MA222F": {"periodo": 2,"prereq": [""],               "professor": "", "horario": ["", ""], "disc_desc": "Probabilidade E Estatística"},
    "CC23B":  {"periodo": 3,"prereq": ["CC22D"],          "professor": "", "horario": ["", ""], "disc_desc": "Sistemas Gerenciadores De Banco De Dados"},
    "CC23C":  {"periodo": 3,"prereq": ["CC22C"],          "professor": "", "horario": ["", ""], "disc_desc": "Estrutura De Dados"},
    "CC23D":  {"periodo": 3,"prereq": [""],               "professor": "", "horario": ["", ""], "disc_desc": "Arquitetura E Organização De Computadores"},
    "CC23E":  {"periodo": 3,"prereq": ["CC21C"],          "professor": "", "horario": ["", ""], "disc_desc": "Programação Orientada A Objetos"},
    "CC23F":  {"periodo": 3,"prereq": [""],               "professor": "", "horario": ["", ""], "disc_desc": "Linguagem De Estruturação E Apresentação De"},
    "MA223A": {"periodo": 3,"prereq": [""],               "professor": "", "horario": ["", ""], "disc_desc": "Cálculo Numérico"},
    "CC24A":  {"periodo": 4,"prereq": ["CC23B", "CC23E"], "professor": "", "horario": ["", ""], "disc_desc": "Linguagem De Programação Objeto Orientada"},
    "CC24C":  {"periodo": 4,"prereq": ["CC23C"],          "professor": "", "horario": ["", ""], "disc_desc": "Pesquisa E Ordenação De Dados"},
    "CC24D":  {"periodo": 4,"prereq": [""],               "professor": "", "horario": ["", ""], "disc_desc": "Engenharia De Requisitos"},
    "CC24E":  {"periodo": 4,"prereq": ["CC22C", "CC23D"], "professor": "", "horario": ["", ""], "disc_desc": "Linguagem De Montagem"},
    "CC24F":  {"periodo": 4,"prereq": [""],               "professor": "", "horario": ["", ""], "disc_desc": "Comunicação De Dados"},
    "CC24G":  {"periodo": 4,"prereq": ["MA221B"],         "professor": "", "horario": ["", ""], "disc_desc": "Computação Gráfica"},
    "ED224B": {"periodo": 4,"prereq": [""],               "professor": "", "horario": ["", ""], "disc_desc": "Metodologia Da Pesquisa"}
}

dias_semana = [
    "SEGUNDA",
    "TERÇA",
    "QUARTA",
    "QUINTA",
    "SEXTA"
]

horarios = {
    "M1": ["07:30", "08:20"],
    "M2": ["08:20", "09:10"],
    "M3": ["09:10", "10:00"],
    "M4": ["10:20", "11:10"],
    "M5": ["11:10", "12:00"],
    "T1": ["13:00", "13:50"],
    "T2": ["13:50", "14:40"],
    "T3": ["14:40", "15:30"],
    "T4": ["15:50", "16:40"],
    "T5": ["16:40", "17:30"],
}

professores = {
    "AGNALDO":{"nome":"Agnaldo Da Costa","preferencias":[]},
    #"ANDERSON":{"nome":"Anderson Brilhador","preferencias":[]},
    "ARLETE":{"nome":"Arlete Teresinha Beuren","preferencias":[]},
    "CLAUDIO":{"nome":"Claudio Jose Biazus","preferencias":["CC24E","CC24D", "CC21D"]},
    "DAVI":{"nome":"Davi Marcondes Rocha","preferencias":["MA221F","CC24G"]},
    "DIEGO":{"nome":"Diego Venancio Thomaz","preferencias":["MA221A","MA222F"]},
    #"ELENILTON":{"nome":"Elenilton Jairo Dezengrini","preferencias":[]},
    "EUCLIDES":{"nome":"Euclides Peres Farias Junior","preferencias":[]},
    "EVANDRO NAKAJIM":{"nome":"Evandro Alves Nakajima","preferencias":["MA222A","MA223A"]},
    "EVANDRO SILVA":{"nome":"Evandro Da Silva Dos Santos","preferencias":["CC24D","MA221B"]},
    #"FERNANDO S":{"nome":"Fernando Schutz","preferencias":[]},
    #"FRANCK":{"nome":"Franck Carlos Velez Benito","preferencias":["CC23C"]},
    "GIANI":{"nome":"Giani Carla Ito","preferencias":["CC21C","CC22D","CC22C"]},
    "GIUVANE":{"nome":"Giuvane Conti","preferencias":["CC23E","CC24A"]},
    "GLORIA":{"nome":"Gloria Patricia Lopez Sepulveda","preferencias":["CC23D","CC24C"]},
    "HAMILTON":{"nome":"Hamilton Pereira Da Silva","preferencias":[]},
    "HOFFMANN":{"nome":"Alessandra Bortoletto Garbelotti Hoffmann","preferencias":[]},
    "LEILIANE":{"nome":"Leiliane Pereira De Rezende","preferencias":["CC22C","CC22D","CC23B","CC22C","CC22B"]},
    #"LUANA":{"nome":"Luana Menezes Monguilod","preferencias":["CC24G"]},
    #"MOLINA":{"nome":"Roberto Molina De Souza","preferencias":[]},
    "RAFAEL TESSER":{"nome":"Rafael Keller Tesser","preferencias":[]},
    "THIAGO":{"nome":"Thiago Franca Naves","preferencias":["CC23C"]},
    #"VANDERLEA":{"nome":"Vanderlea De Lima Inaba","preferencias":[]},
    "VERA":{"nome":"Vera Lucia Vasilevski Dos Santos Araujo","preferencias":["ED222E","ED224B"]}#,
    #"WESLEY":{"nome":"Wesley Bertoli Da Silva","preferencias":[]}
}


type1 = 1000 # Coisas que é impossivel de acontecer
type2 = 500  # Coisas que não é preferivel mas é possivel ocorrer
type3 = 100  # Detalhes pontuais

penalizacoes = {
    "T1":{"descricao":"Professores com duas disciplinas diferentes em um mesmo dia e horário","pontuacao": type1},
    "T2":{"descricao":"Aulas de disciplinas diferentes do mesmo periodo no mesmo horario","pontuacao": type1},
    "T3":{"descricao":"Professores ministrarem mais de 3 disciplinas","pontuacao": type2},
    "T4":{"descricao":"Disciplinas estarem no periodo errado","pontuacao": type1},
    "T5":{"descricao":"Professores ministrar materias que não são de sua preferencia","pontuacao": type3}#,
    #"T6":{"descricao":"","pontuacao": 100}
}


