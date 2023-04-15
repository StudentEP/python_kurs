from produkt import Produkt
from koszyk import Koszyk

def main():
    Produkt.wczytaj_produkty("ceny.csv")
    #print(Produkt.produkt("Odbiornik telewizyjny 32 cale").cena(1,2010))
    koszyk = Koszyk()
    koszyk.dodaj(Produkt.produkt("Cebula - za 1 kg"))
    koszyk.dodaj(Produkt.produkt("Cebula - za 1 kg"))

    print(koszyk.wartosc(3,2023))


if __name__ == "__main__":
    main()
