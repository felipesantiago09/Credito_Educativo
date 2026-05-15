import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from src.controller.estudiante_controller import insertar_estudiante
from src.controller.estudiante_controller import consultar_estudiantes
from src.controller.estudiante_controller import eliminar_estudiante
from src.controller.estudiante_controller import actualizar_estudiante




Window.size = (560,1100)
Window.clearcolor = (0.96, 0.97, 0.99, 1)


AZUL_OSCURO  = (0.10, 0.22, 0.44, 1)
AZUL_MEDIO   = (0.18, 0.40, 0.75, 1)
VERDE        = (0.13, 0.65, 0.45, 1)
ROJO         = (0.80, 0.18, 0.18, 1)
BLANCO       = (1, 1, 1, 1)
GRIS_TEXTO   = (0.35, 0.38, 0.45, 1)
GRIS_BORDE   = (0.78, 0.83, 0.92, 1)



class TarjetaLayout(BoxLayout):
   

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self._redibujar, size=self._redibujar)

    def _redibujar(self, *_):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*BLANCO)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(16)])
            Color(*GRIS_BORDE)
            RoundedRectangle(
                pos=(self.x - 1, self.y - 1),
                size=(self.width + 2, self.height + 2),
                radius=[dp(16)]
            )
            Color(*BLANCO)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(16)])


class Encabezado(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(
            orientation='vertical',
            padding=[dp(24), dp(20)],
            size_hint_y=None,
            height=dp(55),
            **kwargs
        )
        self.bind(pos=self._redibujar, size=self._redibujar)

        etiqueta_titulo = Label(
            text="Crédito Educativo",
            font_size=dp(26),
            bold=True,
            color=BLANCO,
            size_hint_y=None,
            height=dp(40),
        )
        self.add_widget(etiqueta_titulo)

    def _redibujar(self, *_):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*AZUL_OSCURO)
            RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(16), dp(16), 0, 0]
            )

class BarraNavegacion(BoxLayout):

    def __init__(self, screen_manager, **kwargs):

        super().__init__(
            orientation='horizontal',
            spacing=dp(10),
            padding=[dp(10), dp(10)],
            size_hint_y=None,
            height=dp(60),
            **kwargs
        )

        boton_credito = Button(
            text="Crédito",
            background_normal='',
            background_color=AZUL_MEDIO,
            color=BLANCO,
            bold=True
        )

        boton_estudiantes = Button(
            text="Estudiantes",
            background_normal='',
            background_color=AZUL_OSCURO,
            color=BLANCO,
            bold=True
        )
        boton_gestion = Button(
            text="Gestión",
            background_normal='',
            background_color=VERDE,
            color=BLANCO,
            bold=True
        )

        boton_credito.bind(
            on_press=lambda x:
            setattr(screen_manager, 'current', 'credito')
        )

        boton_estudiantes.bind(
            on_press=lambda x:
            setattr(screen_manager, 'current', 'estudiantes')
        )
        boton_gestion.bind(
            on_press=lambda x:
            setattr(screen_manager, 'current', 'gestion')
        )

        self.add_widget(boton_credito)
        self.add_widget(boton_estudiantes)
        self.add_widget(boton_gestion)



def crear_etiqueta(texto: str) -> Label:
    return Label(
        text=texto,
        font_size=dp(14),
        color=GRIS_TEXTO,
        halign='left',
        size_hint_y=None,
        height=dp(22),
        text_size=(None, None),
    )


def crear_campo_texto(sugerencia: str) -> TextInput:
    
    return TextInput(
        hint_text=sugerencia,
        font_size=dp(18),
        foreground_color=(0.10, 0.15, 0.30, 1),
        background_color=BLANCO,
        cursor_color=AZUL_MEDIO,
        hint_text_color=(0.65, 0.70, 0.80, 1),
        padding=[dp(12), dp(10)],
        size_hint_y=None,
        height=dp(46),
        multiline=False,
        write_tab=False,
    )


# ── Aplicación principal ───────────────────────────────────────────────────────

