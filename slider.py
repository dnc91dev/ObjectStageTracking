class SlidingObject:
    def __init__(self, name, speed, direction):
        """
        Constructor de la clase SlidingObject.

        Args:
            name (str): El nombre del objeto que se desliza.
            speed (float): La velocidad del objeto que se desliza.
            direction (str): La dirección en la que se desliza el objeto.
        """
        #aca se encuentra la diferencia para encapsular, en este caso encapsular variables
        self.__name = name
        self.__speed = speed
        self.__direction = direction

    def move(self):
        """
        Mover el objeto que se desliza.

        Returns:
            str: Una cadena que indica el movimiento del objeto.
        """
        if self.__direction == "forward":
            return f"{self.__name} se desliza hacia adelante a una velocidad de {self.__speed} m/s."
        elif self.__direction == "backward":
            return f"{self.__name} se desliza hacia atrás a una velocidad de {self.__speed} m/s."
        else:
            return f"{self.__name} no se mueve."

    def __str__(self):
        """
        Representación en cadena del objeto que se desliza.

        Returns:
            str: Una cadena que describe el objeto que se desliza.
        """
        return f"{self.__name} se desliza a una velocidad de {self.__speed} m/s en la dirección {self.__direction}."


# Ejemplo de uso
sliding_object = SlidingObject("Bola", 5.0, "forward")
print(sliding_object.move())  # Output: Bola se desliza hacia adelante a una velocidad de 5.0 m/s.
print(sliding_object)  # Output: Bola se desliza a una velocidad de 5.0 m/s en la dirección forward.
