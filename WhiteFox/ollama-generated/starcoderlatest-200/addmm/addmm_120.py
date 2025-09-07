
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1, inp)
        v2 = v1 + inp
        return v2

 # Initializing the model
m = Model()
 
 # Inputs to the model
 x1 = torch.randn(10, 8, 32, 32)
 inp = torch.randn(10, 4, 32, 32)
 