
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.scale = 0.7071067811865476
 
    def forward(self, x1):
        x2  = self.conv(x1).div_(self.scale)
        v1   = torch.einsum('bij,bij->b', (x1, x2))
        v2   = torch.matmul(x1, x2)
        v3   = v1 * v2
        v4   = torch.erf(v3)
        v5   = v4 + 1
        v6   = torch.matmul(x2, v5)
        return v6


# Initializing the model
m  = Model()
# Input to the model
x1  = torch.randn(1, 3, 64, 64)
