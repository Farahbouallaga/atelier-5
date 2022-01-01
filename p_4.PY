class point:# class point
    def __init__(self ,x=0.0,y=0.0) :
       
        self.px=float(x)
        self.py=float(y)
class segment :# class segment avec l'utilisation de class point
    def __init__(self,x1,y1,x2,y2):

        self.orig=point(x1,y1)
        self.extrem=point(x2,y2)
        print('segment :')
        print (self.orig.px,self.orig.py,self.extrem.px,self.extrem.py)


s=segment(1,2,3,4)