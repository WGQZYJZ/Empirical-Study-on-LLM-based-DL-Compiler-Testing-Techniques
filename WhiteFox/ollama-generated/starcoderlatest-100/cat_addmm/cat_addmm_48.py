
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.addmm(v1, mat1, mat2)
        v3 = torch.cat([v1], dim)
        return v6
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
