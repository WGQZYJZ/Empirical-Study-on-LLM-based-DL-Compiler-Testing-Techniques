
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.dim = dim
 
    def forward(self, x1):
        mat1 = torch.eye(self.dim)
        mat2 = torch.zeros((self.dim,))
        v1 = self.conv(x1)
        v2 = torch.addmm(v1, mat1, mat2)
        t2 = torch.cat([v2], dim=self.dim)
        return t2

# Initializing the model
m = Model(3)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
