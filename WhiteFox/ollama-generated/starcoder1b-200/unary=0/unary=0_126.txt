
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 ** 2
        v4 = v3 * v1
        v5 = torch.tanh(v4)
        v6 = v5 + 1
        v7 = v2 * v9
        v8 = torch.erf(v7)
        v9 = v8 + 1
        v10 = v1 * v9
        return v10


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
