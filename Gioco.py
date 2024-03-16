import random
class Domanda:
    def __init__(self, domanda, livello, risposte):
        self.livello = livello
        self.domanda = domanda
        self.risposte = risposte

    """def __str__(self):
        stringa = "Livello " + str(self.livello) + ") " + self.domanda
        #i = 1
        copia_risposte = self.risposte
        random.shuffle(copia_risposte)
        for r in copia_risposte:
            stringa += str(copia_risposte.index(r) + 1) + ". " + r + "\n"
            #i = i+1
        return stringa"""


class Giocatore:
    def __init__(self, nickname, punteggio):
        self.nickname = nickname
        self.punteggio = punteggio

    def __str__(self):
        return self.nickname + " " + str(self.punteggio)

    def __lt__(self, other):
        if self.punteggio == other.punteggio:
            return self.nickname < other.nickname
        else:
            return self.punteggio > other.punteggio


livello_max = 0
lista_domande = []
f = open("domande.txt", "r")
riga = f.readline()
n_riga = 1
livello = 0
quesito = ""
opzioni = []
while riga != "":
    if n_riga == 1:
        char_da_escludere = '\n'
        riga_modif = ""
        for char in riga:
            if char!= char_da_escludere:
                riga_modif += char
        quesito = riga_modif
    elif n_riga == 2:
        livello = int(riga)
        if livello > livello_max:
            livello_max = livello
    elif 2 < n_riga < 6:
        char_da_escludere = '\n'
        riga_modif = ""
        for char in riga:
            if char != char_da_escludere:
                riga_modif += char
        opzioni.append(riga_modif)
    elif n_riga == 6:
        char_da_escludere = '\n'
        riga_modif = ""
        for char in riga:
            if char != char_da_escludere:
                riga_modif += char
        opzioni.append(riga_modif)
        domanda = Domanda(quesito, livello, opzioni)
        lista_domande.append(domanda)
        livello = 0
        quesito = ""
        opzioni = []
    elif n_riga == 7:
        n_riga = 0
    n_riga = n_riga+1
    riga = f.readline()
f.close()

#for d in lista_domande:
    #print(d.__str__())

liv_attuale = 0
corretta = True
punti = 0
while corretta is True and liv_attuale < livello_max+1:
    copia_domande = []
    copia_domande += lista_domande
    random.shuffle(copia_domande)
    for d in copia_domande:
        if d.livello == liv_attuale:
            print("Livello " + str(d.livello) + ") " + d.domanda)
            copia_risposte = []
            copia_risposte += d.risposte
            random.shuffle(copia_risposte)
            stringa = ""
            risposta_corretta = 0
            for r in copia_risposte:
                stringa += str(copia_risposte.index(r) + 1) + ". " + r + "\n"
                if r == d.risposte[0]:
                    risposta_corretta = int(copia_risposte.index(r)) + 1
            print(stringa)
            scelta = input("Inserisci la risposta: ")
            print(scelta + "\n")
            if int(scelta) == risposta_corretta:
                punti += 1
                print("Risposta corretta!\n")
                liv_attuale += 1
                break
            else:
                print("Risposta sbagliata! La risposta corretta era " + str(risposta_corretta) + "\n")
                corretta = False
                break
    continue

print("Hai totalizzato " + str(punti) + " punti!")
name = input("Inserisci il tuo nickname: ")

nuovo_giocatore = Giocatore(name, punti)
lista_giocatori = []
f1 = open("punti.txt", "r")
riga1 = f1.readline()
while riga1 != "":
    riga1_split = riga1.split(" ")
    nominativo = riga1_split[0]
    score = int(riga1_split[1])
    gamer = Giocatore(nominativo, score)
    lista_giocatori.append(gamer)
    riga1 = f1.readline()
f1.close()
lista_giocatori.append(nuovo_giocatore)
lista_giocatori.sort()

f2 = open("punti.txt", "w")
primo = False
for g in lista_giocatori:
    if primo is False:
        f2.write(g.__str__())
        primo = True
    else:
        f2.write("\n" + g.__str__())
f2.close()





