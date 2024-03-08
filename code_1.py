    #Importando bibliotecas
    import pyautogui
    import time
    import pandas
    import numpy
    import openpyxl

    #Declarando pausa
    pyautogui.PAUSE = 1

    #Abrindo Chrome
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")

    #Abrindo site
    link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
    pyautogui.write(link)
    pyautogui.press("enter")

    #Declarando pausa maior
    time.sleep(3)

    #Fazendo Login
    pyautogui.click(x=621, y=411)
    pyautogui.write("gle.missael@gmail.com")
    pyautogui.press("tab")
    pyautogui.write("123456")
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(3)

    #Importando base de dados
    tabela = pandas.read_csv("produtos.csv")

    #Loop
    for linha in tabela.index:

        #Cadastrando um produto
        #Clicando na primeira linha
        pyautogui.click(x=388, y=294)

        #Codigo
        pyautogui.write(tabela.loc[linha, "codigo"])
        pyautogui.press("tab")

        #Marca
        pyautogui.write(tabela.loc[linha, "marca"])
        pyautogui.press("tab")

        #Tipo
        pyautogui.write(tabela.loc[linha, "tipo"])
        pyautogui.press("tab")

        #Categoria
        pyautogui.write(str(tabela.loc[linha, "categoria"]))
        pyautogui.press("tab")

        #Preço
        pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
        pyautogui.press("tab")

        #Custo
        pyautogui.write(str(tabela.loc[linha, "custo"]))
        pyautogui.press("tab")

        #Obs
        obs = tabela.loc[linha, "obs"]
        if not pandas.isna(obs):
            pyautogui.write(obs)
        pyautogui.press("tab")
        pyautogui.press("enter")

        #Scroll
        pyautogui.scroll(5000)