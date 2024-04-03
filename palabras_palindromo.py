import unittest

def obtener_cantidad_de_palabras_palindrome(palabras):
    resultado = 0
    for palabra in palabras: #por cada palabra en la lista palabras
        palabra = palabra.replace(" ", "").replace(",", "").replace("-", "").lower() #elimina espacios, comas y guiones del string de cada palabra
        if palabra == palabra[::-1]:  #si la palabra sin espacios, comas ni guiones es igual a la palabra leida al reves
            resultado += 1  #se le suma uno al contador de palindromos
    return resultado  #devuelve cuantos palindromos hay en la list


class TestCantidadDePalabrasPalindromes(unittest.TestCase):
    def test_cantidad_de_palabras_palindromes_simple(self):
        palabras = ["ala"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 1)

    def test_cantidad_de_palabras_palindromes_con_2(self):
        palabras = ["ala", "neuquen"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_3(self):
        palabras = ["ala", "neuquen", "hola"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_4(self):
        palabras = ["ala", "neuquen", "hola", "programacion"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_5(self):
        palabras = ["ala", "neuquen", "hola", "programacion", "palap"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 3)

    def test_cantidad_de_palabras_palindromes_complejo(self):
        palabras = ["ala", "neuquen", "hola", "programacion", "palap", "neu  quen"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 4)

    def test_cantidad_de_palabras_palindromes_complejo_2(self):
        palabras = [
            "ala",
            "neuquen",
            "hola",
            "programacion",
            "palap",
            "neu  quen",
            "agita falsos usos la fatiga",
            "presidente de la camara de diputados: martin menem",
			"A man, a plan, a canal - Panama"
        ]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 6)

    # def test_cantidad_de_palabras_palindromes_complejo_2(self):
    #     palabras = [
    #         "ala",
    #         "neuquen",
    #         "hola",
    #         "programacion",
    #         "palap",
    #         "neu  quen",
    #         "agita falsos usos la fatiga",
    #         "presidente de la camara de diputados: martin menem",
    #     ]
    #     resultado = obtener_cantidad_de_palabras_palindrome(palabras)
    #     self.assertEqual(resultado, 5)


if __name__ == '__main__':
    unittest.main()