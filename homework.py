class Fut():
    def __init__(self,rating,name,nationality,dribbling,shooting) :
        self.rating = rating
        self.name = name
        self.nationality = nationality
        self.dribbling = dribbling
        self.shooting = shooting
      
    
    def my_rating (self):
     return self.rating    
 
    def change_my_rating( self,my_new_rating):
        self.rating = my_new_rating
    
    def my_name(self):
        return self.name
   
    def my_nationality(self):
        return self.nationality
 
    def my_dribbling(self):
        return self.dribbling

    def change_my_dribbling(self,my_new_dribbling):
        self.dribbling = my_new_dribbling
    
    def my_shooting(self):
        return self.shooting
    
    def __str__(self):
        return f'{self.name} is a Footballer {self.name} is {self.nationality}. {self.name} loves his fifa rating which is {self.rating} {self.name} shooting in fifa is {self.shooting}   {self.name} dribbling is {self.dribbling} '
 
 
Messi= Fut(90,'Messi',"Argentinian",94,90)

Messi.change_my_rating("91")
Messi.change_my_dribbling("97")

print(Messi)
