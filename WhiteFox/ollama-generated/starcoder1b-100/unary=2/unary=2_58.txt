
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = torch.pow(v2, 1.0 / 3.0)
        v4 = torch.tanh(torch.pow(v3, -2.0))
        v5 = torch.erf(v4)
        v6 = v2 * v8 = v5 * v5 + v4
        v7 = v6 * v1
        return v7


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
