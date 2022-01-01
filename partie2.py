

#from typing import List








class etudiant:
    def __init__(self):# constructeur de class etudiant 
       
        self.nom="farah"
        self.prenom="boallaga"
        self.age=12
        self.cne="H123"
        self.note=14
        self.nom1="salima"
        self.prenom1="boallaga"
        self.age1=20
        self.cne1="H124"
        self.note1=15
        list=[self.nom,self.prenom,self.age,self.cne,self.note,self.nom1,self.prenom1,self.age1,self.cne1,self.note1]
        print(list)
        print('ordrer la liste selon age')# order la liste selon l'age
        if(list[2]>list[7]):
            list=[self.nom,self.prenom,self.age,self.cne,self.note,self.nom1,self.prenom1,self.age1,self.cne1,self.note1]
            print(list)
        else:
            list=[self.nom1,self.prenom1,self.age1,self.cne1,self.note1,self.nom,self.prenom,self.age,self.cne,self.note]
            print(list)
            print('ordrer la liste selon moyenne')# ordrer la liste selon moyenne
        if(list[4]>list[9]):
            list=[self.nom,self.prenom,self.age,self.cne,self.note,self.nom1,self.prenom1,self.age1,self.cne1,self.note1]
            print(list)
        else:
            list=[self.nom1,self.prenom1,self.age1,self.cne1,self.note1,self.nom,self.prenom,self.age,self.cne,self.note]
            print(list)


e=etudiant()# rappelle de constructeur


    