class PantallaCredito(Screen):

    def __init__(self, screen_manager=None, **kwargs):

        super().__init__(**kwargs)

        self.screen_manager = screen_manager

        contenedor_raiz = BoxLayout(
            orientation='vertical',
            spacing=0
        )

        contenedor_raiz.add_widget(Encabezado())

        if self.screen_manager:

            contenedor_raiz.add_widget(
                BarraNavegacion(self.screen_manager)
            )

        contenedor_raiz.add_widget(
            self._construir_cuerpo()
        )

        self.add_widget(contenedor_raiz)
    def _construir_cuerpo(self) -> BoxLayout:
    
        cuerpo = BoxLayout(
            orientation='vertical',
            padding=[dp(20), dp(16)],
            spacing=dp(14),
            size_hint_y=1
        )
        cuerpo.add_widget(self._construir_formulario())
        cuerpo.add_widget(self._construir_boton_calcular())
        cuerpo.add_widget(self._construir_tarjeta_resultado())
        cuerpo.add_widget(Widget())
        return cuerpo

    def _construir_formulario(self) -> TarjetaLayout:
       
        tarjeta = TarjetaLayout(
            orientation='vertical',
            padding=[dp(20), dp(18)],
            spacing=dp(10),
            size_hint_y=None,
            height=dp(310)
        )

        tarjeta.add_widget(crear_etiqueta("Valor del crédito"))
        self.campo_monto = crear_campo_texto("Ej: 5000000")
        tarjeta.add_widget(self.campo_monto)

        tarjeta.add_widget(crear_etiqueta("Tasa de interés mensual"))
        self.campo_tasa = crear_campo_texto("Ej: 1.5    (máximo 4%)")
        tarjeta.add_widget(self.campo_tasa)

        tarjeta.add_widget(crear_etiqueta("Número de cuotas  (1 – 36)"))
        self.campo_plazo = crear_campo_texto("Ej: 24")
        tarjeta.add_widget(self.campo_plazo)

        return tarjeta

    def _construir_boton_calcular(self) -> Button:
        
        boton = Button(
            text="Calcular cuota",
            font_size=dp(17),
            bold=True,
            background_normal='',
            background_color=AZUL_MEDIO,
            color=BLANCO,
            size_hint_y=None,
            height=dp(52),
        )
        boton.bind(on_press=self.calcular_cuota)
        return boton

    def _construir_tarjeta_resultado(self) -> TarjetaLayout:
       
        self.tarjeta_resultado = TarjetaLayout(
            orientation='vertical',
            padding=[dp(16), dp(14)],
            spacing=dp(4),
            size_hint_y=None,
            height=dp(90),
            opacity=0,
        )

        etiqueta_titulo_resultado = Label(
            text="Cuota mensual a pagar",
            font_size=dp(13),
            color=GRIS_TEXTO,
            size_hint_y=None,
            height=dp(20),
        )
        self.etiqueta_valor_resultado = Label(
            text="",
            font_size=dp(30),
            bold=True,
            color=VERDE,
            size_hint_y=None,
            height=dp(44),
        )
        self.tarjeta_resultado.add_widget(etiqueta_titulo_resultado)
        self.tarjeta_resultado.add_widget(self.etiqueta_valor_resultado)
        return self.tarjeta_resultado

   

    def calcular_cuota(self, *_):
        
        from model import logica_Credito

        self.tarjeta_resultado.opacity = 0
        self.etiqueta_valor_resultado.color = VERDE

        try:
            monto = self._leer_decimal(self.campo_monto.text)
            tasa  = self._leer_decimal(self.campo_tasa.text) / 100
            plazo = self._leer_entero(self.campo_plazo.text)

            cuota = round(logica_Credito.calcular_cuota(monto, tasa, plazo), 2)
            self.etiqueta_valor_resultado.text = self._formatear_moneda(cuota)
            self.tarjeta_resultado.opacity = 1

        except ValueError:
            self._mostrar_error(
                "Valor inválido",
                "Por favor ingrese solo números en todos los campos.\n"
                "Ejemplo de tasa: 1.5  (sin el signo %)"
            )
        except Exception as error:
            self._mostrar_error(" No se pudo calcular", str(error))

    def _leer_decimal(self, texto: str) -> float:
        
        return float(texto.replace(',', '.').strip())

    def _leer_entero(self, texto: str) -> int:
        
        return int(texto.strip())

    def _formatear_moneda(self, valor: float) -> str:
        
        return f"$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

    def _mostrar_error(self, titulo: str, mensaje: str):
        
        contenido = BoxLayout(
            orientation='vertical',
            padding=[dp(20), dp(16)],
            spacing=dp(12)
        )

       
        etiqueta_mensaje = Label(
            text=mensaje,
            font_size=dp(14),
            color=BLANCO,
            halign='center',
            text_size=(dp(320), None),
        )

        boton_cerrar = Button(
            text="Entendido",
            font_size=dp(15),
            bold=True,
            background_normal='',
            background_color=ROJO,
            color=BLANCO,
            size_hint_y=None,
            height=dp(44),
        )

        contenido.add_widget(etiqueta_mensaje)
        contenido.add_widget(boton_cerrar)

        ventana_error = Popup(
            title=titulo,
            title_color=BLANCO,
            title_size=dp(16),
            content=contenido,
            size_hint=(None, None),
            size=(dp(360), dp(200)),
            separator_color=ROJO,
        )
        boton_cerrar.bind(on_press=ventana_error.dismiss)
        ventana_error.open()

