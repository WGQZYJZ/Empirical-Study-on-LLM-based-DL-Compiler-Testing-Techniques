
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.addmm = torch.addmm
 
    def forward(self, x1):
        v1  = torch.addmm(x1, mat1, mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        v2  = torch.cat([v1], dim) # Concatenate the result along a specified dimension
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(3, 64)
mat1 = torch.randn(30, 64)
mat2 = torch.randn(30, 7950)
__output__  = m(x1)