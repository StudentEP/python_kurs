class Koszyk:
    def __init__(self):
        self.__produkty = {}

    def dodaj(self, produkt):
        if produkt.get_nazwa() in self.__produkty.keys():
            self.__produkty[produkt.get_nazwa()] = produkt,self.__produkty[produkt.get_nazwa()][1]+1
        else:
            self.__produkty[produkt.get_nazwa()] = produkt, 1