
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2):
         v7 = torch.full([4096], 1)
         v8 = torch.cumsum(v7, 0)
         return v8

 # Initializing the model
 m = Model()
 
 # Inputs to the model