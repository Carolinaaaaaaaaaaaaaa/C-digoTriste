# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 21:43:20 2023

@author: Carol

"""

#CODIGO COM PONTO VERMELHO
'''
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse
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
                self.desenhar_pontos()
                self.points = []

    def calcular_distancia(self, ponto1, ponto2):
        distancia_pixels = math.sqrt((ponto2[0] - ponto1[0])**2 + (ponto2[1] - ponto1[1])**2)
        print(distancia_pixels)
        return distancia_pixels

    def desenhar_pontos(self):
        with self.image.canvas:
            Color(1, 0, 0)  # Vermelho
            for point in self.points:
                Ellipse(pos=(point[0], point[1]), size=(5, 5))

if __name__ == "__main__":
    PointSelectionApp().run()
'''




#CÓDIGO COM LINHA E PONTO VERMELHO

"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
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
                self.desenhar_pontos()
                self.desenhar_linha()
                self.points = []

    def calcular_distancia(self, ponto1, ponto2):
        distancia_pixels = math.sqrt((ponto2[0] - ponto1[0])**2 + (ponto2[1] - ponto1[1])**2)
        return distancia_pixels

    def desenhar_pontos(self):
        with self.image.canvas:
            Color(1, 0, 0)  # Vermelho
            for point in self.points:
                Ellipse(pos=(point[0] - 5, point[1] - 5), size=(10, 10))

    def desenhar_linha(self):
        with self.image.canvas:
            Color(0, 0, 1)  # Azul
            x1, y1 = self.points[0]
            x2, y2 = self.points[1]
            Line(points=[x1, y1, x2, y2], width=1)

if __name__ == "__main__":
    PointSelectionApp().run()
"""


#CODIGO COM LINHA, PONTO VERMELHO, ARRASTA +-
'''
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
import math

class PointSelectionApp(App):
    def build(self):
        self.image_path = "levedura.jpg"  # Substitua pelo caminho da sua imagem
        self.points = []
        self.drag_enabled = False

        layout = BoxLayout(orientation='vertical')

        self.image = Image(source=self.image_path, allow_stretch=True)
        self.image.bind(on_touch_down=self.iniciar_selecao)
        self.image.bind(on_touch_move=self.mover_ponto)
        layout.add_widget(self.image)

        self.label = Label(text="")
        layout.add_widget(self.label)

        button_select = Button(text="Selecionar Pontos")
        button_select.bind(on_press=self.toggle_drag)
        layout.add_widget(button_select)

        button_drag = Button(text="Mover Pontos")
        button_drag.bind(on_press=self.toggle_drag)
        layout.add_widget(button_drag)

        return layout

    def iniciar_selecao(self, instance, touch):
        if self.image.collide_point(*touch.pos) and not self.drag_enabled:
            self.points.append((touch.x, touch.y))

            if len(self.points) == 2:
                distancia = self.calcular_distancia(self.points[0], self.points[1])
                self.label.text = f'Distância: {distancia:.2f} pixels'
                self.desenhar_pontos()
                self.desenhar_linha()
                self.points = []

    def mover_ponto(self, touch):
        if self.drag_enabled and self.points:
            self.points[-1] = touch.pos
            self.image.canvas.clear()
            self.desenhar_pontos()
            self.desenhar_linha()

    def toggle_drag(self, instance):
        self.drag_enabled = not self.drag_enabled

    def calcular_distancia(self, ponto1, ponto2):
        distancia_pixels = math.sqrt((ponto2[0] - ponto1[0])**2 + (ponto2[1] - ponto1[1])**2)
        return distancia_pixels

    def desenhar_pontos(self):
        with self.image.canvas:
            Color(1, 0, 0)  # Vermelho
            for point in self.points:
                Ellipse(pos=(point[0] - 5, point[1] - 5), size=(10, 10))

    def desenhar_linha(self):
        with self.image.canvas:
            Color(0, 0, 1)  # Azul
            x1, y1 = self.points[0]
            x2, y2 = self.points[1]
            Line(points=[x1, y1, x2, y2], width=1)

if __name__ == "__main__":
    PointSelectionApp().run()

'''

#tentar rodar de novo:

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.core.window import Window
import math

class PointSelectionApp(App):
    def build(self):
        self.image_path = "levedura.jpg"  # Substitua pelo caminho da sua imagem
        self.points = []
        self.drag_enabled = False
        self.dragged_point_index = -1

        layout = BoxLayout(orientation='vertical')

        self.image = Image(source=self.image_path, allow_stretch=True)
        self.image.bind(on_touch_down=self.iniciar_selecao)
        self.image.bind(on_touch_move=self.mover_ponto)
        Window.bind(mouse_pos=self.on_mouse_pos)
        layout.add_widget(self.image)

        self.label = Label(text="")
        layout.add_widget(self.label)

        button_select = Button(text="Selecionar Pontos")
        button_select.bind(on_press=self.toggle_drag)
        layout.add_widget(button_select)

        button_drag = Button(text="Mover Pontos")
        button_drag.bind(on_press=self.toggle_drag)
        layout.add_widget(button_drag)

        return layout

    def iniciar_selecao(self, instance, touch):
        if self.image.collide_point(*touch.pos) and not self.drag_enabled:
            self.points.append((touch.x, touch.y))

            if len(self.points) == 2:
                distancia = self.calcular_distancia(self.points[0], self.points[1])
                self.label.text = f'Distância: {distancia:.2f} pixels'
                self.desenhar_pontos()
                self.desenhar_linha()
                self.points = []

    def on_mouse_pos(self, *args):
        if self.drag_enabled and self.dragged_point_index != -1:
            self.points[self.dragged_point_index] = Window.mouse_pos

    def mover_ponto(self, instance, touch):
        if self.drag_enabled and self.dragged_point_index != -1:
            self.points[self.dragged_point_index] = touch.pos
            self.image.canvas.clear()
            self.desenhar_pontos()
            self.desenhar_linha()

    def toggle_drag(self, instance):
        self.drag_enabled = not self.drag_enabled
        if not self.drag_enabled:
            self.dragged_point_index = -1

    def calcular_distancia(self, ponto1, ponto2):
        distancia_pixels = math.sqrt((ponto2[0] - ponto1[0])**2 + (ponto2[1] - ponto1[1])**2)
        return distancia_pixels

    def desenhar_pontos(self):
        with self.image.canvas:
            Color(1, 0, 0)  # Vermelho
            for point in self.points:
                Ellipse(pos=(point[0] - 5, point[1] - 5), size=(10, 10))

    def desenhar_linha(self):
        with self.image.canvas:
            Color(0, 0, 1)  # Azul
            x1, y1 = self.points[0]
            x2, y2 = self.points[1]
            Line(points=[x1, y1, x2, y2], width=1)

if __name__ == "__main__":
    PointSelectionApp().run()

