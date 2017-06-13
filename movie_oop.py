class Movie():
    """a story or event recorded by a camera as a set of moving images 
    and shown in a theater or on television; a motion picture.

    Attributes:
        Name: A string representing the movie's name.
        length: An integer representing running time of the movie.
    """

    def __init__(self, name, length):
        self.name = name
        self.length = length
        # self.done_shooting = False
        # shoot()

    # def shoot(self):
    #     self.done_shooting = True
    #     return self.name + " Status: Shooting successful!"

    def play(self):
        return str(self.name) + " is Playing. Length: " + str(self.length)

class Comedy(Movie):
    """ A comedy is a movie which is usually filled with jokes and
    actors/actresses just being stupid!
    """

    def play(self):
        return "Start laughing already because " + str(self.name) + \
        " is not going to spare your ribs!\n Length: " + str(self.length)

class Horror(Movie):
    """An horror is a scary movie
    """

    def play(self):
        return "Don't dare watch " + str(self.name) +" alone HUMAN! " \
        "\n Length: " + str(self.length)

class RealityShow(Movie):
    """A reality show, always a boring movie! Nothing to say.
    """
    pass