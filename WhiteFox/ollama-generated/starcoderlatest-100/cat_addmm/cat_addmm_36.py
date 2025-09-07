
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = torch.addmm(input, mat1, mat2)
        v2 = torch.cat([t1], dim) 
        return v6


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
