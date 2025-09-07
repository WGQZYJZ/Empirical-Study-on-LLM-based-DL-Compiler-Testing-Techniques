
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 16, 1, stride=1, padding=1)
 
    def forward(self, x1, mat1, mat2, dim):
        v1 = torch.addmm(input, mat1, mat2)
        v2 = torch.cat([v1], dim)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
mat1 = torch.randn(16, 1)
mat2 = torch.randn(16, 16)
dim = 0
