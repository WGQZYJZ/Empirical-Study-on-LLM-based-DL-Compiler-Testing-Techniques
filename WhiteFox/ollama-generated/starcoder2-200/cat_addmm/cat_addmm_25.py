
class Model(torch.nn.Module):
    def __init__(self, mat1, mat2, dim):
        super().__init__()

    def forward(self, x1):
        v1 = torch.addmm(x1, mat1, mat2)
        return  torch.cat([v1], dim=dim)


# Initializing the model
mat1  = torch.randn(500, 3948)
mat2  = torch.randn(3948, 768)
m     = Model(mat1, mat2, -1)
x1    = torch.randn(48, 3948)
__output__  = m(x1)

