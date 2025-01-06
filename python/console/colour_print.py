class Print:
    """Imprimir mensajes por consola con color de texto (`error`, `warning`, `succes`, `info`)
    """
    def __init__(self) -> None:
        self.RES = '\u001B[0m' # Resetear color
        self.RED = '\u001B[31m'
        self.YELLOW = '\u001B[33m'
        self.BLUE = '\u001B[34m'
        self.GREEN = '\u001B[32m'

    def err(self, err:str) -> None:
        """Imprimir errores (Color Texto: Rojo)

        Args:
            `err:str`: Error que se imprimirá
        """
        self.__w(f'{self.RED}{err}{self.RES}')

    def inf(self, inf:str) -> None:
        """Imprimir información (Color Texto: Azul)

        Args:
            `inf:str`: Información que se imprimirá
        """
        self.__w(f'{self.BLUE}{inf}{self.RES}')

    def warn(self, warn:str) -> None:
        """Imprimir mensajes de precaución (Color Texto: Amarillo)

        Args:
            `warn:str`: Mensaje que se imprimirá
        """
        self.__w(f'{self.YELLOW}{warn}{self.RES}')

    def suc(self, suc:str) -> None:
        """Imprimir mensajes de éxito (Final de ejecución, podría ser...) (Color Texto: Verde)

        Args:
            `suc:str`: Mensaje que se imprimirá
        """
        self.__w(f'{self.GREEN}{suc}{self.RES}')

    def __w(self, msg:str) -> None:
        """Imprimir mensaje con colores

        Args:
            `msg:str`: Mensaje que se imprimirá
        """
        print(msg)

    def test(self) -> None:
        """Ejecutar prueba
        """
        try:
            a = ''
            a += 12
        except TypeError as e:
            self.err(f'Error: {e.__class__.__name__}, Mensaje: {e.__str__()}')
        self.inf('Hello World')
        self.warn('Precaución, tenga cuidado')
        self.suc('Ejecución finalizada...')

if __name__ == '__main__':
    p = Print()
    p.test()
