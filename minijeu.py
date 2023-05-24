import random

def main():
    nombre_mystere = random.randint(1, 100)
    essais = 0
    
    print("=== Devinez le nombre mystère (entre 1 et 100)  ===")
    
    while True:
        nombre_joueur = int(input("Entrez un nombre : "))
        essais += 1
        
        if nombre_joueur < nombre_mystere:
            print("C'est plus !")
        elif nombre_joueur > nombre_mystere:
            print("C'est moins !")
        else:
            print(f"Bravo, vous avez trouvé le nombre mystère en {essais} essais !")
            break

if __name__ == "__main__":
    main()
