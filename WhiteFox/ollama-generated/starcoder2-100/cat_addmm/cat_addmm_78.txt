
class Model(torch.nn.Module):
    def __init__(self, mat1, mat2):
        super().__init__()
 
    def forward(self, x0):
        v1  = torch.addmm(x0, mat1, mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        v3  = torch.cat([v1], 0) # Concatenate the result along axis 0
        return v3

# Initializing model
m = Model(mat1=torch.randn((5,4)),
          mat2=torch.randn((4,6)))
 
# Inputs to the model
x0 = torch.randn(784)
__output__  = m(x0)

