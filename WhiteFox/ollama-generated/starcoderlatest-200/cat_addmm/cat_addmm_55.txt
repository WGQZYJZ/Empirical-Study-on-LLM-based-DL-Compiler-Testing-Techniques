
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
 
    def forward(self, x1, mat1, mat2):
        v1 = torch.addmm(x1, mat1, mat2)
        v2 = torch.cat([v1], dim=dim)
        return v2


# Initializing the model and using it for testing purposes only
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
mat1 = torch.ones(8, dtype=torch.float)
mat2 = torch.zeros(8, dtype=torch.float)
