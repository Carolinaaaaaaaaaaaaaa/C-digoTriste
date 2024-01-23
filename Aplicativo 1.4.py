# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 21:14:44 2023

CÓDIGO QUE DÁ CERTO
"""


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
import math

class PointSelectionApp(App):
    def build(self):
        self.image_path = "levedura.jpg"  # Substitua pelo caminho da sua imagem
        self.points = []

        layout = BoxLayout(orientation='vertical')

        self.image = Image(source=self.image_path, allow_stretch=True)
        self.image.bind(on_touch_down=self.iniciar_selecao)
        layout.add_widget(self.image)

        self.label = Label(text="")
        layout.add_widget(self.label)

        button = Button(text="Selecionar Pontos")
        layout.add_widget(button)

        return layout

    def iniciar_selecao(self, instance, touch):
        if self.image.collide_point(*touch.pos):
            self.points.append((touch.x, touch.y))

            if len(self.points) == 2:
                distancia = self.calcular_distancia(self.points[0], self.points[1])
                self.label.text = f'Distância: {distancia:.2f} pixels'
                self.points = []

    def calcular_distancia(self, ponto1, ponto2):
        distancia_pixels = math.sqrt((ponto2[0] - ponto1[0])**2 + (ponto2[1] - ponto1[1])**2)
        print(distancia_pixels)
        return distancia_pixels



"""
    def distanciaReal(self, distancia_pixels):
        distancia1 = distancia_pixels

"""



PointSelectionApp().run()









