# pip install pyautogui

import pyautogui
import time 

pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar
# pyautogui.press -> pressionar uma tecla
# pyautogui.write -> escrever


# Passo 1: Abrir o sistema da empresa
#    Sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pressionar a tecla windows
pyautogui.press("win")

# escrever edge
pyautogui.write("edge")

# pressionar a tecla enter
pyautogui.press("enter")

# entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

# pressionar enter
pyautogui.press("enter")

# Pedir para o computador esperar 2 segundos 
time.sleep(2)


# Passo 2: Fazer o login

# clicar no campo de e-mail
pyautogui.click(x=487, y=365)

#escrever um e-mail
pyautogui.write("tahixoj815@pariag.com")

#passar para o próximo form
pyautogui.press("tab")

#escrever uma senha
pyautogui.write("lablalablalbal")

#clicar no botão "logar"
pyautogui.click(x=631, y=522)


# Passo 3: Importar a base de dados dos produtos
# pip install pandas openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)


time.sleep(2)


# Passo 4: Cadastrar 1 produto

for linha in tabela.index: 
    pyautogui.click(x=483, y=245) # clica no 1º campo

    #escrever o código
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #escrever a marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #escrever o tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #escrever a categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #escrever o preço unitário
    preço_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preço_unitario))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs e ir pro botão enviar
    obs = str(tabela.loc[linha, "obs"]) 
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    

    #apertar o botão "enviar"
    pyautogui.press("enter")

    # espera um pouco pra página carregar
    time.sleep(1)

    #número positivo = scroll pra cima
    #número negativo = scroll pra baixo
    pyautogui.scroll(10000)

    
# Passo 5: Repetir o passo 4 até acabar todos os produtos

# nan = valor vazio em uma base de dados
# = not a number