import json

class Myjson:
  def __init__(self,file,new):
    self._file = file
    self._new = new
  def read(self):
    with open(self._file) as doc:
      data = json.load(doc)
      return data
    
  def write(self):
    with open(self.file,"w") as doc:
      json.dump(self.new,doc)
