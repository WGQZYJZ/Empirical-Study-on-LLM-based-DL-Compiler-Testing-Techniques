
class Model(torch.nn.Module):
    def __init__(self, mat1, mat2):
        super().__init__()
        self.mat1 = torch.nn.Parameter(mat1)
        self.mat2 = torch.nn.Parameter(mat2)
 
    def forward(self, x1):
        return self.mat1 @ self.mat2 + x1

# Initializing the model
m  = Model(torch.randn((32, 32), device='cuda'), torch.randn((32, 32)))

# Inputs to the model
x1 = torch.randn(16, 3, 64, 64)
