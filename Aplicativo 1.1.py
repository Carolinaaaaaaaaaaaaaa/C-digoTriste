# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 23:19:22 2023

@author: Carol
"""

import cv2
import tkinter as tk
from tkinter import filedialog


def calcular_distancia(ponto1, ponto2, escala):
    distancia_pixels = ((ponto1[0] - ponto2[0])**2 + (ponto1[1] - ponto2[1])**2)**0.5
    distancia_real = distancia_pixels * escala
    return distancia_real

def carregar_imagem():
    file_path = filedialog.askopenfilename()
    imagem = cv2.imread(file_path)
    return imagem

def selecionar_pontos(imagem):
    # Implemente a lógica para permitir ao usuário selecionar dois pontos na imagem.
    # Você pode usar eventos de clique do mouse ou toque na tela, dependendo da plataforma.

def inserir_escala():
    # Implemente a lógica para permitir ao usuário inserir a escala.

def exibir_resultado(distancia):
    # Implemente a lógica para mostrar a distância calculada ao usuário.

def main():
    janela = tk.Tk()
    janela.title("Calculadora de Distância")
    
    imagem = carregar_imagem()
    pontos = selecionar_pontos(imagem)
    escala = inserir_escala()
    distancia = calcular_distancia(pontos[0], pontos[1], escala)
    
    exibir_resultado(distancia)
    
    janela.mainloop()

if __name__ == "__main__":
    main()