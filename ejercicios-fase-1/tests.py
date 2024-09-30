import unittest as unt
from colorama import Fore, Style
from index import es_par, es_palindromo, fibonacci, contar_palabras

# Test es_par

class TestEsPar(unt.TestCase):
    def test_par(self):
        # print(Fore.GREEN + "Test Passed" + Style.RESET_ALL)
        self.assertTrue(es_par(4))
        print(Fore.BLUE + "Fallo Test" + Style.RESET_ALL)
            

    def test_impar(self):
        #print(Fore.RED + "Test Failed" + Style.RESET_ALL)
        self.assertFalse(es_par(5))
        

# Test
class TestPalindromo(unt.TestCase):
    def test_palindromo(self):
        self.assertTrue(es_palindromo('radar'))
    
    def test_no_palindromo(self):
        self.assertFalse(es_palindromo('hello'))

# Test
class TestFibonacci(unt.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)

# Test
class TestContarPalabras(unt.TestCase):
    def test_conteo(self):
        self.assertEqual(contar_palabras("Hola mundo"), 2)

if __name__ == '__main__':
    unt.main()


