class Estudiante:
    """Representa un estudiante. No depende de ningún ORM ni base de datos."""

    def __init__(self, id=None, nombre=None, correo=None, carrera=None):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.carrera = carrera

    def __repr__(self):
        return (
            f"<Estudiante(id={self.id}, nombre='{self.nombre}', "
            f"correo='{self.correo}', carrera='{self.carrera}')>"
        )

    def is_equal(self, otro):
        """Compara dos estudiantes por sus datos, sin considerar el id."""
        if not isinstance(otro, Estudiante):
            return False
        return (
            self.nombre == otro.nombre
            and self.correo == otro.correo
            and self.carrera == otro.carrera
        )
