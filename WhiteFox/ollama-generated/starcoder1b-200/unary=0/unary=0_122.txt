
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.square(v1)
        v3 = torch.cube(v2)
        v4 = torch.sqrt(torch.pow(v3, 0.5)) * 0.044715
        v5 = v1 + v4
        v6 = torch.tanh(v5)
        v7 = v6 + 1
        v8 = torch.mul(v2, v9)
        return v8


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
