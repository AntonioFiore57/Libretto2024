class Voto:
    def __init__(self, esame, cfu, punteggio, lode, data):
        self.esame = esame
        self.cfu = cfu
        self.__punteggio = punteggio # fuori dalla classe: _Voto__punteggio
        self.lode = lode
        self.data = data

        if self.lode and self.punteggio!=30:
            raise ValueError("Lode non applicabile")
    @property
    def punteggio(self):
        return self.__punteggio

    @punteggio.setter
    def punteggio(self, punteggio):
        self.__punteggio = punteggio


    def __str__(self):
        return f"Esame {self.esame} superato con {self.punteggio}"

    def __repr__(self):
        return f"Voto('{self.esame}', {self.cfu}, {self.punteggio}, {self.lode}, '{self.data}')"


v1 = Voto("Analisi I", 10, 25, False, '2022-03-03')

print(v1.punteggio)
print(v1._Voto__punteggio)
