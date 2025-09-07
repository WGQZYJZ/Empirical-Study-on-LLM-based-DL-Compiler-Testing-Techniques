
class Model(torch.nn.Module):
    def __init__(self, d1=256000, d2=384000):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.addmm(x1, x2)  # Matrix multiplication between the input and another tensor
        v2  = torch.cat([v1], dim)  # Concatenate along a specific dimension
        return v2


# Initializing the model
m = Model()

# Inputs to the model
mat1 = torch.randn(4, d1, dtype=torch.float32) + 10
mat2 = torch.randn(d1, d2).float()
__output__  = m(mat1, mat2)

