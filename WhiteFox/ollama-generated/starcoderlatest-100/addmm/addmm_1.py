
class Model(torch.nn.Module):
    def __init__(self, inp=100):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = v1 + inp
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(32, 64, 800, 800)
x2 = torch.randn(32, 64, 800, 800)
