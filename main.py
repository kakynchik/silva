class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def make_sound(self):
        print(f"{self.name} zvy4it: {self.sound}")
animal1 = Animal("cow", "moo")
animal1.make_sound()
animal2 = Animal("fish", "bulk")
animal2.make_sound()