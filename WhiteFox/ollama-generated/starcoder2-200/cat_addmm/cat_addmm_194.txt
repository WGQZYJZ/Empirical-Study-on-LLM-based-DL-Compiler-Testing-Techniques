
class Model(torch.nn.Module):
    def __init__(self, dim=3):
        super().__init__()

    def forward(self, x1, mat1, mat2): 
        v1  = torch.addmm(x1, mat1, mat2)
        return torch.cat([v1], dim)


# Initializing the model
m  = Model()

 # Inputs to the model
mat1  = torch.randn(5, 8, 32, 32)
mat2  = torch.randn(49*8, 7)
x1    = torch.rand(64, 49*8)
dim   = 0
