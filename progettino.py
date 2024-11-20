
def aggiungiElemento(listaSpesa):
    num = None
    while num == None:
        try:
            num = int(input("Quanti elementi vuoi aggiungere?"))
        except:
            print("Inserisci un numero")
    
    for i in range(num):
        elemento = input("Inserisci elemento da aggiungere alla lista")
        listaSpesa.append(elemento)
        print("Elemento aggiunto")

def visualizzaLista(listaSpesa):
    print(listaSpesa)

listaSpesa = []
aggiungiElemento(listaSpesa)
visualizzaLista(listaSpesa)