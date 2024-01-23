# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 21:22:52 2023

Aplicativo

@author: Carol
"""

import cv2
import numpy as np

def calcular_distancia(ponto1, ponto2):
    return np.linalg.norm(ponto1 - ponto2)

def main():
    # Carregar a imagem
    imagem = cv2.imread('levedura.jpg')

    # Definir dois pontos na imagem (por exemplo, marcas ou pontos de referência)
    ponto1 = np.array([100, 200])  # Coordenadas do primeiro ponto
    ponto2 = np.array([300, 400])  # Coordenadas do segundo ponto

    # Desenhar os pontos na imagem
    cv2.circle(imagem, tuple(ponto1), 5, (0, 0, 255), -1)  # Ponto 1 em vermelho
    cv2.circle(imagem, tuple(ponto2), 5, (0, 0, 255), -1)  # Ponto 2 em vermelho

    # Calcular a distância entre os pontos
    distancia = calcular_distancia(ponto1, ponto2)

    # Exibir a distância na imagem
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(imagem, f'Distancia: {distancia:.2f} pixels', (50, 50), fonte, 1, (0, 0, 255), 2)

    # Exibir a imagem com as marcações
    cv2.imshow('Medição de Distância', imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
