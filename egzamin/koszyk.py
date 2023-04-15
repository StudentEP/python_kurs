class Koszyk:
    def __init__(self):
        self.__produkty = {}

    def dodaj(self, produkt):
        if produkt.get_nazwa() in self.__produkty.keys():
            self.__produkty[produkt.get_nazwa()] = produkt,self.__produkty[produkt.get_nazwa()][1]+1
        else:
            self.__produkty[produkt.get_nazwa()] = produkt, 1


   def wartość(self, miesiac, rok):
       if Produkt.waliduj_date(miesiac, rok):
           suma=0
           for produkt in self.__produkty:
               produkt[0].cena(miesiac, rok)*produkt[1]
           return suma

       return None

