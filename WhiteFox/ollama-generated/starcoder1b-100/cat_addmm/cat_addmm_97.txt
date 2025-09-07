
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Conv2d(3, 8, 1)
        self.m2 = torch.nn.Linear(4096, 4096)
 
    def forward(self, x1):
        v1 = self.m1(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = self.m2(torch.cat([v2, v5], dim=1))
        return v6


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
