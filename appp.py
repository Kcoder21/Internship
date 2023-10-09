class Hokage ():
    def __init__(self,name,best_jutsu,Parents,son,wife,rank):
       self.name = name 
       self.best_jutsu = best_jutsu
       self.Parents = Parents
       self.son = son
       self.wife = wife
       self.rank = rank
    
    def my_name(self):
        return self.name
     
    def my_best_jutsu(self):
        return self.best_jutsu
    
    def change_best_jutsu(self, new_best_jutsu):
        self.best_jutsu = new_best_jutsu
     
    def my_Parents(self):
        return self.Parents     
     
    def my_son(self):
         return self.son

    def my_wife(self):
        return self.wife
    
    def my_rank(self):
        return self.rank
     
    
    def __str__(self):
        return f'{self.name} is a shinobi {self.best_jutsu} is very good. {self.name} love his {self.Parents}, {self.name} loves his {self.son},{self.name} loves his {self.wife}   {self.name} rank is {self.rank} '
     

     
Naruto= Hokage("Naruto","sexy jutstu","Minato & Minani", "Boruto" , "Hinata", "Hokage")

Naruto.change_best_jutsu("Rasengan")

print(Naruto)


    