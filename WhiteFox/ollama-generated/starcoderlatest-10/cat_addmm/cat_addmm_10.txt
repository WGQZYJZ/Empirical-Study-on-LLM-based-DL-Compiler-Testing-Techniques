
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
 
    def forward(self, x1, mat1, mat2):
        v1 = torch.addmm(x1, mat1, mat2)
        v2 = torch.cat([v1], dim)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(4, 3, 64, 64)
mat1 = torch.randn(8, 3)
mat2 = torch.randn(12, 3)
