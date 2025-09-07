
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v0 = torch.mm(x1, inp)
        v2  = v0 + inp
        return v2


# Initializing the model
m = Model()

 # Inputs to the model
inp = torch.randn(489, 736)
 
x1 = torch.randn(456, 893)
