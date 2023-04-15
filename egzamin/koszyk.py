class Koszyk:
    def __init__(self):
        self.__produkty = {}

    def dodaj(self, produkt):
        if produkt.get_nazwa() in self.__produkty.keys():
            self.__produkty[produkt.get_nazwa()] = produkt,self.__produkty[produkt.get_nazwa()][1]+1
        else:
            self.__produkty[produkt.get_nazwa()] = produkt, 1


      def wartosc(self, miesiac, rok):
    if Produkt.waliduj_date(miesiac, rok):
        suma = 0
        for produkt in self.__produkty.values():
            suma += produkt[0].cena(miesiac, rok) * produkt[1]
        return suma


    return None

    def roczna_stopa_inflacji(self, miesiac, rok):
        if Produkt.waliduj_date(miesiac, rok) and rok > 2010:
            cena_teraz = self.wartosc(miesiac, rok)
            cena_rok_temu = self.wartosc(miesiac, rok - 1)
            return (cena_teraz - cena_rok_temu) / cena_rok_temu * 100
        return None