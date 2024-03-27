import unittest

def is_palindrome(value):
    print(value)
    print(value[::-1])
    if value == value[::-1]:
        return True
    else:
        return False

    # for indice in range(len(value)):
    #     reverse = -(indice + 1)
    #     if value [indice] != value[reverse]:
    #         return False


class Test_is_palindrome(unittest.TestCase):

    def test_with_a(self):
        input = 'abca'
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_ala(self):
        input = 'ala'
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_neuquen(self):
        input = 'neuquen'
        result = is_palindrome(input) 
        self.assertTrue(result)

    def test_with_oso(self):
        input = 'oso'
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_hola(self):
        input = 'hola'
        result = is_palindrome(input)
        self.assertFalse(result)

    def test_with_oso(self):
        input = 'oso'
        result = is_palindrome(input)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()


