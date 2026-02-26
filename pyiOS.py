import toga
from toga.style import Pack
from toga.style.pack import CENTER, COLUMN
from toga.colors import rgb

class HolaMundoApp(toga.App):
    def startup(self):
        main_box = toga.Box(
            style=Pack(direction=COLUMN, align_items=CENTER, margin=20)
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

        main_box.add(self.label)
        main_box.add(boton)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def mostrar_hola_mundo(self, widget):
        self.label.text = "Hola Mundo !"
        self.label.style.color = rgb(255, 165, 0)


def main():
    # Nombre visible y ID de la app (ajústalo a tu dominio)
    return HolaMundoApp("MiAppPy", "org.ejemplo.holamundo", icon="resources/icon.png")

if __name__ == "__main__":
    app = main()
    app.main_loop()