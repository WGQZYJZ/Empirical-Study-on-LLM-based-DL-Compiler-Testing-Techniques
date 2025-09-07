
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.pow(v1, 0.5)
        v3 = torch.pow(v1, 0.7071067811865476)
        v4 = torch.exp(v3)
        v5 = torch.multiply(v4, torch.divide(v4, v4))
        v6 = v2 + v5
        v7 = torch.tanh(v6)
        v8 = torch.addcdiv(v7, 1, v1)
        v9 = torch.multiply(v8, 0.7978845608028654)
        v10 = torch.tanh(v9)
        return v10


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
