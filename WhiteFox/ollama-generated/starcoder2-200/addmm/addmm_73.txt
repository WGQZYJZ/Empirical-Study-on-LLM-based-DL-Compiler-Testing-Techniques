
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, x1, x2, inp=None):
       v0 = torch.mm(x1, x2)
       v1 = v0 + 1 if (inp != None) else 0
       return v1

 # Initializing the model
m = Model()
 
 # Inputs to the model
 x1  = torch.randn(8, 3)
 x2  = torch.randn(3, 4)
 inp_tensor=torch.randn(5, 7) if (inp!=None) else None
 
 