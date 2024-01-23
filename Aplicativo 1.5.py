# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 22:19:50 2023

@author: Carol
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Line
import math

class PointSelectionApp(App):
    def build(self):
        self.image_path = "levedura.jpg"  # Substitua pelo caminho da sua imagem
        self.points = []
        self.current_color_index = 0
        self.colors = [(1, 0, 0, 1), (0, 0, 1, 1)]  # Vermelho e Azul, você pode adicionar mais cores se desejar

        layout = BoxLayout(orientation='vertical')

        self.image = Image(source=self.image_path, allow_stretch=True)
        self.image.bind(on_touch_down=lambda instance, touch: self.iniciar_selecao(touch))
        layout.add_widget(self.image)

        self.label = Label(text="")
        layout.add_widget(self.label)

        button_select = Button(text="Selecionar Pontos")
        button_select.bind(on_press=self.iniciar_selecao)
        layout.add_widget(button_select)

        button_clear = Button(text="Limpar")
        button_clear.bind(on_press=self.limpar_selecao)
        layout.add_widget(button_clear)

        return layout

    def iniciar_selecao(self, touch):
        if self.image.collide_point(*touch.pos):
            self.points.append((touch.x, touch.y))

            if len(self.points) == 2:
                distancia = self.calcular_distancia(self.points[0], self.points[1])
                self.label.text = f'Distância: {distancia:.2f} pixels'
                self.points = []

                # Adicione as cores e a linha após calcular a distância
                with self.image.canvas:
                    Color(*self.colors[self.current_color_index])
                    Line(points=self.points)
                    self.current_color_index = (self.current_color_index + 1) % len(self.colors)

    def limpar_selecao(self, instance):
        self.points = []
        self.label.text = ""
        self.image.canvas.before.clear()

    def calcular_distancia(self, ponto1, ponto2):
        distancia_pixels = math.sqrt((ponto2[0] - ponto1[0])**2 + (ponto2[1] - ponto1[1])**2)
        return distancia_pixels

if __name__ == "__main__":
    PointSelectionApp().run()
