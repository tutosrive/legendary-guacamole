# Escribir logs
from io import TextIOWrapper
from datetime import datetime
import traceback
import os

# Ruta absoluta de este módulo
current_path:str = os.path.dirname(__file__)

class Logger:
    """Escribir registros de ejecución
    """
    def __init__(self, name:str = 'log.log') -> None:
        # Nombre del archivo
        self.name:str = name
        # Archivo abierto
        self.file:TextIOWrapper = self.__open()
        # Ruta absoluta del archivo
        self.path:str
    
    def __open(self) -> TextIOWrapper | int:
        """Abrir archivos

        Returns:
            `TextIOWrapper`: Archivo
                o
            `int`: `-1`: Error
        """
        try:
            self.path = os.path.abspath(self.name)
            # Retornar archivo
            return open(self.name, 'a', encoding='utf-8')
        except FileNotFoundError as e:
            # Escribir un resgistro "interno"
            self.__log(e)
            return -1

    def log(self, msg:str) -> None:
        """Crear registros

        Args:
            `msg:str`: Mensaje que se quiere registrar 
        """
        # Escribir mensaje de registro
        self.__write(self.__date(), msg)
        # Mostrar ruta del archivo log.log
        print(f'Revise {self.path} para ver los registros.')
    
    def log_e(self, e: Exception) -> None:
        """Regiistrar errores (`Excepcition`)

        Args:
            `e:Exception`: Excepción conla cual se trabajará
        """
        trace:dict = self.__traceback(e)
        msg:str = f'Exception: {e.__class__.__name__} - File: {trace.get('path')} - ErrorLine: {trace.get('line')} - Messsage: {e}'
        self.log(msg)

    def __write(self, date:datetime, msg:str) -> int:
        """Escribir registros

        Args:
            `msg:str`: Mensaje del registro que se escribirá

        Returns:
            `int`: Cantidad de caracteres escritos:
                `-1`: Ocurrió una `excepción`
                `>= 0`: Caracteres escritos
        """
        try:
            # Escribir mensaje en archivo
            self.file.writelines([f'{date} - {msg}\n'])
        except TypeError as e:
            # Crear registro en módulo
            self.__log(e)
            return -1
    
    def __date(self) -> datetime:
        """Obtener la fecha-hora actual

        Returns:
            `datetime`: Hora actual (Obtenida con `datetime.datetime.now()`)
        """
        return datetime.now()

    def __log(self, e:Exception) -> int:
        """Crear registros "internos" (Del propio módulo)

        Args:
            `e:Exception`: Excepción "capturada"

        Returns:
            `int`: Cantidad de caracteres escritos:
                `-1`: Ocurrió una `excepción`
                `>= 0`: Caracteres escritos
        """
        state:int
        try:
            # Registro de excepciones (Ruta de archivo y línea de error)
            trace:dict = self.__traceback(e)
            # Ruta absoluta de este archivo
            filename:str = os.path.join(current_path, 'log.log')
            print(f'Revise el archivo "log" que se encuentra en esta ruta: {filename}')
            # Escribir registro del error "interno"
            with open(filename, 'a', encoding='utf-8') as f:
                w = f.writelines([f'{self.__date()} - Exception: {e.__class__.__name__} -File: {trace.get('path')} - ErrorLine: {trace.get('line')} - Messsage: {e}\n'])
                f.close() 
                state = w
        except FileNotFoundError:
            state = -1
        except TypeError:
            state = -1
        except SyntaxError:
            state = -1
        # Estado del registro
        return state

    def __traceback(self, e:Exception) -> dict:
        """Obtener un registro preciso de la excepción

        Args:
            `e:Exception`: Exceeption con la cual se trabajará

        Returns:
            `dict`: Diccionario con claves: line (Línea del error), path (Ruta del archivo de error)
        """
        trace_back = traceback.extract_tb(e.__traceback__)
        return {'line': trace_back[-1][1], 'path': trace_back[-1][0]}