class PantallaEstudiantes(Screen):

    def __init__(self, screen_manager=None, **kwargs):

        super().__init__(**kwargs)

        self.screen_manager = screen_manager

        layout = BoxLayout(
            orientation='vertical',
            spacing=0
        )

        layout.add_widget(Encabezado())

        if self.screen_manager:

            layout.add_widget(
                BarraNavegacion(self.screen_manager)
            )

        contenido = BoxLayout(
            orientation='vertical',
            padding=[dp(20), dp(80)],
            spacing=dp(20)
        )

        tarjeta = TarjetaLayout(
            orientation='vertical',
            padding=[dp(20), dp(20)],
            spacing=dp(10),
            size_hint_y=None,
            height=dp(300)
        )

        tarjeta.bind(minimum_height=tarjeta.setter('height'))
        

        titulo = Label(
            text="Gestión de Estudiantes",
            font_size=dp(24),
            bold=True,
            color=AZUL_OSCURO,
            size_hint_y=None,
            height=dp(40)
        )

        tarjeta.add_widget(titulo)

        tarjeta.add_widget(
            crear_etiqueta("Nombre")
        )

        self.campo_nombre = crear_campo_texto(
            "Ingrese nombre"
        )

        tarjeta.add_widget(self.campo_nombre)

        tarjeta.add_widget(
            crear_etiqueta("Correo")
        )

        self.campo_correo = crear_campo_texto(
            "Ingrese correo"
        )

        tarjeta.add_widget(self.campo_correo)

        tarjeta.add_widget(
            crear_etiqueta("Carrera")
        )

        self.campo_carrera = crear_campo_texto(
            "Ingrese carrera"
        )

        tarjeta.add_widget(self.campo_carrera)

        boton_guardar = Button(
            text="Guardar estudiante",
            background_normal='',
            background_color=AZUL_MEDIO,
            color=BLANCO,
            bold=True,
            size_hint_y=None,
            height=dp(30)
        )

        boton_guardar.bind(
            on_press=self.guardar_estudiante
        )

        tarjeta.add_widget(boton_guardar)
        

        contenido.add_widget(tarjeta)
        scroll = ScrollView()

        self.lista_estudiantes = Label(
            text="",
            color=GRIS_TEXTO,
            halign='left',
            valign='top',
            size_hint_y=None
        )

        self.lista_estudiantes.bind(
            texture_size=self.lista_estudiantes.setter('size')
        )

        scroll.add_widget(self.lista_estudiantes)

        contenido.add_widget(scroll)

        self.actualizar_lista()

        layout.add_widget(contenido)

        self.add_widget(layout)

    def guardar_estudiante(self, *_):

        nombre = self.campo_nombre.text.strip()
        correo = self.campo_correo.text.strip()
        carrera = self.campo_carrera.text.strip()

        if not nombre or not correo or not carrera:

            print("Campos vacíos")
            return
        try:
            insertar_estudiante(
                nombre,
                correo,
                carrera
            )

            print("Estudiante guardado")

            self.campo_nombre.text = ""
            self.campo_correo.text = ""
            self.campo_carrera.text = ""
            self.actualizar_lista()
        except Exception:

            print("ese correo ya Existe")

    def eliminar_estudiante_gui(self, *_):

        id_estudiante = self.campo_eliminar.text.strip()

        if not id_estudiante:

            print("Ingrese ID")
            return

        eliminar_estudiante(
            int(id_estudiante)
        )

        self.campo_eliminar.text = ""

        self.actualizar_lista()

        print("Estudiante eliminado")

    def actualizar_estudiante_gui(self, *_):

        id_estudiante = self.campo_actualizar_id.text.strip()

        nuevo_nombre = self.campo_nuevo_nombre.text.strip()

        if not id_estudiante or not nuevo_nombre:

            print("Complete los campos")
            return

        actualizar_estudiante(
            int(id_estudiante),
            nuevo_nombre
        )

        self.campo_actualizar_id.text = ""
        self.campo_nuevo_nombre.text = ""

        self.actualizar_lista()

        print("Estudiante actualizado")

    def actualizar_lista(self):

        estudiantes = consultar_estudiantes()

        texto = ""

        for e in estudiantes:

            texto += (
                f"{e.id} | "
                f"{e.nombre} | "
                f"{e.correo} | "
                f"{e.carrera}\n"
            )

        self.lista_estudiantes.text = texto

