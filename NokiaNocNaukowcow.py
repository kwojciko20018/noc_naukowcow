from Biblioteka import MineCraftGame

if __name__ == "__main__":
    gra = MineCraftGame()
    gra.wypisz_na_ekran("WITAM W GRZE")
    pozycja_gracza = gra.pobierz_pozycje_gracza()
    pozycja_bloku = gra.losuj_blok_nie_dalej_niz(pozycja_gracza, 50)
    gra.umiesc_blok_na_mapie(pozycja_bloku)

    gra.wypisz_na_ekran("Zaczynamy! znajdz diament")

    wciaz_szukam = True
    
    while (wciaz_szukam == True):
        pozycja_gracza = gra.pobierz_pozycje_gracza()
        odleglosc_gracza_od_celu = gra.licz_odleglosc_miedzy_punktami(pozycja_gracza, pozycja_bloku)
        gra.wypisz_na_ekran("Do celu zostalo " + str(odleglosc_gracza_od_celu))
        if(odleglosc_gracza_od_celu < 2):
            gra.wypisz_na_ekran("Gratuluje ! znalazles skarb")
            wciaz_szukam = False
        gra.poczekaj(1)

    gra.wypisz_na_ekran("Koniec gry")
        
