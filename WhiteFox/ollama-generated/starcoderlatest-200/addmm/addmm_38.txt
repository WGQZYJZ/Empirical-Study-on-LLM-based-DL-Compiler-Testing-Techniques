
class Model(torch.nn.Module):
    def __init__(self, inp: torch.Tensor = None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1) * 0.5
        v2 = torch.mm(v1, x2) + inp
        return v2


# Initializing the model with a keyword argument 'inp'
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(3, 64, 64)
