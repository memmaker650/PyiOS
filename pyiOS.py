import toga
from toga.style import Pack
from toga.style.pack import CENTER, COLUMN, ROW, END
from toga.colors import rgb

import sqlite3
import logging

class HolaMundoApp(toga.App):
    sqliteConnection = 0

    def open_document(self, file):
        # Ignorar cualquier documento que intente abrir la app
        return
        
    def arrancarDB(self):
        self.sqliteConnection = sqlite3.connect("./DB/dbiOS.db")
        cursor = self.sqliteConnection.cursor()
        logging.info("Successfully Connected to SQLite")

        logging.info('Creación Base de Datos y Tablas principales.')
        #cursor.execute("""CREATE DATABASE OctoPussyDB""")
        try:
            # cursor.execute("""CREATE TABLE partida (id integer PRIMARY KEY, fecha Date, jugador text NOT NULL, puntuacion integer, nivel integer NOT NULL)""")
            # cursor.execute("""CREATE TABLE estadisticas (id interger PRIMARY KEY, jugador text NOT NULL, partida integer, disparos integer, nivelmax integer NOT NULL, enemigosmuertos integer, vidasusadas integer)""")
            # sqliteConnection.commit()
            logging.info('Ejecución SQL creación tablas.')
        except sqlite3.Error as error:
            logging.error("Failed to Tables in SQLite", error)
        finally:
            logging.info('Tablas DB creadas')

        logging.info('Fin acciones Base de Datos')

    def cerrarDB(self):
        #Cerramos base de datos
        self.sqliteConnection.close()
        logging.info("The SQLite connection is closed")

    # -------- Pantalla 1 (inicial) --------
    def construir_pantalla_inicial(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, margin=20))

        contenido_box = toga.Box(
            style=Pack(direction=COLUMN, align_items=CENTER)
        )

        # Texto inicial encima del botón
        self.label = toga.Label(
            "Pulsa el botón",
            style=Pack(margin_bottom=20, text_align=CENTER)
        )

        # Botón que cambia el texto
        boton = toga.Button(
            "Botón",
            on_press=self.mostrar_hola_mundo,
            style=Pack(margin=10)
        )

        contenido_box.add(self.label)
        contenido_box.add(boton)

        # Espaciador vertical para empujar la barra inferior hacia abajo
        espaciador_vertical = toga.Box(style=Pack(flex=1))

        # Barra inferior con botón a la derecha
        barra_inferior = toga.Box(
            style=Pack(margin_left=430, direction=COLUMN, horizontal_align_items=END)
        )

        boton_siguiente = toga.Button(
            "Siguiente ▶",
            on_press=self.ir_a_pantalla_dos,
            style=Pack(margin=10)
        )

        barra_inferior.add(boton_siguiente)

        main_box.add(contenido_box)
        main_box.add(espaciador_vertical)
        main_box.add(barra_inferior)

        return main_box

    def mostrar_hola_mundo(self, widget):
        self.label.text = "Hola Mundo !"
        self.label.style.color = rgb(255, 165, 0)

    def ir_a_pantalla_dos(self, widget):
        self.main_window.content = self.construir_pantalla_dos()

    # -------- Pantalla 2 --------
    def construir_pantalla_dos(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, margin=20))

        contenido_box = toga.Box(
            style=Pack(direction=COLUMN, align_items=CENTER)
        )

        self.label_pantalla_dos = toga.Label(
            "Segunda pantalla",
            style=Pack(margin_bottom=20, text_align=CENTER)
        )

        boton_mostrar_texto = toga.Button(
            "Mostrar texto",
            on_press=self.mostrar_texto_segunda,
            style=Pack(margin=10)
        )

        contenido_box.add(self.label_pantalla_dos)
        contenido_box.add(boton_mostrar_texto)

        espaciador = toga.Box(style=Pack(flex=1))

        # Barra inferior con botón a la izquierda (por defecto)
        barra_inferior = toga.Box(
            style=Pack(direction=ROW)
        )

        boton_volver = toga.Button(
            "◀ Volver",
            on_press=self.volver_pantalla_inicial,
            style=Pack(margin=10)
        )

        barra_inferior.add(boton_volver)

        main_box.add(contenido_box)
        main_box.add(espaciador)
        main_box.add(barra_inferior)

        return main_box

    def mostrar_texto_segunda(self, widget):
        self.label_pantalla_dos.text = "Texto de la segunda pantalla"

    def volver_pantalla_inicial(self, widget):
        self.main_window.content = self.construir_pantalla_inicial()

    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.arrancarDB()
        # Pantalla inicial al arrancar
        self.main_window.content = self.construir_pantalla_inicial()
        self.main_window.show()


def main():
    logging.basicConfig(filename="./log/pyiOS.log", level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
    logging.warning("Inicio pyiOS!!!")

    # Nombre visible y ID de la app (ajústalo a tu dominio)
    return HolaMundoApp("MiAppPy", "org.ejemplo.holamundo", icon="resources/icon.png")

if __name__ == "__main__":
    app = main()
    app.main_loop()