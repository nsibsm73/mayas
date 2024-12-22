# Sujet 24-NSIJ1ME3 - Exercice 3 : Les Mayas - Numération, Piles, POO 

import tkinter as tk

import PIL.Image
import PIL.ImageTk
import os


class Enonce:
    def __init__(self, fenetre):
        self.ratio=1
        fenetre.title("24-NSIJ1ME3 - Exercice 3 - Les Mayas")
        fenetre.geometry("800x1200+400+5")
        self.text_frame=tk.Frame(fenetre, width = 800, height=1000, padx=15, pady=15)
        self.text_frame.place(x=5,y=5)
        self.text = tk.Text(self.text_frame , height=40,width=80, font=("Liberation Serif", round(12/self.ratio)))
        self.text.place(x=10, y=10)
        self.scrollbar = tk.Scrollbar(self.text_frame, orient="vertical", command=self.text.yview)
        # Lier la barre de défilement au widget Text
        self.text.config(yscrollcommand=self.scrollbar.set)

        fenetre.after(1000, self.config_scrollbar)



        self.imagesInit()
        self.zoneTexteInit()
        self.zoneTexte()


        fenetre.mainloop()  

    def config_scrollbar(self):
        # Obtenir les dimensions du widget Text
        text_width = self.text.winfo_width()
        text_height = self.text.winfo_height()
        
        # Placer la barre de défilement à droite du widget Text
        self.scrollbar.place(x=text_width + 10, y=10, height=text_height)
    def imagesInit(self):
        # Initialisation des dessins
      
        script_dir = os.path.dirname(os.path.abspath(__file__))+"\images"
        print("Repertoire : ", script_dir)
        dessin=["les20Symboles","coquille","point", "trait", "Maya_407", "Maya_3435", "classMaya","MethodeMayaToDec", "fonctionMystere"]
        self.photo={}
        for elt in dessin:
            image_path = os.path.join(script_dir, elt+".png")
            image = PIL.Image.open(image_path)
            
            image=image.resize((round(image.width/self.ratio), round(image.height/self.ratio)), PIL.Image.Resampling.LANCZOS)

            self.photo[elt]=PIL.ImageTk.PhotoImage(image)
