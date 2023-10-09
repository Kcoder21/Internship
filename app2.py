class Student():
    def __init__(self,name,Class,game,movie,book):
       self.name = name 
       self.Class = Class
       self.game = game
       self.movie = movie
       self.book = book
       
    def play_game(self):
        return self.game
     
    def best_movie(self):
        return self.movie
     
    def my_class(self):
        return self.Class     
     
    def best_book(self):
         return self.book 
    
    def __str__(self):
        return f'{self.name} is a student,{self.movie} is intresting.I love playing{self.game},I love reading {self.book} '
    
    
kamshire= Student("kcoder","JSS3","CODM","Naruto Shippumen VI","Middle school life")
Awsome= Student("Asome","Basic 5", "GTA V", "Justice League","Diary of a Wimpy kid")
Great=  Student("Greatee","Jss3","Bloxc fruit","One piece","Diary of a Wimpy Kid")
print(kamshire)
print(Awsome)
print(Great)