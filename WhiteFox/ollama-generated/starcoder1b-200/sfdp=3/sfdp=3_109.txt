
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 * 0.5).mul(torch.rand_like(v1))
        v3 = v1.sub_(v2).mul(0.7071067811865476)
        v4 = torch.erf(v3) + 1
        v5 = (v4 * v1).mul(v2)
        v6 = v5.matmul(v6)
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
