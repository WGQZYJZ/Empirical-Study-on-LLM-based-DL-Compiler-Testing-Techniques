
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
 
    def forward(self, x1, mat1, mat2):
        v1  = torch.addmm(x1, mat1, mat2)
        v2  = torch.cat([v1], dim=dim)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
dim  = 0 # Concatenate along dimension zero
mat1  = torch.randn(3, 7)
mat2  = torch.randn(5, 4, 7)
x1  = torch.randn(5, 3, 6, 8)


__output__  = m(x1, mat1, mat2)