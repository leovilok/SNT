#!/bin/python

from random import choice
import csv

def genquestions(eleve, data):
    qfile = open("out/Questions-" + eleve["nom"] + '-' + eleve["prenom"] + ".md", 'w')
    afile = open("out/Corrige-questions-" + eleve["nom"] + '-' + eleve["prenom"] + ".md", 'w')
    
    print("# Questions sur les données hospitalières\n", file=qfile)
    print("Pour {} {}.\n".format(eleve["prenom"], eleve["nom"]), file=qfile)
    
    print("# Corrigé des questions sur les données hospitalières\n", file=afile)
    print("Pour {} {}.\n".format(eleve["prenom"], eleve["nom"]), file=afile)
    
    # Question 1
    expl_descr1 = choice(descrs)

    print("## 1. D'après les métadonnées, à quoi correspond le descripteur '{}' ?\n".format(expl_descr1[0]), file=qfile)
    
    print("## 1. D'après les métadonnées, à quoi correspond le descripteur '{}' ?\n".format(expl_descr1[0]), file=afile)
    print("Le descripteur '{}' correspond au **{}**.\n".format(expl_descr1[0], expl_descr1[1]), file=afile)


    # Question 2
    expl_descr2 = choice(descrs)

    while expl_descr2 == expl_descr1:
        expl_descr2 = choice(descrs)
    print("## 2. D'après les métadonnées, quel descripteur représente le **{}** ?\n".format(expl_descr2[1]), file=qfile)
    
    print("## 2. D'après les métadonnées, quel descripteur représente le **{}** ?\n".format(expl_descr2[1]), file=afile)
    print("Le descripteur '{}' correspond au {}.\n".format(expl_descr2[0], expl_descr2[1]), file=afile)

    # Question 3
    dep = choice(deps)

    print("## 3. __Filtrez__ les départements pour ne garder que le {} ({}), quelle est la date du premier objet (première ligne) ?\n".format(dep[0], dep[1]), file=qfile)
    
    print("## 3. __Filtrez__ les départements pour ne garder que le {} ({}), quelle est la date du premier objet (première ligne) ?\n".format(dep[0], dep[1]), file=afile)
    print("La première date est le 2020-03-18 (23 mars 2020).\n", file=afile)

    # Question 4
    print("## 4. __Triez__ les dates par ordre décroissant pour avoir la plus récente (presque actuelle) en haut, "
          "combien d'hommes (sexe=1) et de femmes (sexe=2) sont actuellement hospitalisés ?\n", file=qfile)
          
    print("En {} il y a actuellement __ hommes et __ femmes hospitalisés.\n".format(dep[1]), file=qfile)

    print("## 4. __Triez__ les dates par ordre décroissant pour avoir la plus récente (presque actuelle) en haut, "
          "combien d'hommes (sexe=1) et de femmes (sexe=2) sont actuellement hospitalisés ?\n", file=afile)

    datadep = [line for line in data if line["dep"] == dep[0]]
    #datadep.sort(key=lambda line : line["jour"])

    datadep_h = [line for line in datadep if line["sexe"] == "1"]
    #datadep_h.sort(key=lambda line : line["jour"])
    datadep_f = [line for line in datadep if line["sexe"] == "2"]
    #datadep_f.sort(key=lambda line : line["jour"])
    print("En {} il y a actuellement {} hommes et {} femmes hospitalisés.\n".format(dep[1], datadep_h[-1]["hosp"], datadep_f[-1]["hosp"]), file=afile)
    
    
    # Question 5
    sexe = choice(sexes)
    print("## 5. __Filtrez__ pour ne garder que les {} (sexe={}) en conservant le filtre de département ({}), ".format(sexe[1], sexe[0], dep[0]),
          "**triez** par nombre de personnes hospitalisées ('hosp') décroissantes.\n", file=qfile)
    print("### 5.1 Quel jour y avait-t-il le plus de {} à l'hôpital en {} ?\n".format(sexe[1], dep[1]),
          file=qfile)       

    print("## 5. __Filtrez__ pour ne garder que les {} (sexe={}) en conservant le filtre de département ({}), ".format(sexe[1], sexe[0], dep[0]),
          "**triez** par nombre de personnes hospitalisées ('hosp') décroissantes.\n", file=afile)
    print("### 5.1 Quel jour y avait-t-il le plus de {} à l'hôpital en {} ?\n".format(sexe[1], dep[1]),
          file=afile)       

    dataq5 = [line for line in datadep if line["sexe"] == sexe[0]]
    dataq5.sort(key=lambda line: -int(line["hosp"]))

    print("Le pic de personnes à l'hôpital a été atteint le {}.\n".format(dataq5[0]["jour"]), file=afile)

    
    print("### 5.2 Quel était alors le nombre de {} hospitalisés en {} ?\n".format(sexe[1], dep[1]),
          file=qfile)

    print("### 5.2 Quel était alors le nombre de {} hospitalisés en {} ?\n".format(sexe[1], dep[1]),
          file=afile)
          
    print("Il y en avait {}.\n".format(dataq5[0]["hosp"]), file=afile)
    
    print("### 5.3 Est-ce que c'était pendant la première ou la 2ème vague du virus ?\n",
          file=qfile)
          
    print("### 5.3 Est-ce que c'était pendant la première ou la 2ème vague du virus ?\n",
          file=afile)
    print("C'était la 2ème vague.\n".format(dataq5[0]["hosp"]), file=afile)
    
    # Question 6
    print("## 6. Re-triez par jour décroissant et pour les 2 sexes (sexe=0), "
          "est-ce qu'il y a actuellement plus de personnes en réanimation en Charente (16) ou en {} ({}) ?\n".format(dep[1], dep[0]),
          file=qfile)
    
    print("## 6. Re-triez par jour décroissant et pour les 2 sexes (sexe=0), "
          "est-ce qu'il y a actuellement plus de personnes en réanimation en Charente (16) ou en {} ({}) ?\n".format(dep[1], dep[0]),
          file=afile)
    
    deprea = int(datadep[0]["rea"])
    data16 = [line for line in data if line["dep"] == "16" and line["sexe"] == "0"]
    charrea = int(data16[0]["rea"])
    
    if deprea == charrea:
        print("Il y a autant de personnes en réanimation en {} et en Charente : {} \n".format(dep[1], deprea), file=afile)
    elif deprea > charrea:
        print("Il y a plus de personnes en réanimation en {} qu'en Charente : {} > {} \n".format(dep[1], deprea, charrea), file=afile)
    else:
        print("Il y a moins de personnes en réanimation en {} qu'en Charente : {} < {} \n".format(dep[1], deprea, charrea), file=afile)



    

descrs = [
	("hosp","nombre de personnes hospitalisées"),
	("rea","nombre de personnes en réanimation ou soins intensifs"),
	("rad","nombre cumulé de personnes retournées à domicile"),
	("dc","nombre cumulé de personnes décédées à l'hôpital")
]

sexes = [
	("0", "personnes des 2 sexes"),
	("1", "hommes"),
	("2", "femmes")
]

deps = [
	#("16", "Charente"),
	("17", "Charente-Maritime"),
	("24", "Dordogne"),
	("33", "Gironde"),
	("79", "Deux-Sèvres"),
	("86", "Vienne"),
	("87", "Haute-Vienne")
]

def getdata():
    with open('donnees-hospitalieres-covid19-2020-12-06-19h03.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        data = [line for line in csv_reader]
        with open('eleves.csv', mode='r') as csv_eleves:
            csv_reader = csv.DictReader(csv_eleves, delimiter=',')
            eleves = [line for line in csv_reader]
            return data, eleves

data, eleves = getdata()

i=0
for eleve in eleves:
    print(i, "/", len(eleves))
    i+=1
    genquestions(eleve, data)

