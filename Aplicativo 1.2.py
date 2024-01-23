# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 23:19:22 2023

@author: Carol
"""

import cv2
import tkinter as tk
from tkinter import filedialog


def calcular_distancia(ponto1,ponto2):
    distancia_pixels = ((ponto1[0] - ponto2[0])**2 + (ponto1[1] - ponto2[1])**2)**0.5
    return distancia_pixels

def carregar_imagem():
    file_path = filedialog.askopenfilename()
    imagem = cv2.imread(file_path)
    return imagem

def selecionar_pontos(imagem):
    # Implemente a lógica para permitir ao usuário selecionar dois pontos na imagem.
    # Você pode usar eventos de clique do mouse ou toque na tela, dependendo da plataforma.
    return imagem

# distancia_pixels é a distancia da colonia que vou medir com o app
def exibir_resultado(distancia_pixels,distancia_pixels_objeto_conhecido,distancia_conhecida):
    distancia_desconhecida = (distancia_pixels*distancia_conhecida)/distancia_pixels_objeto_conhecido
    return distancia_desconhecida

def main():
    janela = tk.Tk()
    janela.title("Calculadora de Distância")
    
    (ponto11, ponto22) = selecionar_pontos(imagem)
    (ponto33, ponto44) = selecionar_pontos(imagem)
    n = float(input("Digite um número para a distância do objeto conhecido: "))
    
    dpoc = calcular_distancia(ponto11,ponto22):
    dp = calcular_distancia(ponto33,ponto44):
    
    imagem = carregar_imagem()
    pontos = selecionar_pontos(imagem)
    distancia = calcular_distancia(pontos[0], pontos[1])
    
    exibir_resultado(dp,dpoc,n)
    
    janela.mainloop()

if __name__ == "__main__":
    main()
    
    
  ##################################################################  
    
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line

class PointSelectionApp(App):
    def build(self):
        self.points = []

        self.widget = Widget()
        self.widget.bind(on_touch_down=self.on_touch_down)

        return self.widget

    def on_touch_down(self, touch):
        if len(self.points) < 2:
            with self.widget.canvas:
                self.points.append((touch.x, touch.y))
                Line(points=self.points)

            if len(self.points) == 2:
                # Chame a função que calcula a distância ou faça o que desejar com os pontos.
                self.calcular_distancia(self.points[0], self.points[1])

    def calcular_distancia(self, ponto1, ponto2):
        # Implemente o cálculo da distância aqui.
        pass

if __name__ == "__main__":
    PointSelectionApp().run()

