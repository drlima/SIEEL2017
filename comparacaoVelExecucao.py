# -*- coding: utf-8 -*-
# Importação das bibliotecas necessárias
import pandas as pd
import numpy as np
import time

start = time.time()

vendas = pd.read_csv('dados/dados.csv ', sep=';', decimal =',')

imposto = pd.read_csv('dados/imposto.csv')

vendas['imposto_venda'] = 0
vendas['receita_liquida'] = 0

for categoria in imposto.columns:
    vendas.loc[vendas['product_department']==categoria,
               'imposto_venda'] = imposto.loc[0, categoria]

vendas.loc[:, 'receita_liquida'] = vendas['receita_bruta']*(1 - vendas['imposto_venda'])

stop = time.time()

t1 = stop - start
# %%
start = time.time()

vendas = pd.read_csv('dados/dados.csv ', sep=';', decimal =',')

imposto = pd.read_csv('dados/imposto.csv')

imposto_venda = np.zeros([vendas.shape[0], 1])
receita_liquida = np.zeros([vendas.shape[0], 1])
for n in range (vendas.shape[0]):
    dept = vendas.product_department.iloc[n]
    imposto_venda[n] = imposto[dept][0]
    receita_liquida[n] = vendas.receita_bruta.iloc[n]*(1 - imposto_venda [n])

stop = time.time()

t2 = stop - start
