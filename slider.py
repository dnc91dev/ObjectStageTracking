class SlidingObject:
    def __init__(self, name, speed, direction):
        """
        Constructor de la clase SlidingObject.

        Args:
            name (str): El nombre del objeto que se desliza.
            speed (float): La velocidad del objeto que se desliza.
            direction (str): La dirección en la que se desliza el objeto.
        """
        self.name = name
        self.speed = speed
        self.direction = direction

    def move(self):
        """
        Mover el objeto que se desliza.

        Returns:
            str: Una cadena que indica el movimiento del objeto.
        """
        if self.direction == "forward":
            return f"{self.name} se desliza hacia adelante a una velocidad de {self.speed} m/s."
        elif self.direction == "backward":
            return f"{self.name} se desliza hacia atrás a una velocidad de {self.speed} m/s."
        else:
            return f"{self.name} no se mueve."

    def __str__(self):
        """
        Representación en cadena del objeto que se desliza.

        Returns:
            str: Una cadena que describe el objeto que se desliza.
        """
        return f"{self.name} se desliza a una velocidad de {self.speed} m/s en la dirección {self.direction}."


# Ejemplo de uso
sliding_object = SlidingObject("Bola", 5.0, "forward")
print(sliding_object.move())  # Output: Bola se desliza hacia adelante a una velocidad de 5.0 m/s.
print(sliding_object)  # Output: Bola se desliza a una velocidad de 5.0 m/s en la dirección forward.
