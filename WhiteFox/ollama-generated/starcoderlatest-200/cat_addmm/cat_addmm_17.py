
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
 
    def forward(self, x1, mat1, mat2):
        v1 = torch.addmm(x1, mat1, mat2)
        v2 = torch.cat([v1], dim)
        return v2


# Inputs to the model
__input__ = torch.randn(32, 32, 8)
__mat1__ = torch.randn(1, 2, 2)
__mat2__ = torch.randn(2, 3, 3)
dim = -1
