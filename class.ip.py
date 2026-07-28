class animal:  # parent
    description = " this class create animals"

    def __init__(self, voice):
        self.voice = voice

    def make_voice(self):
        print(f" animal makes {self.voice} ")


class dog(animal):  # child
    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    def introduce(self):
        print(f"{self.name}says: {self.sound}-{self.sound}")

    def protect(self):
        print(f" yes , {self.name} is protecting you")


dog = dog("gaban", "arr vooww", True)
dog.introduce()
dog.make_voice()
