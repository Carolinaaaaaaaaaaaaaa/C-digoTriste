# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 18:32:04 2024

@author: Carol
"""
#talvez de certo

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
        self.image_path = "levedura.jpg"
        self.points = []
        self.drag_enabled = False
        self.dragged_point_index = -1

        layout = BoxLayout(orientation='vertical')

        self.image_widget = Image(source=self.image_path, allow_stretch=True)
        self.image_canvas = self.image_widget.canvas
        self.points_canvas = self.image_widget.canvas.after
        self.image_widget.bind(on_touch_down=self.iniciar_selecao)
        self.image_widget.bind(on_touch_move=self.mover_ponto)
        Window.bind(mouse_pos=self.on_mouse_pos)
        layout.add_widget(self.image_widget)

        self.label = Label(text="")
        layout.add_widget(self.label)

        button_select = Button(text="Selecionar Pontos")
        button_select.bind(on_press=self.habilitar_selecao)
        layout.add_widget(button_select)

        button_drag = Button(text="Mover Pontos")
        button_drag.bind(on_press=self.habilitar_movimento)
        layout.add_widget(button_drag)

        return layout

    def iniciar_selecao(self, instance, touch):
        print("iniciar_selecaooo")
        #breakpoint()
        if self.image_widget.collide_point(*touch.pos) and not self.drag_enabled:
            self.points.append((touch.x, touch.y))
            self.desenhar_pontos()

            if len(self.points) == 2:
                distancia = self.calcular_distancia(self.points[0], self.points[1])
                self.label.text = f'Distância: {distancia:.2f} pixels'
                self.desenhar_linha()
                self.points = []

    def on_mouse_pos(self, *args):
        if self.drag_enabled and self.dragged_point_index != -1:
            self.points[self.dragged_point_index] = Window.mouse_pos
            self.desenhar_pontos()

    def mover_ponto(self, instance, touch):
        print("moveu")
        if self.drag_enabled and self.dragged_point_index != -1:
            self.points[self.dragged_point_index] = touch.pos
            self.desenhar_pontos()
            self.desenhar_linha()

    def habilitar_selecao(self, instance):
        self.drag_enabled = False
        self.dragged_point_index = -1

    def habilitar_movimento(self, instance):
        self.drag_enabled = True

    def calcular_distancia(self, ponto1, ponto2):
        distancia_pixels = math.sqrt((ponto2[0] - ponto1[0])**2 + (ponto2[1] - ponto1[1])**2)
        return distancia_pixels

    def desenhar_pontos(self):
        self.points_canvas.clear()
        with self.points_canvas:
            Color(1, 0, 0)
            for point in self.points:
                Ellipse(pos=(point[0] - 5, point[1] - 5), size=(10, 10))

    def desenhar_linha(self):
        with self.points_canvas:
            Color(0, 0, 1)
            x1, y1 = self.points[0]
            x2, y2 = self.points[1]
            Line(points=[x1, y1, x2, y2], width=1)

if __name__ == "__main__":
    PointSelectionApp().run()
