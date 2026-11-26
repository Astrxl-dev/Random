# 🎲 Devine le nombre

Un petit jeu en Python qui se joue dans le terminal : l'ordinateur choisit un nombre au hasard entre **-1000 et 1000**, et tu dois le deviner.

## Fonctionnalités

- Nombre entier aléatoire entre -1000 et 1000 (bornes incluses)
- Indication après chaque erreur : trop petit ou trop élevé
- Nombre d'essais illimité

## Prérequis

- [Python 3](https://www.python.org/downloads/)

Aucune bibliothèque externe n'est nécessaire : le script utilise uniquement le module standard `random`.

## Installation

Clone le dépôt, ou télécharge directement le fichier `Random_.py` :

```bash
git clone https://github.com/<ton-pseudo>/<nom-du-depot>.git
cd <nom-du-depot>
```

## Utilisation

```bash
python Random_.py
```

Selon ton système, la commande peut être `python3 Random_.py`.

## Exemple de partie

Début d'une partie (les messages dépendent du nombre tiré au sort) :

```text
Devine le nombre choisi par l'ordinateur : 0
Le nombre rentré n'est pas celui de l'ordinateur
Le nombre que tu as entré est trop petit. Celui de l'ordinateur est plus élevé
Devine le nombre choisi par l'ordinateur : 500
Le nombre que tu as entré est trop petit. Celui de l'ordinateur est plus élevé
Devine le nombre choisi par l'ordinateur : 
```

💡 **Astuce :** en proposant à chaque fois le milieu de l'intervalle restant (recherche dichotomique), tu trouves le nombre en 11 essais maximum.

## Limites connues

- Le message de victoire ne s'affiche que si le nombre est trouvé du premier coup. Sinon, le programme se termine sans message.
- Une saisie qui n'est pas un nombre entier (texte, nombre à virgule, saisie vide) provoque une erreur et arrête le programme.
- Après la première erreur, le message « Le nombre rentré n'est pas celui de l'ordinateur » apparaît deux fois.
