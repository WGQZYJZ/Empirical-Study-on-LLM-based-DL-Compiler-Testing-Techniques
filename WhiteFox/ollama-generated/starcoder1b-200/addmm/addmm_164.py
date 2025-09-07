
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 4, 1)
        self.conv2 = torch.nn.Conv2d(4, 8, 1)
 
    def forward(self, x1, inp=None):
        v1 = self.conv1(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + inp
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 10, 10)
inp = torch.randn(2, 8)
