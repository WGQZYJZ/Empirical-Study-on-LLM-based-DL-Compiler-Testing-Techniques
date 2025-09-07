
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = F.conv2d(x1, 0.5)
        v2 = F.conv2d(v1, 0.7071067811865476)
        v3 = torch.erf(v2)
        v4 = v3 * 0.044715
        v5 = v1 + v4
        v6 = F.conv2d(v5, 0.7978845608028654)
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
