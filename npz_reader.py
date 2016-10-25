
class NPZInputReader():
  def __init__(self, file_path="", dim_x=1, dim_y=1, sim_time=1000):
    self.retinaLeft = [[[] for y in range(dim_y)] for x in range(dim_x)]
    self.retinaRight = [[[] for y in range(dim_y)] for x in range(dim_x)]
        
    f=load(file_path)
    left=f["left"]
    right=f["right"]
    left["time"] /= 1000. # us to ms
    right["time"] /= 1000.
    
    for t,x,y,p in left:
      self.retinaLeft[x][y].append(t)
    
    for t,x,y,p in right:
      self.retinaRight[x][y].append(t)


