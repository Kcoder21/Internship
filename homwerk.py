class   Uchiha ():
    def __init__(self,name,best_jutsu,daughter,wife,rank):
       self.name = name 
       self.best_jutsu = best_jutsu
       self.daughter = daughter
       self.wife = wife
       self.rank = rank
    
    def my_name(self):
        return self.name
     
    def my_best_jutsu(self):
      return
    
    def change_best_jutsu(self, new_best_jutsu):
        self.best_jutsu = new_best_jutsu   
     
    def my_daughter(self):
         return self.daughter

 
 
 
    def my_wife(self):
        return self.wife
    
    def my_rank(self):
        return self.rank 
        
    def change_my_rank(self,my_new_rank):
        self.rank = my_new_rank 
     
     
     
    
    def __str__(self):
        return f'{self.name} is a shinobi {self.best_jutsu} is very good. {self.name} loves {self.daughter},{self.name} loves  {self.wife}   {self.name} rank is {self.rank} '
     

     
Sasuske= Uchiha("Sasuske","Chidori","Sarada", "Sakura", "Special Jonin")

Sasuske.change_best_jutsu(" Fireball")
Sasuske.change_my_rank ("villige gaurdian")



print(Sasuske)


    