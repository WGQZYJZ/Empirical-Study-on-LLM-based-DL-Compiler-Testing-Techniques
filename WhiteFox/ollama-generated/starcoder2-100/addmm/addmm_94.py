
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, inp):
        v1 = torch.mm(x1, x2) 
        return v1 + inp
 
 # Initializing the model
m  = Model()

 # Inputs to the model 
 x1 = torch.randn(5, 4)
 x2 = torch.randn(5, 3)

 inp = torch.randn(5, 6)

