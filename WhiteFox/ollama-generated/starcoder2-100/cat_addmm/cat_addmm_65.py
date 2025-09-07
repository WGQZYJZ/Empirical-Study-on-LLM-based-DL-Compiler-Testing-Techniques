
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
 
    def forward(self, x):
        v1  = torch.addmm(x, mat1, mat2)
        v2 = torch.cat([v1], dim) 
        return v2

# Initializing the model with the specified argument for concatenation dimension
m = Model()

