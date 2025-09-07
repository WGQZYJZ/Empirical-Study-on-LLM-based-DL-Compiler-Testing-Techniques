
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.inp = inp
 
    def forward(self, x1, inp):
        v1 = self.conv(x1)
        v2 = v1  * 0.5 + self.inp
        return v2


# Initializing the model
m = Model()

# Inputs to the model
inp = torch.randn(3, 3, 64, 64)
