
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
      splitted = torch.split(x1,[500])
      merged =  torch.cat([splitted[i] for i in range(len(splitted))],dim=2) #this is a bug 
      return merged

m  = Model()

# Inputs to the model