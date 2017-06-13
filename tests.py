import unittest
from movie_oop import Comedy, Horror, RealityShow

class MovieOOPTest(unittest.TestCase):
    """docstring for MovieOOPTest"""

    def test_comedy(self):
        self.comedy = Comedy("Fist Fight", 91)
        self.assertTrue(isinstance(self.comedy.play(), "Start laughing already because" \
         + "Fist Fight is not going to spare your ribs!\n Length: 91"))

    def test_horror(self):
        self.horror = Horror("Ouija: Origin of Evil", 99)
        self.assertTrue(isinstance(self.horror.play(), "Don't dare watch Ouija: Origin of Evil alone HUMAN! " \
        "\n Length: 99"))
    def test_realityshow(self):
        self.realityshow = RealityShow("Keeping up with the  Kardassians", 600)
        self.assertTrue(isinstance(self.realityshow.play(), "Keeping up with the  Kardassians is Playing. Length: 600"))



if __name__ == "__main__":
    unittest.main()