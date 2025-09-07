
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=0):
         v = torch.mm(x1, 2) + inp
         return v

 # Initializing the model
m = Model()
 
 
 # Inputs to the model
x1 = torch.randn(4, 3, dtype=torch.float64)
inp_1 = torch.tensor(0., dtype=torch.float64).cuda() if torch.cuda.is_available() else torch.tensor(0.)
 
 
 