# ---------------------------





    def zoneTexteInit(self):
        # Création du widget Text et configuration
        self.text.config(tabs=())

        
        self.text.tag_configure("exposant", offset=5, font=("Liberation Serif", round(8/self.ratio)))
        self.text.tag_configure("indice", offset=-5, font=("Liberation Serif", round(8/self.ratio)))

        self.text.tag_configure("decale", lmargin1=round(30/self.ratio), lmargin2=round(30/self.ratio))  # Décalage interne
        self.text.tag_configure("centré", justify="center")  # Alignement centré
        self.text.tag_configure("gras", font=("Liberation Serif", round(12/self.ratio), "bold"))
        self.text.tag_configure("petit", font=("Liberation Serif", round(6/self.ratio)))



    # Contenu du widget Text
    def zoneTexte(self):

        print("************************************************")
        self.text.insert(tk.END,"\n                        24-NSIJ1ME3 - Exercice 3 - Les Mayas", "gras" )
        
        txt = """

        \nCet exercice porte sur les bases de numération, la structure de données PILE et la POO.

    La civilisation Maya est une ancienne civilisation de Mésoamérique principalement connue 
    pour ses avancées dans les domaines de l'écriture, de l'art, de l'architecture, de l'agriculture, 
    des mathématiques et de l'astronomie. 
    La numération Maya est une numération positionnelle de base 20 (dite vigésimale)
    utilisant trois symboles pour former les "chiffres" :

        \u2022 une coquille pour le zéro """


        self.text.insert(tk.END, txt)
        self.text.image_create(tk.END, image = self.photo["coquille"])

        txt ="\n    \u2022 un point pour l'unité "
        self.text.insert(tk.END, txt)
        self.text.image_create(tk.END, image=self.photo["point"])
        
        self.text.insert(tk.END, "\n    \u2022 un trait pour la valeur 5 ")
        self.text.image_create(tk.END, image=self.photo["trait"])
        self.text.insert(tk.END,"\n\nLes chiffres sont les suivants. Ils utilisent une numération aditive :\n\n                     ")

        self.text.image_create(tk.END, image=self.photo["les20Symboles"])

        self.text.insert(tk.END, 
        """\nDans une version simplifiée de ce système, l'écriture d'un nombre se fait par 
    empilement de "chiffres". Chaque étage correspond à un chiffre de poids 20 fois 
    supérieur au poids du chiffre de l'étage inférieur. 

    Ainsi la valeur du chiffre de l'étage le plus bas est multipliée par 20""")
        self.text.insert(tk.END, "0", "exposant")
        self.text.insert(tk.END, """ soit 1, du second 
        étage par 20""")
        self.text.insert(tk.END, 1, "exposant")
        self.text.insert(tk.END, " , du troisième étage par 20")
        self.text.insert(tk.END, "2", "exposant")
        self.text.insert(tk.END, " , et ainsi de suite. ")

        self.text.insert(tk.END, """\n\nExemple : la représentation Maya de l'entier 407 est la suivante.
        \n                                          """)
        self.text.image_create(tk.END, image=self.photo["Maya_407"])
        self.text.insert(tk.END, "\n\n1.  Compléter le tableau donné en ")
        self.text.insert(tk.END, "annexe à rendre avec la copie", "gras")
        self.text.insert(tk.END,""".\n\n2.  Justifier que l'écriture Maya de l'entier 3435 est : 
        \n                                          """)
        self.text.image_create(tk.END,image=self.photo["Maya_3435"])
        self.text.insert(tk.END,"\n\n On ")
        self.text.insert(tk.END,"modélise l'écriture d'un entier","gras")
        self.text.insert(tk.END, """ dans sa représentation Maya par une pile formée
    de listes. Chacune de ces listes est composée de trois entiers et modélise le "chiffre"
    d'un étage :\n
            \u2022  le premier entier vaut 0 ou 1 suivant s'il y a ou non une coquille ;
            \u2022  le deuxième représente le nombre de points ;
            \u2022  le troisième représente le nombre de traits.\n
    Ainsi, la modélisation Maya de l'entier 3435 est [[0, 0, 3], [0, 1, 2], [0, 3, 1]]
    et celle de l'entier 407 est [[0, 2, 1], [1, 0, 0], [0, 1, 0]]. \n
    Le sommet de la pile se situe en fin de liste.\n
    On dispose de la classe suivante :\n\n     """ )
        self.text.image_create(tk.END, image=self.photo["classMaya"])
        self.text.insert(tk.END, """\n
    3.  \u00C9crire une suite d'instructions permettant de créer une instance, nommée M, de
        la classe Maya qui modélise le nombre entier 3435.\n
    4.  \u00C9crire la méthode nbEtages de la classe Maya. Celle-ci renvoie le nombre de
        "chiffres" utilisés pour écrire le nombre correspondant en écriture Maya.\n\n""")
        self.text.insert(tk.END, "\nDe l'écriture Maya à l'écriture décimale", "gras")
        self.text.insert(tk.END, """"\n
    5.   \u00C9crire une fonction valeurChiffre ayant pour paramètre une liste L. Celle-ci
    renvoie la valeur de l'entier associé à la liste L = [c, p, t] où c (valeur 0 ou 1)
    indique la présence d'une coquille, p est le nombre de points et t, le nombre de traits
    composant une "chiffre" Maya.\n
    Exemple : 
                        
        >>> valeurChiffre([0,2,3])
        >>> 17
        >>> valeurChiffre([1, 0, 0])
        >>> 0

    6.  Recopier et compléter les lignes 2, 4, 5 et 7 de la méthode MayaToDec suivante
        de la classe Maya. Cette méthode renvoie la valeur de l'entier associé à l'objet
        Maya. On pourra utiliser les méthodes estVide, nbEtages et retirer. 
    \n\n""")
        self.text.image_create(tk.END, image=self.photo["MethodeMayaToDec"])
        self.text.insert(tk.END,"\n\n\nDe l'écriture décimale vers sa modélisation Maya", "gras")
        self.text.insert(tk.END, """\n
    On considère que la fonction DecToVige est déjà écrite. Celle-ci prend en paramètre
    un entier n et renvoie la décomposition en base 20 de celui-ci sous la forme d'une liste
    [a""")
        self.text.insert(tk.END,"0", "indice")
        self.text.insert(tk.END, ", a")
        self.text.insert(tk.END,"1", "indice")
        self.text.insert(tk.END, ", ..., a")
        self.text.insert(tk.END,"p", "indice")
        self.text.insert(tk.END, " ] telle que : ")
        self.text.insert(tk.END, "\n                        n = a")
        self.text.insert(tk.END,"0", "indice")
        self.text.insert(tk.END, " x 20")
        self.text.insert(tk.END,"0", "exposant")
        self.text.insert(tk.END, " + a")
        self.text.insert(tk.END,"1", "indice")
        self.text.insert(tk.END, " x 20")
        self.text.insert(tk.END,"1", "exposant")
        self.text.insert(tk.END, " + a") 
        self.text.insert(tk.END,"2", "indice")
        self.text.insert(tk.END, " x 20")
        self.text.insert(tk.END,"2", "exposant")
        self.text.insert(tk.END, "+ ... + a")
        self.text.insert(tk.END,"p", "indice")
        self.text.insert(tk.END, " x 20")
        self.text.insert(tk.END,"p", "exposant")
        self.text.insert(tk.END, """Exemple : 
                        
        >>> DecToVige(3435)
        >>> [15, 11, 8]
        >>> DecToVige(407)
        >>> [7, 0, 1]\n
    7.  \u00C9crire la fonction decompChiffre qui prend en paramètre un entier n compris
        entre 0 et 19 et renvoie la liste [c, p, t] où c vaut 0 ou 1 et indique la présence
        ou non d'une coquille, p est le nombre de points et t le nombre de traits
        composant le "chiffre" Maya correspondant. 

    Exemple :
        >>> decompChiffre(17)
        >>> [0, 2, 3]
        >>> decompChiffre(0)
        >>> [1, 0, 0]\n
    8.  \u00C9crire la fonction DecToMaya qui prend en paramètre un entier n et renvoie la
        modélisation Maya d'un objet M de la classe Maya correspondant. 
                        
    Exemple : 
        >>> DecToMaya(3435).nombre
        [[0, 0, 3], [0, 1, 2], [0, 3, 1]]
        >>> DecToMaya(407).nombre
        [[0, 2, 1], [1, 0, 0], [0, 1, 0]]\n\n""")
        self.text.insert(tk. END, "Opérations sur les nombres en modélisation Maya", "gras")
        self.text.insert(tk. END, """\n
    On souhaite additionner des nombres directement à partir de leur modélisation Maya. \n
    9.  \u00C9crire la méthode multiple de la classe Maya qui renvoie le résultat de la 
        multiplication par 20 d'un nombre en modélisation Maya. 
                        
    Exemple : 

        >>> M = Maya()
        >>> M.ajouter([0, 0, 3])
        >>> M.ajouter([0, 1, 2])
        >>> M.multiplie().nombre
        [[1, 0, 0], [0, 0, 3], [0, 1, 2]]
                        
    On donne la fonction mystere suivante : \n\n """)
        self.text.image_create(tk.END, image=self.photo["fonctionMystere"])
        self.text.insert(tk.END, """\n\n
    10. Donner les résultats renvoyés par les deux appels suivants : 
                        
    \u2022  mystere([0, 1, 1], [0, 3, 1], 0)
                        
    \u2022  mystere([0, 1, 1], [0, 4, 2], 0)
                        
    11. \u00C9crire une méthode somme de la classe Maya permettant d'ajouter à l'instance
        courante un autre nombre maya2 de même taille en modélisation Maya. """)






        # Ligne à laisser à la fin! C'est pour faire une marge à gauche
        self.text.tag_add("decale", "1.0", "end")
        # --------------------------------------------------------------

# Fenêtre de l'énoncé
if __name__=="__main__" :
    fenetre = tk.Tk()
    page1 = Enonce(fenetre)




