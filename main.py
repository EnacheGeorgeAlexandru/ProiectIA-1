import queue

# stare_initiala = [[1, 2, 3],
#                   [8, 6, 4],
#                   [7, 5, 0]]

stare_initiala = [[2, 0, 3],
                  [1, 8, 4],
                  [7, 6, 5]]

class Nod:
    def __init__(self, stare_init):
        self.stare = stare_init
        self.vecini = []
        # initializez stare -> o lista de liste reprezentand configuratia tablei
        # declar lista de vecini(noduri), goala. vecinii vor fi adaugati doar atunci cand nodul este expandat
    
    def construiesteVecini(self):
        directii = ["sus", "jos", "stanga", "dreapta"]
        for directie in directii:
            vecin = self.succesor(directie)
            if vecin.stare != self.stare:
                self.vecini.append(vecin)
        #adaug veinii in lista atunci cand nodul este expandat (doar daca este diferit de cel curent pentru ca
        #primesc 4 noduri (daca 0 era in colt doar 2 sunt diferite de cel initial, daca era la margine 3 st diferite, daca
        #era in mijloc avem 4)

    def esteScop(self):
        return self.stare == [[1, 2, 3],
                              [8, 0, 4],
                              [7, 6, 5]]

    def printStare(self):
        for line in self.stare:
            print(line)

    def succesor(self, directie):
        cpy_stare = []
        for line in self.stare:
            lin = []
            for i in line:
                lin.append(i)
            cpy_stare.append(lin)

        l, c = -1, -1
        for i in range(3):
            for j in range(3):
                if cpy_stare[i][j] == 0:
                    l, c = i, j
                    break
        # gasesc pozitia lui 0 (patratul gol de pe tabla)

        if directie == "sus" and l > 0:
            cpy_stare[l][c], cpy_stare[l - 1][c] = cpy_stare[l - 1][c], 0
        elif directie == "jos" and l < 2:
            cpy_stare[l][c], cpy_stare[l + 1][c] = cpy_stare[l + 1][c], 0
        elif directie == "stanga" and c > 0:
            cpy_stare[l][c], cpy_stare[l][c - 1] = cpy_stare[l][c - 1], 0
        elif directie == "dreapta" and c < 2:
            cpy_stare[l][c], cpy_stare[l][c + 1] = cpy_stare[l][c + 1], 0
        #interschimb 0 cu sus/jos/stanga/dreapta

        return Nod(cpy_stare)
        # returnez un nod construit cu starea construita aici
    def euristica(self):
        gresit = 0
        scop =  [[1, 2, 3],
                 [8, 0, 4],
                 [7, 6, 5]]
        for i in range (3):
            for j in range (3):
                if self.stare[i][j] != scop[i][j]:
                    gresit += 1
        #cate numere sunt pe pozitii gresite pe tabla
        return gresit

def cautare(str):
    nod_init = Nod(stare_initiala)

    def bfs(nod_init):
        frontiera = queue.Queue()
        #coada pentru parcurgerea in latime
        explorat = []
        frontiera.put(nod_init)
        cost = 0

        while frontiera.empty() == 0:
            cost += 1
            #nu exista costuri suplimentare, se va considera ca fiecare verificare a unui nod are cost 1
            nod = frontiera.get()
            nod.construiesteVecini()
            #construiesc vecinii aici si mai jos ii adaug in coada daca nodul curent nu este scop
            explorat.append(nod.stare)
            print("nodul curent:")
            nod.printStare()
            if nod.esteScop():
                print("gasit")
                break
            #iau un nod din coada, verific daca e scop, daca nu este mai departe vecinii lui sunt adaugati in coada
            #daca nu au fost deja explorati
            for vecin in nod.vecini:
                if vecin.stare not in explorat:
                    frontiera.put(vecin)
        print("costul: ", cost)

    def greedy(nod_init):
        cost = 0
        lista_noduri = []
        lista_noduri.append(nod_init)

        while lista_noduri:
            cost += 1
            min = 10
            #functia euristica returneaza un intreg mai mic strict ca 10
            for n in lista_noduri:
                if n.euristica() < min:
                    nod = n
                    min = n.euristica()
            #gasesc nodul a carui functie euristica returneaza valoarea cea mai mica

            print("nodul curent:")
            nod.printStare()
            nod.construiesteVecini()
            if nod.esteScop():
                print("gasit")
                break

            for vecin in nod.vecini:
                lista_noduri.append(vecin)
            lista_noduri.remove(nod)
            #daca nodul curent nu a fost scop, il elimin, adaug vecinii si mergem mai departe la nodul cu valoarea minima a f euristice
        print("costul: ", cost)

    if str == "bfs":
        bfs(nod_init)

    if str == "greedy":
        greedy(nod_init)


cautare("bfs")
cautare("greedy")

#pe exemplul cu care este initializata aici starea initiala(exemplul din curs) putem observa cum cautarea
# neinformata verifica 17 noduri, iar cautarea informata, chiar si cu o functie euristica
# simpla, verifica doar 5 noduri.






