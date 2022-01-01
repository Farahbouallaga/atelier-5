


class Vecteur2D:
    

  def __init__(self): # le constructeur
     self.v11=9
     self.v12=5
     self.v21=9
     self.v22=7
    

 
  def afficher (self):# la fonction d'affichage
      
    print('les deux parametres de vecteurs sont: ')
    print('les parametre de premiere vecteur est : (',self.v11,',',self.v12,')')    
    print('les parametre de premiere vecteur est : (',self.v21,',',self.v22,')')    

  def somme (self): # la method de la somme de deux vecteurs

   print('la somme de ces deux vecteurs est: ')
   self.somme1=self.v11+self.v21
   self.somme2=self.v12+self.v22
   print('(',self.somme1,',', self.somme2,')')





v=Vecteur2D() 

v.afficher()
v.somme()

    