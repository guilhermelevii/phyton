from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import time
import pyautogui
import pandas as pd
import requests
import time
import os
import re
import locale

# Definir a localização para português
locale.setlocale(locale.LC_TIME,'pt_BR.UTF-8')

def validate(codConta, idCaminho):
    mes_atual = data_atual.strftime("%b %Y").upper() # Defina o mês atual aqui
    diretorio_base = r'C:\Users\guilh\OneDrive\Área de Trabalho\python\phyton\diretorio base'
    caminho_pasta = os.path.join(diretorio_base, str(idCaminho))

    if not os.path.exists(caminho_pasta):
        return False  # Pasta não existe, retorna False

    # Lista de arquivos na pasta
    arquivos_pasta = os.listdir(caminho_pasta)

    # Padrão para o nome do arquivo (99.941-5 AGO 2023)
    padrao_arquivo = fr'^{codConta} {mes_atual} - EXTRATO (CC|RENDIMENTO)\.pdf'

    # Verifica se pelo menos um arquivo corresponde ao padrão
    arquivo_encontrado = any(re.match(padrao_arquivo, arquivo) for arquivo in arquivos_pasta)

    return arquivo_encontrado