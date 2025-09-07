
class Model(torch.nn.Module):
    def __init__(self, mat1, mat2, dim=0):
        super().__init__()
        self.mat = torch.nn.Parameter(torch.randn(3, 5))
        self.dim  = dim

    def forward(self, x1):
        v1  = torch.addmm(x1, self.mat[None], None)
        v2  = torch.cat([v1], self.dim)
        return v2


# Initializing the model
m = Model(torch.randn(30,5), torch.randn(40,6))

# Inputs to the model
x1 = torch.randn(70, 80, 90)
__output__  = m(x1)

