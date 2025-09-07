
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, mat1, mat2):
        v1 = torch.addmm(x1, mat1, mat2)
        v2 = torch.cat([v1], dim=0)
        return v2


# Inputs to the model
mat1 = torch.randn(2, 3, 5, 6) # (2, 3, 5, 6) matrix multiplication is performed
mat2 = torch.randn(2, 3, 7, 8) # (2, 3, 7, 8) matrix multiplication is performed
x1   = torch.randn(2, 3, 9, 10) # (2, 3, 9, 10) is concatenated along dimension 0 with mat1 and x1
