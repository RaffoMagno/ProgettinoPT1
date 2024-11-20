
def aggiungiElemento(listaSpesa):
    num = None
    while num == None:
        try:
            num = int(input("Quanti elementi vuoi aggiungere? "))
        except:
            print("Inserisci un numero")
    
    for i in range(num):
        elemento = input("Inserisci elemento da aggiungere alla lista: ")
        listaSpesa.append(elemento)
        print("Elemento aggiunto")

def visualizzaLista(listaSpesa):
    for ingrediente in listaSpesa:
        print(f'{listaSpesa.index(ingrediente)} - {ingrediente}')

def rimuoviElemento(listaSpesa):
    visualizzaLista(listaSpesa)
    indice = None
    while indice == None:
        try:
            indice = int(input("Inserisci indice elemento da rimuovere: "))
        except:
            print('Inserisci valore numerico')
    listaSpesa.pop(indice)
    visualizzaLista(listaSpesa)

def contaElementi(listaSpesa):
    print(f'Ci sono {len(listaSpesa)} elementi nella lista')

listaSpesa = []

scelta = None
while scelta != 5:
    print("\n1 - Aggiungi elemento")
    print("2 - Visualizza lista")
    print("3 - Rimuovi elemento")
    print("4 - Conta elementi")
    print("5 - Termina programmaa")
    try:
        scelta = int(input("La tua scelta: "))
    except:
        print("Inserisci valore numerico")

    if scelta == 1:
        aggiungiElemento(listaSpesa)
    elif scelta == 2:
        visualizzaLista(listaSpesa)
    elif scelta == 3:  
        rimuoviElemento(listaSpesa)
    elif scelta == 4:  
        contaElementi(listaSpesa)