


class Rectangle: # la class rectangle

    def __init__(self):# les parametres de ractangle
     
     self.L=4
     self.l=5
     self.nom="rectangle"


    def afficher (self) :# fonction d'affichage
     print('la langeur est :',self.L)
     print('la largeur est :',self.l)
     print('le nom est :',self.nom)
    def surface (self) :# methode calculer la surface
     self.sur=self.L * self.L
     print('la surface de rectangle est :',self.sur)
class care(Rectangle): # class care
  
  
    def __init__(self):
     
     self.L=5
     self.l=5
     self.nom="care"
    def surface (self) :
      self.sur=self.L * self.L
      print('la surface de care est :',self.sur)

s=Rectangle()# rappelle des class et ses methodes
s.afficher()
s.surface()
n=care()
n.afficher()
n.surface()