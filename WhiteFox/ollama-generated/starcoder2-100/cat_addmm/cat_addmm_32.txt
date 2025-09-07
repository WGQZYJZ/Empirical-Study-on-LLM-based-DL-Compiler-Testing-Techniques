
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.addmm(x1, mat1, mat2) # add input to the result of a matrix multiplication 
        return torch.cat([v1], dim=0)


# Initializing the model
m  = Model() 

# Inputs to the model
x1 = torch.randn(5, 64 * 3* 3)
mat1 = torch.randn(2, 64 * 3* 3)
mat2 = torch.randn(2 ,64 + x1.size(-1))
__output__  = m(x1)

