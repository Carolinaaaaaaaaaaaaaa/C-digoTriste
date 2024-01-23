
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

        self.background_image = Image(source=self.image_path, allow_stretch=True)
        layout.add_widget(self.background_image)


        self.image = Image(source=self.image_path, allow_stretch=True)
        self.image.opacity = 1
        self.image.height = 0

        self.image.bind(on_touch_down=self.iniciar_selecao)
   
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
        if not self.drag_enabled:
            
            if len(self.points) == 0:
                
                self.reset() # resetar para foto normal
                

            self.points.append(touch.pos)
            
            if len(self.points) == 4:
                distancia = self.calcular_distancia(self.points[0], self.points[1])
          
                distancia2 = self.calcular_distancia(self.points[2], self.points[3])
                
                self.label.text = f'Distância: {distancia:.2f} pixels - Distância 2 : {distancia2:.2f} pixels'
                
                
                self.desenhar_pontos()
                self.desenhar_linha()

                
                self.points = []
            
               
                    
                
                
                
                
                

    def on_mouse_pos(self, *args):
        if self.drag_enabled and self.dragged_point_index != -1:
            self.points[self.dragged_point_index] = Window.mouse_pos

    def mover_ponto(self, touch):
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

    def reset(self):
        with self.image.canvas:
            self.image.canvas.clear()

            

    def desenhar_linha(self):
        with self.image.canvas:
            Color(0, 0, 1)  # Azul
            x1, y1 = self.points[0]
            x2, y2 = self.points[1]
            x3, y3 = self.points[2]
            x4, y4 = self.points[3]

            Line(points=[x1, y1, x2, y2], width=1)
            Line(points=[x3, y3, x4, y4], width=1)

            

if __name__ == "__main__":
    PointSelectionApp().run()

 