import arcade
import arcade.gui

# Tamaño de la ventana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Ejemplo de Menú con Arcade GUI"

class MainView(arcade.View):
    def __init__(self):
        super().__init__()
        # Manager para la GUI de esta vista
        self.manager = arcade.gui.UIManager()

        # Botón para abrir el menú
        menu_button = arcade.gui.UIFlatButton(text="Menú", width=200)

        @menu_button.event("on_click")
        def on_click_menu(event):
            menu = MenuView(self)
            self.window.show_view(menu)

        # Usamos un layout de anclaje para centrar el botón
        anchor = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor.add(
            anchor_x="center_x",
            anchor_y="center_y",
            child=menu_button
        )

    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()

    def on_draw(self):
        self.clear()
        # Aquí podría dibujarse algo del juego si hubiese
        self.manager.draw()


class MenuView(arcade.View):
    def __init__(self, previous_view: MainView):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.previous_view = previous_view

        # Creamos botones del menú
        btn_start = arcade.gui.UIFlatButton(text="Comenzar", width=200)
        btn_options = arcade.gui.UIFlatButton(text="Opciones", width=200)
        btn_quit = arcade.gui.UIFlatButton(text="Salir", width=200)

        # Layout tipo caja (vertical) para organizar los botones
        vbox = arcade.gui.UIBoxLayout()

        vbox.add(btn_start)
        vbox.add(btn_options)
        vbox.add(btn_quit)

        # Anclar ese layout al centro
        anchor = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor.add(
            anchor_x="center_x",
            anchor_y="center_y",
            child=vbox
        )

        # Asociar eventos de clic
        @btn_start.event("on_click")
        def on_click_start(event):
            # Por simplicidad, volvemos a la vista anterior (o podrías cargar la vista de juego)
            self.window.show_view(self.previous_view)

        @btn_options.event("on_click")
        def on_click_options(event):
            print("Mostrar opciones (a implementar)")

        @btn_quit.event("on_click")
        def on_click_quit(event):
            arcade.exit()

    def on_show_view(self):
        arcade.set_background_color(arcade.color.GRAY)
        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()

    def on_draw(self):
        self.clear()
        self.manager.draw()


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=False)
    main_view = MainView()
    window.show_view(main_view)
    arcade.run()


if __name__ == "__main__":
    main()
