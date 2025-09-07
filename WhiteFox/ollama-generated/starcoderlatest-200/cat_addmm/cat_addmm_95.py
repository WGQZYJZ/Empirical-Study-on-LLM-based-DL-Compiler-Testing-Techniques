
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
 
    def forward(self, x1, mat1, mat2):
        v1 = torch.addmm(x1, mat1, mat2)
        v2 = torch.cat([v1], dim)
        return v2


# Inputs to the model
__input__  = torch.randn(256, 3072, requires_grad=True)
x1         = __input__.view(-1, 1, 64, 64)
mat1       = torch.randn(64, 8, requires_grad=True)
mat2       = torch.randn(8, 3072, requires_grad=True)


