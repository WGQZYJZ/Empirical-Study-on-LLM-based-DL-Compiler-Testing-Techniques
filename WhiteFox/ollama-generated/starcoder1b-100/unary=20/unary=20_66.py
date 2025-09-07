
class Upsample(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 4, 1, stride=2, padding=0)
 
    def forward(self, x):
        return self.conv(x) * 0.5


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.upsample = Upsample()
        self.conv1 = torch.nn.Conv2d(4, 8, 3, stride=1, padding=1)
 
    def forward(self, x):
        out = self.upsample(x)
        out = self.conv1(out)
        return out


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 8, 64, 64)
