import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.metrics import dp
from kivy.core.window import Window

from src.controller.estudiante_controller import (
    insertar_estudiante,
    consultar_estudiantes,
    actualizar_estudiante,
    eliminar_estudiante
)

Window.size = (500, 650)


class EstudiantesApp(App):

    def build(self):
        print("APP INICIANDO")

        layout = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=10
        )

        titulo = Label(
            text="Gestión de Estudiantes",
            font_size=28,
            bold=True,
            size_hint_y=None,
            height=60
        )

        layout.add_widget(titulo)

        self.input_id = TextInput(
            hint_text="ID estudiante",
            multiline=False,
            size_hint_y=None,
            height=45
        )

        self.input_nombre = TextInput(
            hint_text="Nombre",
            multiline=False,
            size_hint_y=None,
            height=45
        )

        self.input_correo = TextInput(
            hint_text="Correo",
            multiline=False,
            size_hint_y=None,
            height=45
        )

        self.input_carrera = TextInput(
            hint_text="Carrera",
            multiline=False,
            size_hint_y=None,
            height=45
        )

        layout.add_widget(self.input_id)
        layout.add_widget(self.input_nombre)
        layout.add_widget(self.input_correo)
        layout.add_widget(self.input_carrera)

        boton_insertar = Button(
            text="Insertar estudiante",
            size_hint_y=None,
            height=50
        )

        boton_buscar = Button(
            text="Consultar estudiantes",
            size_hint_y=None,
            height=50
        )

        boton_actualizar = Button(
            text="Actualizar estudiante",
            size_hint_y=None,
            height=50
        )

        boton_eliminar = Button(
            text="Eliminar estudiante",
            size_hint_y=None,
            height=50
        )

        boton_insertar.bind(on_press=self.insertar)
        boton_buscar.bind(on_press=self.consultar)
        boton_actualizar.bind(on_press=self.actualizar)
        boton_eliminar.bind(on_press=self.eliminar)

        layout.add_widget(boton_insertar)
        layout.add_widget(boton_buscar)
        layout.add_widget(boton_actualizar)
        layout.add_widget(boton_eliminar)

        self.resultado = Label(
            text="",
            font_size=16
        )

        layout.add_widget(self.resultado)

        return layout

    def insertar(self, instance):

        try:

            insertar_estudiante(
                self.input_nombre.text,
                self.input_correo.text,
                self.input_carrera.text
            )

            self.resultado.text = "Estudiante insertado correctamente"

        except Exception as e:

            self.mostrar_error(str(e))

    def consultar(self, instance):

        try:

            estudiantes = consultar_estudiantes()

            texto = ""

            for estudiante in estudiantes:

                texto += (
                    f"{estudiante.id} | "
                    f"{estudiante.nombre} | "
                    f"{estudiante.correo} | "
                    f"{estudiante.carrera}\n"
                )

            self.resultado.text = texto

        except Exception as e:

            self.mostrar_error(str(e))

    def actualizar(self, instance):

        try:

            actualizar_estudiante(
                int(self.input_id.text),
                self.input_nombre.text,
                self.input_correo.text,
                self.input_carrera.text
            )

            self.resultado.text = "Estudiante actualizado"

        except Exception as e:

            self.mostrar_error(str(e))

    def eliminar(self, instance):

        try:

            eliminar_estudiante(
                int(self.input_id.text)
            )

            self.resultado.text = "Estudiante eliminado"

        except Exception as e:

            self.mostrar_error(str(e))

    def mostrar_error(self, mensaje):

        popup = Popup(
            title="Error",
            content=Label(text=mensaje),
            size_hint=(None, None),
            size=(400, 200)
        )

        popup.open()


if __name__ == "__main__":
    EstudiantesApp().run()