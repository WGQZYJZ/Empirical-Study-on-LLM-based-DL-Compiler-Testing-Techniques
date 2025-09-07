
class Model(torch.nn.Module):
    def __init__(self, inp=None):
        super().__init__()
 
    def forward(self, x1, x2=None):
        v1 = torch.mm(x1, x2)
        if x2 is None:
            v2 = v1 + inp
        else:
            v3 = torch.cat((v1, v2), dim=1)
        return v3
# Initializing the model
m = Model()

 # Inputs to the model with two inputs
x1 = torch.randn(1, 8)
