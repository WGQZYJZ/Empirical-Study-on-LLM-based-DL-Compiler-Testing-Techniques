
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, inp):
        v1 = self.conv(inp)
        v2 = torch.mm(v1, v1) + inp
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
inp = torch.randn(1, 8, 64, 64)
