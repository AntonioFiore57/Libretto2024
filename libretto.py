"""
Scrivere un programma Python che permetta di gestire un libretto universitario.
Il programma dovrà definire una classe Voto, che rappresenta un singolo esame superato,
ed una classe Libretto, che contiene l'elenco dei voti di uno studente.
"""
from random import randint

lst_esami= ['Analisi I', 'Analisi II', 'Fisica I',
           'Fisica II', 'Chimica', 'Meccanica razionale', 'Informatica I'
            , 'Cucina creativa', 'Salsa baciacata', 'Astronomia', 'Letteratura classica']

class Voto:
    def __init__(self, esame, cfu, punteggio, lode, data):
        self.esame = esame
        self.cfu = cfu
        self.__punteggio = 0
        self.lode = lode
        self.data = data

        self.punteggio = punteggio
        if self.lode and self.__punteggio!=30:
            raise ValueError("Lode non applicabile")
    @property
    def punteggio(self):
        return self.__punteggio

    @punteggio.setter
    def punteggio(self, punteggio):
        if punteggio >= 18 and punteggio <= 30:
            self.__punteggio = punteggio
        else:
            raise ValueError("Punteggio esame errato (punteggio compreso tra 18 e 30 )")

    def __str__(self):
        return f"Esame {self.esame} superato con {self.punteggio}"

    def __repr__(self):
        return f"Voto('{self.esame}', {self.cfu}, {self.punteggio}, {self.lode}, '{self.data}')"



class Libretto:
    def __init__(self):
        self.voti = []

    def append(self, voto):
        """
        La funzione controlla se è presente un esame con lo stesso nome
        dell'oggetto voto passato come parametro. In questo caso non lo inserisce
        :param voto: oggetto voto
        :return: True se l'esame è stato inserito
        """
        # non si possono inserire due esami con lo stesso nome
        presente = False
        for vv in self.voti:
            if vv.esame == voto.esame:
                presente = True
                break
        if not presente:
            self.voti.append(voto)
        return not presente

    def media(self):
        if len(self.voti)==0:
            raise ValueError("Elenco voti vuoto")
        punteggi = [v.punteggio for v in self.voti]
        return sum(punteggi)/len(punteggi)

lib = Libretto()

# inserire nel `Libretto` un elenco di 10 oggetti `Voto` a piacere
for i in range(10):
    n = randint(0, len(lst_esami)-1 )
    nomeEsame = lst_esami[n]
    crediti = randint(5, 15)
    punteggio = randint(18, 30)
    lode = True if punteggio == 30 and crediti%2==0 else  False
    data = f"{randint(2000, 2023)}-{randint(1, 12)}-{randint(1, 28)}"

    voto = Voto(nomeEsame, crediti, punteggio, lode, data)

    lib.append(voto)

for vv in lib.voti:
    print(vv)

