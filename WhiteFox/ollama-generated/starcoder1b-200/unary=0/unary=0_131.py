
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.pow(v1, 2)
        v3 = torch.pow(v2, 1.0 / 3)
        v4 = torch.pow(v1, -1.5 / 6)
        v5 = v4 * 0.5
        v6 = v5 + 1
        v7 = v3 * v6
        v8 = torch.tanh(v7)
        v9 = v8  + 1
        v10 = v2 * v9
        return v10


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
