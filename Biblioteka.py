#import the minecraft.py module from the minecraft directory
import mcpi.minecraft as minecraft
#import minecraft block module
import mcpi.block as block
#import time, so delays can be used
import time
#import random module to create random number
import random
#import math module to use square root function
import math

class MineCraftGame:
    def __init__(self):
        self.gra = minecraft.Minecraft.create()

    def wypisz_na_ekran(self, tekst):
        self.gra.postToChat(tekst)

    def pobierz_pozycje_gracza(self):
        return self.gra.player.getPos()

    def __roundVec3(self, vec3):
        return minecraft.Vec3(int(vec3.x), int(vec3.y), int(vec3.z))

    def losuj_blok_nie_dalej_niz(self, pozycja_gracza, odleglosc):
        losowa_pozycja = self.__roundVec3(pozycja_gracza)
        losowa_pozycja.x = random.randrange(losowa_pozycja.x - odleglosc, losowa_pozycja.x + odleglosc)
        losowa_pozycja.y = random.randrange(losowa_pozycja.y - 5, losowa_pozycja.y + 5)
        losowa_pozycja.z = random.randrange(losowa_pozycja.z - odleglosc, losowa_pozycja.z + odleglosc)
        return losowa_pozycja

    def umiesc_blok_na_mapie(self, pozycja):
        self.gra.setBlock(pozycja.x, pozycja.y, pozycja.z, block.DIAMOND_BLOCK)

    
    def licz_odleglosc_miedzy_punktami(self, pozycja_gracza, pozycja_bloku):
        xd = pozycja_gracza.x - pozycja_bloku.x
        yd = pozycja_gracza.y - pozycja_bloku.y
        zd = pozycja_gracza.z - pozycja_bloku.z
        return int(math.sqrt((xd*xd) + (yd*yd) + (zd*zd)))

    def poczekaj(self, czas):
        time.sleep(czas)
        
        


