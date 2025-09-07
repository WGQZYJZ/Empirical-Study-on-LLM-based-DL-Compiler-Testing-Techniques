
class Model(torch.nn.Module):
    def __init__(self, mat1, mat2, dim):
        super().__init__()
        self.mat1 = mat1
        self.mat2 = mat2
        self.dim = dim
 
    def forward(self, x):
        v1 = torch.addmm(x, self.mat1, self.mat2)
        v2 = torch.cat([v1], self.dim)
        return v2


# Initializing the model
m = Model(torch.ones(10, 3), torch.ones(3, 2), 1)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
