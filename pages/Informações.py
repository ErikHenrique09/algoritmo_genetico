import streamlit as st

st.title('Informações sobre os metodos utilizados')

col1, col2 = st.columns([0.5,0.5],gap='small')

formatacao_justify = """<p style="text-align: justify;">{}</p>"""

with col1:

    st.header('Metodos de seleção')
    txt1 = """
        O metodo de seleção se refere a como os melhores individuos da geração serão selecionados para formar a nova geração.
        
Neste trabalho foram utilizados 3 metodos de seleção:
- Seleção por torneio   
- Seleção por truncamento
- Seleção por kbest         
    
    """
    st.write(formatacao_justify.format(txt1), unsafe_allow_html=True)

    st.header('Seleção por torneio')
    txt2 = """
O metodo de seleção por torneio sorteia pares de individuos da população e realiza uma 'luta' entre eles, baseada no score, por fim 
retorna os individuos selecionados para montar a proxima geração 
"""
    st.write(formatacao_justify.format(txt2), unsafe_allow_html=True)

    st.header('Seleção por truncamento')
    txt2 = """
   A seleção por truncamento ordena a população com base no score e seleciona em porcentagem os individuos, por fim retorna 
   os novos individuos que irão cruzar e formar a nova geração
    """
    st.write(formatacao_justify.format(txt2), unsafe_allow_html=True)

    st.header('Seleção por KBest')
    txt2 = """
       Simplesmente seleciona os k melhores individuos da população com base na função de avaliação
        """
    st.write(formatacao_justify.format(txt2), unsafe_allow_html=True)

with (col2):
    st.header('Metodos de cruzamento')
    txt1 = """
O metodo de crossover indica como sera feito o cruzamento de dois individuos para gerarem um novos individuos que irão constituir
a nova geração

Neste trabalho foram utilizados 2 metodos de crossover:
- Crossover uniponto   
- Crossover Multiponto
"""
    st.write(formatacao_justify.format(txt1), unsafe_allow_html=True)
    # PULINHO DE LINHA MAROTO
    st.write('')
    st.write('')
    st.write('')

    st.header('Crossover uniponto')
    txt2 = """
    Seleciona um ponto aleatorio de referencia para o corte, divide os dois individuos em 2 e cruza as metades para gerar um novo 
    """
    st.write(formatacao_justify.format(txt2), unsafe_allow_html=True)

    st.write('')
    st.write('')

    st.header('Crossover Multiponto')
    txt2 = """
       Seleciona 2 ou mais pontos aleatorios de referencia para o corte, divide os individuos e ao mesclar aplica alguma organização 
       que faça sentido para gerar o novo individuo
        """
    st.write(formatacao_justify.format(txt2), unsafe_allow_html=True)
