from produkt import Produkt

def main():
    Produkt.wczytaj_produkty("ceny.csv")
    print(Produkt.produkt("Odbiornik telewizyjny 32 cale").cena(1,2010))

if __name__ == "__main__":
    main()
