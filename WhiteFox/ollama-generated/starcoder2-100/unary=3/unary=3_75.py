
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v0  = torch.randn(4, 3, 64, 64)
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v1 * 0.7071067811865476
        v4  = torch.erf(v3)
        v5  = v4 + 1
        v6  = v2 * v5
        return v6

# Initializing the model
m = Model()

# Inputs to the model
x0, x1 = torch.randn(4, 8, 3), torch.randn(4, 8, 3)
__output__  = m(x0), m(x1)

