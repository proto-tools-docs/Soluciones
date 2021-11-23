"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Ingresar un texto que contenga letras y números. Obtener la suma de
todos los números incluidos en el texto.

Ejemplo:

texto = "El 23 de mayo de 1973 se inauguró el edificio CPM, el cual" \
    " se encontraba en la calle Rawson al 1300"

Resultado: 23 + 1773 + 1300 = 3296
"""
from unittest import main, TestCase


def solver(s: str) -> int:
    return sum(int(x) for x in s.split() if x.isdigit())


def main_():
    s = input('Ingrese un texto: ')
    print(solver(s))


class Test(TestCase):

    data = (
        ("El 23 de mayo de 1973 se inauguró el edificio CPM, el cual" \
            " se encontraba en la calle Rawson al 1300", 3296),
        ("La última versión estable fue el 4 de octubre del 2021", 2025),
    )

    def test_solver(self):
        for text, expected in self.data:
            self.assertEqual(solver(text), expected)


if __name__ == "__main__":
    main()