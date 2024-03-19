"""

"""
from random import randint
import  copy

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
        return f"Esame {self.esame} superato con {self.str_punteggio()}"

    def __repr__(self):
        return f"Voto('{self.esame}', {self.cfu}, {self.punteggio}, {self.lode}, '{self.data}')"

    def str_punteggio(self):
        """
        Costrusce la stringa in base al punteggio tenendo conto della lode
        :return: stringa rappresentativa del punteggio
        """
        return f"30 e lode" if self.punteggio == 30 and self.lode else f"{self.punteggio}"

    def copy(self):
        return Voto(self.esame, self.cfu, self.punteggio, self.lode, self.data)

class Libretto:
    def __init__(self):
        self.voti = []
    def clona(self):
        nuovo = Libretto()
        # nuovo.voti = copy.deepcopy(self.voti)
        for v in self.voti:
            nuovo.append( v.copy() )

        for v in nuovo.voti:
            if (18 <=v.punteggio<= 23) or v.punteggio == 29:
                v.punteggio += 1
            elif 24<=v.punteggio <=28:
                v.punteggio += 2

        return nuovo
    def append(self, voto):
        """
        La funzione controlla:
            se il voto è presente (has_voto) -> viene sollevata un'eccezione
            se vi sono conflitti (has_conflitto) -> viene sollevata un'eccezione

        :param voto: oggetto voto da inserire nella lista
        :return: None
        """

        if self.has_voto(voto):
            raise ValueError("Voto già presente")
        if self.has_conflitto(voto):
            raise  ValueError("Voto in conflitto")
        self.voti.append(voto)


        for vv in self.voti:
            if vv.esame == voto.esame:
                presente = True
                break
        if not presente:
            self.voti.append(voto)
        return not presente

    def findByPunteggio(self, punteggio, lode):
        """
        Ricerca degli esami che hanno il punteggio e l lode passati come parametri.
        Si controlla la compatibilità tra punteggio e lode; se esiste incompatibilità
        si restituisce una lista vuota
        :param punteggio: intero punteggio da cercare
        :param lode: booleano
        :return: lista degli oggetti Voto che soddisfano la richiesta (lista vuota in caso contrario)
        """


        if punteggio != 30 and lode:
            votiTrovati = []
        else:
            votiTrovati = [voto for voto in self.voti if voto.punteggio == punteggio and voto.lode == lode]
        return votiTrovati

    def has_voto(self, voto):
        """

        nomeEsame, punteggio, lode
        Ricerca nella lista voti se esiste un voto con nome esame, punteggio e lode
         uguali a quelli dell'oggetto passsato come parametro.
        Non si controlla la consistenza dell' punteggio.
        :param voto: oggetto Voto da cercare nella lista voti
        :return: True se si è trovata corrispondenza
        """

        trovato = False
        for v in self.voti:
            if v.esame == voto.esame and v.punteggio == voto.punteggio and v.lode == voto.lode:
                trovato = True
                break

        return trovato

    def has_conflitto(self, voto):
        """
        Ricerca nella lista voti se esiste un voto con nome esame uguale a quello
        del parametro ma con punteggio diverso
        Non si controlla la consistenza dell' punteggio.
        :param voto: oggetto Voto da confrontare  nella lista voti
        :return: True se esiste conflitto
        """

        conflitto = False
        for v in self.voti:
            if v.esame == voto.esame and (v.punteggio != voto.punteggio or v.lode != voto.lode):
                conflitto = True
                break

        return conflitto

    def findNomeEsame(self, nomeEsame):
        """
        Ricerca il nome dell'esame nella lista degli esami se viene trovato restituisce l'oggetto voto
        corrispondente. In caso contrario la funzione solleva un'eccezione
        :param nomeEsame: stringa nome esame da cercare
        :return: oggetto voto
        """
        trovato = False
        n = len(self.voti)
        for i in range(n-1):
            if self.voti[i].esame == nomeEsame:
                trovato = True
                break
        if not trovato:
            raise ValueError("Nome esame non trovato")

        return self.voti[i]

    def media(self):
        if len(self.voti)==0:
            raise ValueError("Elenco voti vuoto")
        punteggi = [v.punteggio for v in self.voti]
        return sum(punteggi)/len(punteggi)

lib = Libretto()

def domanda_1():
    # inserire nel `Libretto` un elenco di 10 oggetti `Voto` a piacere
    for i in range(10):

        nomeEsame = lst_esami[i]
        crediti = randint(5, 15)
        punteggio = randint(18, 30)
        lode = True if punteggio == 30 and crediti%2==0 else  False
        data = f"{randint(2000, 2023)}-{randint(1, 12)}-{randint(1, 28)}"

        voto = Voto(nomeEsame, crediti, punteggio, lode, data)

        lib.append(voto)

    for vv in lib.voti:
        print(vv)



def domanda_2():
    # stampare tutti i corsi in cui il punteggio è pari a 25
    # impostiamo alcuni esami al voto richiesto
    lib.voti[1].punteggio = 25
    lib.voti[3].punteggio = 25
    lib.voti[8].punteggio = 25
    for voto in lib.findByPunteggio(25, False):
        print(voto)

def domanda_3():
    # ricercare nel `Libretto` il punteggio di un esame, dato il nome del corso
    nomeEsame = 'Analisi 34'
    try:
        voto = lib.findNomeEsame(nomeEsame)
        print(voto)
    except:
        print(f"{nomeEsame} non trovato")

def domanda_4():
    """
    creare un nuovo oggetto `Voto`, e verificare se tale valutazione esiste già nel `Libretto` (stesso esame con stesso
   punteggio)
    """
    voto = Voto("Fisica Teorica",15, 30, True, '2022-03-18')
    #voto = lib.voti[8]

    if lib.has_voto(voto):
        print(f"{voto} è presente")
    else:
        print(f" {voto} non  è presente")

def domanda_5():
    # creare un nuovo oggetto Voto, e verificare se esiste
    # un conflitto con il Libretto (stesso esame e punteggio diverso)
    voto1 = Voto("Fisica Teorica", 15, 30, True, '2022-03-18')
    voto2 = Voto(lib.voti[8].esame, lib.voti[8].cfu, lib.voti[8].punteggio, lib.voti[8].lode, lib.voti[8].data)


    print(f"voto1: {lib.has_conflitto(voto1)}")
    print(f"voto2: {lib.has_conflitto(voto2)}")

    voto2.punteggio = 18
    print(f"voto2 modificato: {lib.has_conflitto(voto2)}")

def domanda_6():
    # modificare il metodo Libretto.append() in modo da evitare
    # di inserire valutazioni duplicate
    # (stesso esame con stesso punteggio) o in conflitto

    #voto1 = Voto("Fisica Teorica", 15, 30, True, '2022-03-18')
    voto1 = Voto(lib.voti[8].esame, lib.voti[8].cfu, lib.voti[8].punteggio, lib.voti[8].lode, lib.voti[8].data)
    voto1.punteggio = 18
    voto1.lode = False

    try:
        lib.append(voto1)
        print(f"\n{voto1}   Aggiunto")
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    domanda_1()
    print('\n-----------------------\n')

    lib2 = lib.clona()

    for v in lib2.voti:
        print(v)

    print("\n*** Fatto ***")