#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-

import csv
f = open("assets/distance_sons.csv", encoding="iso-8859-1")
distance_sons = f.readlines()

auto_exe = True

def similarite_son(a,b):
    'renvoie un score de similarité entre 2 sons'
    index_a = distance_sons[0].strip().split(';').index(a)
    index_b = distance_sons[0].strip().split(';').index(b)

    if index_a < index_b:
        index_a,index_b = index_b, index_a

    return(float(distance_sons[index_a].split(';')[index_b])/10)

def similarite_syllabe(a,b):
    'renvoie un score de similarité entre 2 syllabes'
    score = 0
    longeur_min = min(len(a),len(b))
    longeur_max = max(len(a),len(b))
    for i in range(longeur_min):
        score += similarite_son(a[i],b[i])
    return (score/longeur_max)

def similarite_mot(a,b):
    'renvoie un score de similarité entre 2 mots décomposés en syllabes'        
    les_syllabes_a = a.split('-')
    les_syllabes_b = b.split('-')
    longeur_min = min(len(les_syllabes_a),len(les_syllabes_b))
    longeur_max = max(len(les_syllabes_a),len(les_syllabes_b))
    score = 0
    for syllabe in range(longeur_min):
        if (syllabe == 0 or syllabe == (longeur_min-1)):
            
            score += similarite_syllabe(les_syllabes_a[syllabe],les_syllabes_b[syllabe])
        else:
            ntm = similarite_syllabe(les_syllabes_a[syllabe],les_syllabes_b[syllabe])
            if ntm == 1:
                score += 1
            else :
                score += 0.6*ntm
    return (score/longeur_max)

def parophone(mot,nb_mots):
    'Renvoie *nb_mots* de parophones de *mot*. *mot* doit être ecrit en fo-ne-tik'
    parophones_trouves = []
    tsv_file = open("assets/Lexique383.tsv",encoding="utf_8")
    dictionnaire = csv.reader(tsv_file, delimiter="\t")
    
    for row in dictionnaire:
        score = similarite_mot(mot,str(row[22]))
        if score > 0.5:
            parophones_trouves.append([score,(str(row[0])), str(row[22]) ])    
    tsv_file.close()
    parophones_trouves.sort(reverse=True)
    parophones_retenus = parophones_trouves[0:nb_mots]

    for mot in parophones_retenus:
        print (mot[1] + (25 - len(mot[1]))*' ' + mot[2] + (20 - len(mot[2]))*' ' + 'score :  ' + str(round(mot[0],2)))

while auto_exe:
	mot_parophone = input('mot : ')
	parophone(str(mot_parophone),30)
