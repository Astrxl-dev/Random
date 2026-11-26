import random

nombre_ordinateur = random.randint(-1000,1000)

entrée_utilisateur = int(input("Devine le nombre choisi par l'ordinateur : "))

if entrée_utilisateur != nombre_ordinateur :
    print ("Le nombre rentré n'est pas celui de l'ordinateur")

else :
    print ("Bravo tu as deviné le nombre choisi par l'ordinateur")

while entrée_utilisateur != nombre_ordinateur :

    if entrée_utilisateur < nombre_ordinateur :
        print ("Le nombre que tu as entré est trop petit. Celui de l'ordinateur est plus élevé")
    else : 
        print ("Le nombre que tu as entré est trop élevé. Celui de l'ordinateur est plus petit")

    print ("Le nombre rentré n'est pas celui de l'ordinateur")
    entrée_utilisateur = int(input("Devine le nombre choisi par l'ordinateur : "))

