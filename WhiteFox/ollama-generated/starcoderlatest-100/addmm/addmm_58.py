
class Model(torch.nn.Module):
    def __init__(self, inp=0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1, x1)
        v2 = v1 + (inp if inp is not None else 0)
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
