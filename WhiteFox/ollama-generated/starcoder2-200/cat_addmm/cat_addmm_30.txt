
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v  = torch.addmm(x1, mat1, mat2) # Performs a matrix multiplication and then adds it to an input tensor
        return  torch.cat([v], dim)

# Inputs to the model
mat1  = torch.randn(784, 50)
mat2  = torch.randn(784, 396)
 
x1  = torch.randn(32, 50) # This is an input tensor to a matrix multiplication operation
__output__  = m(x1, mat1)

