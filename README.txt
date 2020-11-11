***UTILISATION***

Appeler la fonction parophone(mot,nb_mots)
Le mot doit être écrit en phonétique,
Utiliser le tableau des code phonétiques pour correctemement l'orthographier.
Il faut utiliser la première colonne du 'tableau code phonetique.png' (code lexique)

ex : 

>>> parophone('e-le-f@',20)
éléphants                     score :  0.87
éléphant                      score :  0.87
élégants                      score :  0.82
élégants                      score :  0.82
élégant                       score :  0.82
élégant                       score :  0.82
échauffant                    score :  0.77
élisant                       score :  0.76
élaguait                      score :  0.76
élaguais                      score :  0.76
étouffants                    score :  0.76
étouffant                     score :  0.76
étouffant                     score :  0.76
éléphantes                    score :  0.76
éléphante                     score :  0.76
étoffait                      score :  0.75
étoffaient                    score :  0.75
éléments                      score :  0.75
élément                       score :  0.75
échauffa                      score :  0.75
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
Remarque : le mot doit être décomposé en syllabes séparées par un '-'
