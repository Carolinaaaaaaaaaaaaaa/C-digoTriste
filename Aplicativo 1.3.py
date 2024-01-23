# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 18:05:00 2023

@author: Carol
"""
'''
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

        self.label = Label(text="Selecione dois pontos na imagem.")
        layout.add_widget(self.label)

        self.distancia_label = Label(text="")
        layout.add_widget(self.distancia_label)

        button = Button(text="Limpar")
        button.bind(on_press=self.limpar)
        layout.add_widget(button)

        return layout

    def iniciar_selecao(self, instance, touch):
        if self.image.collide_point(*touch.pos):
            self.points.append((touch.x, touch.y))

            if len(self.points) == 2:
                distancia = self.calcular_distancia(self.points[0], self.points[1])
                self.distancia_label.text = f'Distância: {distancia:.2f} pixels'
                self.label.text = f'Pontos selecionados: {self.points[0]}, {self.points[1]}'

    def calcular_distancia(self, ponto1, ponto2):
        distancia_pixels = math.sqrt((ponto2[0] - ponto1[0])**2 + (ponto2[1] - ponto1[1])**2)
        return distancia_pixels

    def limpar(self, instance):
        self.points = []
        self.label.text = "Selecione dois pontos na imagem."
        self.distancia_label.text = ""

if __name__ == "__main__":
    PointSelectionApp().run()

'''

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
        self.primeira_distancia = None

        layout = BoxLayout(orientation='vertical')

        self.image = Image(source=self.image_path, allow_stretch=True)
        self.image.bind(on_touch_down=self.iniciar_selecao)
        layout.add_widget(self.image)

        self.label = Label(text="Selecione dois pontos na imagem.")
        layout.add_widget(self.label)

        self.distancia_label = Label(text="")
        layout.add_widget(self.distancia_label)

        button = Button(text="Limpar")
        button.bind(on_press=self.limpar)
        layout.add_widget(button)

        return layout

    def iniciar_selecao(self, instance, touch):
        if self.image.collide_point(*touch.pos):
            self.points.append((touch.x, touch.y))

            if len(self.points) == 2:
                distancia = self.calcular_distancia(self.points[0], self.points[1])
                if self.primeira_distancia is None:
                    self.primeira_distancia = distancia
                self.distancia_label.text = f'Distância: {distancia:.2f} pixels'
                self.label.text = f'Pontos selecionados: {self.points[0]}, {self.points[1]}'

    def calcular_distancia(self, ponto1, ponto2):
        distancia_pixels = math.sqrt((ponto2[0] - ponto1[0])**2 + (ponto2[1] - ponto1[1])**2)
        return distancia_pixels

    def limpar(self, instance):
        self.points = []
        self.label.text = "Selecione dois pontos na imagem."
        self.distancia_label.text = ""

if __name__ == "__main__":
    PointSelectionApp().run()










