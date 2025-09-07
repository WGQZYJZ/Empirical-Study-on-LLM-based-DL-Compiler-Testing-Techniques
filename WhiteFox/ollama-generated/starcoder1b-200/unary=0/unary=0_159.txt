
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).pow(0.5)
        v2 = torch.square(v1)
        v3 = torch.pow(v2, 3)
        v4 = v3 * v1
        v5 = (torch.tanh(v4)) + 1
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
