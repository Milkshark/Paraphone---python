***UTILISATION***

Appeler la fonction parophone(mot,nb_mots)
Le mot doit être écrit en phonétique,
Utiliser le tableau des code phonétiques pour correctemement l'orthographier.
Il faut utiliser la première colonne du 'tableau code phonetique.png' (code lexique)

ex : 

>>> parophone('@-bi-si2', 39)
ambitieux                     score :  0.87
ambitieux                     score :  0.87
ambitieuse                    score :  0.78
ambitieuse                    score :  0.78
anti-chiens                   score :  0.78
...

ou encore

>>> parophone('Ro-Se', 39)
roché                         score :  1.0
rochet                        score :  1.0
rochers                       score :  1.0
rocher                        score :  1.0
rocher                        score :  1.0
rosés                         score :  0.97
rosés                         score :  0.97
rosées                        score :  0.97

Le deuxième chiffre est le nombre de mots à afficher
Remarque : le mot doit être décomposé en syllabes par un '-'
