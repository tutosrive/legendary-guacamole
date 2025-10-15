import arcade
import arcade.gui

# Tamaño de la ventana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Ejemplo con Modal Popup"

class HomeView(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        # No habilitar aún; se habilita en on_show_view

        # Crear botón para abrir modal
        self.btn_open_modal = arcade.gui.UIFlatButton(text="Abrir popup", width=200)
        @self.btn_open_modal.event("on_click")
        def on_click(event):
            self.show_modal()

        # Layout para centrar el botón
        anchor = arcade.gui.UIAnchorLayout()
        anchor.add(
            anchor_x="center_x",
            anchor_y="center_y",
            child=self.btn_open_modal
        )
        self.manager.add(anchor)

    def on_show_view(self):
        """Cuando esta vista es mostrada (se activa)."""
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        self.manager.enable()

    def on_hide_view(self):
        """Cuando la vista deja de estar activa."""
        self.manager.disable()

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def show_modal(self):
        """
        Función para crear y mostrar el popup/modal.
        Usamos UIMessageBox, que ya es un widget modal listo.
        """
        message_box = arcade.gui.UIMessageBox(
            width=300,
            height=180,
            title="Confirmación",
            message_text="¿Quieres continuar?",
            buttons=("Sí", "No")
        )

        @message_box.event("on_action")
        def on_action(event):
            # event.action (o event.text) es el botón presionado
            print("Botón pulsado:", event.action)
            # Por ejemplo:
            if event.action == "Sí":
                print("Usuario seleccionó Sí")
            else:
                print("Usuario seleccionó No")

        # Opcionalmente, podrías ocultar o desactivar el botón principal mientras el modal está abierto:
        self.btn_open_modal.visible = False

        # Cuando se cierra el modal (se hace click en algún botón), puedes restaurar visibilidad
        @message_box.event("on_hide")
        def on_hide(event):
            # Restaurar botón
            self.btn_open_modal.visible = True

        # Agregar el message_box al manager en una capa “superior”
        # layer default está bien; si tienes muchas capas puedes usar layer > 0.
        self.manager.add(message_box, layer=1)


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=False)
    home = HomeView()
    window.show_view(home)
    arcade.run()


if __name__ == "__main__":
    main()
