
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp = None):
        v1 = torch.mm(x1, x2)
        v2 = v1 + inp
        return v6


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
