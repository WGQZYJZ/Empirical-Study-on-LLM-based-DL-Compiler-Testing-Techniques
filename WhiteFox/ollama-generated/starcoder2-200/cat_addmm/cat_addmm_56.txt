
class Model(torch.nn.Module):
    def __init__(self, mat1=None, mat2=None):
        super().__init__()
        self.mat1 = torch.nn.Parameter(mat1) if mat1 is not None else torch.nn.Parameter(0.5 * torch.randn(32))
        self.mat2 = torch.nn.Parameter(mat2) if mat2 is not None else torch.nn.Parameter(torch.rand(3, 3).float() * 0.1 + 0.9)

    def forward(self, x):
        v1 = torch.addmm(x, self.mat1, self.mat2)
        return torch.cat([v1], dim=1)


# Initializing the model with custom matrices
mat1 = np.random.rand(3, 64).astype(np.float32)
mat2 = np.random.rand(64, 10).astype(np.float32)
m = Model(mat1=mat1, mat2=mat2)

 # Inputs to the model with a custom matrix
x = torch.randn(8, 3, 32, 32)
 
__output__  = m(x)