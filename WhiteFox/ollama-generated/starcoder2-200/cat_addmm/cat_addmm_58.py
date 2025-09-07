
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
 
    def forward(self, x1, mat1, mat2):
        v0  = torch.addmm(x1, mat1, mat2)
        v1  = torch.cat([v0],dim)
        return v1


# Initializing the model
m = Model()
m_ = Model(dim=3)
 
# Inputs to the model
mat1 = torch.randn((4896))
mat2 = torch.randn((768, 4896))
input = torch.randn((3, 4, 5))
__output__0 = m(input, mat1, mat2)
__output__1 = m_(input, mat1, mat2)