class PantallaGestion(Screen):

    def __init__(self, screen_manager=None, **kwargs):

        super().__init__(**kwargs)

        self.screen_manager = screen_manager

        layout = BoxLayout(
            orientation='vertical',
            spacing=0
        )

        layout.add_widget(Encabezado())

        if self.screen_manager:

            layout.add_widget(
                BarraNavegacion(self.screen_manager)
            )

        contenido = BoxLayout(
            orientation='vertical',
            padding=[dp(30), dp(60)],
            spacing=dp(20)
        )

        tarjeta = TarjetaLayout(
            orientation='vertical',
            padding=[dp(20), dp(20)],
            spacing=dp(10),
            size_hint_y=None,
            height=dp(300)
        )
        tarjeta.bind(minimum_height=tarjeta.setter('height'))

        titulo = Label(
            text="Gestión de Estudiantes",
            font_size=dp(24),
            bold=True,
            color=AZUL_OSCURO,
            size_hint_y=None,
            height=dp(20)
        )

        tarjeta.add_widget(titulo)

        # ───── ELIMINAR ─────

        tarjeta.add_widget(
            crear_etiqueta("ID para eliminar")
        )

        self.campo_eliminar = crear_campo_texto(
            "Ingrese ID"
        )

        tarjeta.add_widget(self.campo_eliminar)

        boton_eliminar = Button(
            text="Eliminar estudiante",
            background_normal='',
            background_color=ROJO,
            color=BLANCO,
            bold=True,
            size_hint_y=None,
            height=dp(50)
        )

        boton_eliminar.bind(
            on_press=self.eliminar_estudiante_gui
        )

        tarjeta.add_widget(boton_eliminar)

        # ───── ACTUALIZAR ─────

        tarjeta.add_widget(
            crear_etiqueta("ID para actualizar")
        )

        self.campo_actualizar_id = crear_campo_texto(
            "Ingrese ID"
        )

        tarjeta.add_widget(self.campo_actualizar_id)

        tarjeta.add_widget(
            crear_etiqueta("Nuevo nombre")
        )

        self.campo_nuevo_nombre = crear_campo_texto(
            "Ingrese nuevo nombre"
        )

        tarjeta.add_widget(self.campo_nuevo_nombre)

        boton_actualizar = Button(
            text="Actualizar estudiante",
            background_normal='',
            background_color=VERDE,
            color=BLANCO,
            bold=True,
            size_hint_y=None,
            height=dp(50)
        )

        boton_actualizar.bind(
            on_press=self.actualizar_estudiante_gui
        )

        tarjeta.add_widget(boton_actualizar)

        contenido.add_widget(tarjeta)
        contenido.add_widget(Widget())

        layout.add_widget(contenido)

        self.add_widget(layout)

    def eliminar_estudiante_gui(self, *_):

        id_estudiante = self.campo_eliminar.text.strip()

        if not id_estudiante:

            print("Ingrese ID")
            return

        eliminar_estudiante(
            int(id_estudiante)
        )

        self.campo_eliminar.text = ""

        print("Estudiante eliminado")

    def actualizar_estudiante_gui(self, *_):

        id_estudiante = self.campo_actualizar_id.text.strip()

        nuevo_nombre = self.campo_nuevo_nombre.text.strip()

        if not id_estudiante or not nuevo_nombre:

            print("Complete los campos")
            return

        actualizar_estudiante(
            int(id_estudiante),
            nuevo_nombre
        )

        self.campo_actualizar_id.text = ""
        self.campo_nuevo_nombre.text = ""

        print("Estudiante actualizado")

class MainApp(App):

    def build(self):

        sm = ScreenManager()

        pantalla_credito = PantallaCredito(
            screen_manager=sm,
            name="credito"
        )

        sm.add_widget(pantalla_credito)

        pantalla_estudiantes = PantallaEstudiantes(
            screen_manager=sm,
            name="estudiantes"
        )

        sm.add_widget(pantalla_estudiantes)

        pantalla_gestion = PantallaGestion(
            screen_manager=sm,
            name="gestion"
        )

        sm.add_widget(pantalla_gestion)

        return sm

if __name__ == "__main__":
    MainApp().run()