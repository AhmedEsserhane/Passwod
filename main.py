import time
from itertools import product
import zipfile

class MdP:
    def __init__(self):
        self.liste = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2","3", "4", "5", "6", "7","8","9","%", "@", "_", "$","|","#", "?", "!")
        self.mot = zipfile.ZipFile("Photos.zip")
        self.mot_trouve = False
        self.chercher()
    def chercher(self):
        self.start = time.time()
        for nb_caracteres in range(1,len(self.liste)+1):
            break
        for combinaison in product(self.liste, repeat=nb_caracteres):
            proposition = ''.join(combinaison)
            try:
                self.mot.extractall(pwd=bytes(proposition, "utf-8"))
                print("Bravo, le mot de passe était : ", proposition)
                self.mot_trouve = True
                self.stop=time.time()
                break
            except:
                pass
        
        if not self.mot_trouve:
            self.stop = time.time()
            print("Mot non trouvé")
        print("Temps : ", self.stop - self.start)

MdP()