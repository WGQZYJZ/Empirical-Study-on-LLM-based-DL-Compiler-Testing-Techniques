
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.mat1 = torch.randn(32*567)[:, None] * 0.8
        self.mat2 = torch.randn(32*567)[None, :] / 0.4
        self.dim  = dim
 
    def forward(self, x):
        v1  = torch.addmm(x, mat1=self.mat1, mat2=self.mat2)
        v2  = torch.cat([v1], dim=self.dim))

# Initializing the model
m = Model()

 # Inputs to the model
x  = torch.randn(32*567).view(-1, 32, 84)
 
 