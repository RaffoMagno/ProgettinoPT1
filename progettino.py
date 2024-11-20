
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

listaSpesa = []
aggiungiElemento(listaSpesa)
visualizzaLista(listaSpesa)
rimuoviElemento(listaSpesa)