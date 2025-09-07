
class Model(torch.nn.Module):
    def __init__(self, dim=2):
        super().__init__()
 
    def forward(self, x1, m1, m2):
        v1 = torch.addmm(x1, m1, m2) 
        return torch.cat([v1], dim)

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(10, 64)
mat1 = torch.randn(64, 32)
mat2 = torch.randn(32, 8)
__output__  = m(x1, mat1, mat2)

