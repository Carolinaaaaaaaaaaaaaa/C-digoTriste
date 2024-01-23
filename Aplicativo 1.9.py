# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 20:42:13 2023

@author: Carol
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.core.window import Window
import math

class DraggableEllipse(Widget):
    def __init__(self, **kwargs):
        super(DraggableEllipse, self).__init__(**kwargs)
        self.size = (10, 10)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            return True
        return super(DraggableEllipse, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        if touch.grab_current == self:
            self.pos = (touch.x - self.width / 2, touch.y - self.height / 2)
            return True
        return super(DraggableEllipse, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        if touch.grab_current == self:
            touch.ungrab(self)
            return True
        return super(DraggableEllipse, self).on_touch_up(touch)

class PointSelectionApp(App):
    def build(self):
        self.image_path = "levedura.jpg"  # Substitua pelo caminho da sua imagem
        self.points = []

        layout = BoxLayout(orientation='vertical')

        container = Widget()

        self.image_widget = Image(source=self.image_path, allow_stretch=True)
        self.image_widget.bind(on_touch_down=self.iniciar_selecao)
        Window.bind(mouse_pos=self.on_mouse_pos)
        container.add_widget(self.image_widget)

        self.label = Label(text="")
        container.add_widget(self.label)

        self.points_container = Widget()
        container.add_widget(self.points_container)

        button_select = Button(text="Selecionar Pontos")
        button_select.bind(on_press=self.toggle_drag)
        layout.add_widget(button_select)

        button_drag = Button(text="Mover Pontos")
        button_drag.bind(on_press=self.toggle_drag)
        layout.add_widget(button_drag)

        layout.add_widget(container)

        return layout

    def iniciar_selecao(self, instance, touch):
        if self.image_widget.collide_point(*touch.pos) and not self.points:
            draggable_ellipse = DraggableEllipse(pos=(touch.x - 5, touch.y - 5))
            self.points.append(draggable_ellipse)
            self.points_container.add_widget(draggable_ellipse)

            if len(self.points) == 2:
                distancia = self.calcular_distancia(self.points[0].pos, self.points[1].pos)
                self.label.text = f'Distância: {distancia:.2f} pixels'

    def on_mouse_pos(self, *args):
        if self.points and self.drag_enabled and self.points[0].drag_touch is not None:
            self.desenhar_linha()

    def toggle_drag(self, instance):
        self.drag_enabled = not self.drag_enabled
        if not self.drag_enabled:
            self.desenhar_linha()

    def calcular_distancia(self, ponto1, ponto2):
        distancia_pixels = math.sqrt((ponto2[0] - ponto1[0])**2 + (ponto2[1] - ponto1[1])**2)
        return distancia_pixels

    def desenhar_linha(self):
        self.points_container.canvas.clear()
        with self.points_container.canvas:
            Color(1, 0, 0)  # Vermelho
            for point in self.points:
                Ellipse(pos=point.pos, size=point.size)

            if len(self.points) == 2:
                Color(0, 0, 1)  # Azul
                x1, y1 = self.points[0].pos
                x2, y2 = self.points[1].pos
                Line(points=[x1 + 5, y1 + 5, x2 + 5, y2 + 5], width=1)

if __name__ == "__main__":
    PointSelectionApp().run()



