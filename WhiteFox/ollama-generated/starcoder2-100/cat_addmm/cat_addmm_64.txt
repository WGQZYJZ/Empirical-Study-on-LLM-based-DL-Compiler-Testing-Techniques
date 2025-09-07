
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1, mat1, mat2):
        v1  = torch.addmm(x1, mat1, mat2)
        v2  = torch.cat([v1], self.dim)

# Initializing the model
m = Model()
mat1 = torch.randn(5, 4)
mat2 = torch.randn(3, 4)
__output__  = m(torch.randn(6), mat1, mat2)

