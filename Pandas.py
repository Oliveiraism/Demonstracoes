import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# matplotlib inline
# reload_ext autoreload
# autoreload 2

contacorr = [['012020', 5000, 2500],
             ['022020', 5000, 2500],
             ['032020', 5000, 2500],
             ['042020', 5000, 2500],
             ['052020', 5000, 2500],
             ['062020', 5000, 2500]]

dfcontacorr = pd.DataFrame(contacorr,
                           columns=['Periodo', 'Salario', 'Gastos fixos'])

print(dfcontacorr)

cartao = [['012020', 'master', 500],
          ['012020', 'visa', 1000],
          ['022020', 'master', 600],
          ['022020', 'visa', 100],
          ['032020', 'master', 650],
          ['032020', 'visa', 0],
          ['042020', 'master', 250],
          ['042020', 'visa', 700],
          ['052020', 'master', 50],
          ['052020', 'visa', 1000],
          ['062020', 'master', 123],
          ['062020', 'visa', 2000]]

dfcartao = pd.DataFrame(cartao,
                        columns=['Fatura', 'Bandeira', 'Total'])

print(dfcartao)

dfcartao2 = dfcartao.groupby('Fatura').agg({'Total': sum})

orcamento = pd.merge(dfcontacorr, dfcartao2, how='left',
                     left_on='Periodo', right_on='Fatura')

orcamento.rename(columns={'Total': 'Cartoes'}, inplace=True)

orcamento['Investimentos'] = orcamento['Salario'] - orcamento['Cartoes'] - orcamento['Gastos fixos']

print(orcamento)

sns.lineplot(data=orcamento, x='Periodo', y='Investimentos')
plt.show()
