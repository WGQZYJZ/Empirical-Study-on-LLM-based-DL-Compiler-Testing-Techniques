
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=0.5):
        v1 = torch.mm(x1, x2) + inp
        return v1

 # Initializing the model
m  = Model()
 
 # Inputs to the model 
 x1 = torch.randn(8, 32), x2 = torch.randn(32, 64)
  