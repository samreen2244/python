# can you change the self_parameter inside aclass to something eise (say "harry "). 
# try change self to "sit"or "'harry "and see the effecta.

from random import randint
class train:
   
   def __init__(slf, trainNo):
       slf.trainNo = trainNo

   def book(Harry, fro, to):
        print(f"ticket is booked in train no: {Harry.trainNo} from {fro} to {to}")
    
   def getstatus(self):
        print(f"train no: {self.trinNo} is running on time")
    
   def getFare(self, fro ,to):
        print(f"tickit  fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")
        
        
t = train(12349)
t.book("Rampure","Delhi") 
t.getstatus
t.getFare("Rampure", "Delhi")       