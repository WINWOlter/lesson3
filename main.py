class Person:
  height = 170
  name = "Mark"
  is_sad = True
  def __init__(self,name,haight):
   self.name = name
   self.haight = haight


class Vova:
 height = 174
 age = 13
 name = "Vova"



class Cat:
 height = 40
 age = 3
 name = "Cat"
 def __init__(self,name,height):
  self.name = Cat
  self.age = 3
  
 def play_w_human(self,human):
  human.is_sad = False

my_pet = Cat("Cat",40)
me = Person("Mark",170)
you = Person('Vova', 176)

print(me.is_sad)

my_pet.play_w_human(me)

print("Сумний - ",me.is_sad)
     
     

     
  