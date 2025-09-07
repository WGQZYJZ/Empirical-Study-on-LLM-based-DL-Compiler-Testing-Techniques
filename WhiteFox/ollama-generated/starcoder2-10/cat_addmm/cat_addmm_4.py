
class Model(torch.nn.Module):
    def __init__(self, mat1=None, mat2=None, dim=0):
        super().__init__()
        self.mat1 = torch.nn.Parameter(mat1) if mat1 is not None else None
        self.mat2 = torch.nn.Parameter(mat2) if mat2 is not None else None
        self.dim  = dim
 
    def forward(self, x):
        v0 = self.mat1 * self.mat2 + x 
        v1 = torch.cat([v0], dim=self.dim)
        return v1

# Initializing the model with a random matrix
mat1 = torch.randn((3, 7))
m = Model(mat1=mat1)

