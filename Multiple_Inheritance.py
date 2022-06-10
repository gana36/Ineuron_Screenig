class parent1:
  def __init__(self,voice):
    self.voice=voice
  def voic(self):
    print(f"His Voice is very {self.voice}")
class parent2:
  def colr(self):
    print(f'Skin tone is natural')

class child(parent1,parent2):
  def __init__(self,height,voice):
    self.height=height
    self.voice=voice
  def heig(self):
    print(f"{self.height} feet tall")
    parent2.colr(self)
    parent1.voic(self)

c3=child(6,'vibrating')
c3.heig()