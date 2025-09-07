

class Model(torch.nn.Module):
    def __init__(self, mat1, mat2):
        super().__init__()
        self.mat1  = torch.nn.Parameter(data=mat1)
        self.mat2  = torch.nn.Parameter(data=mat2)
 
    def forward(self, x1):
        v1  = torch.addmm(x1, self.mat1, self.mat2)
        return torch.cat([v1], dim=0)

# Initializing the model with two tensors as parameters
mat1  = torch.randn((32, 3, 8), requires_grad=True) # Generates a randomly-initialized 3D tensor with a size of (32, 3, 8) that will be used for matrix multiplication. The number of columns in the first dimension is fixed at 3; however, the third dimension can vary based on the input dimensions
mat2  = torch.randn((1024, 32), requires_grad=True) # Generates a randomly-initialized tensor with a size of (1024, 32). The number of rows in this second tensor is fixed at 32; however, the third dimension can vary based on the input dimensions. This is necessary because matrix multiplication requires that one column in the first tensor matches the number of rows in the second tensor
m = Model(mat1=mat1, mat2=mat2)

 # Inputs to the model
  x1  = torch.randn((5000,3)) # Generates a randomly-initialized 2D tensor with a size of (5000, 3). This is an input for the model. It can have any dimensionality and can be of any size. However, we need to ensure that it matches the size of our matrices above, which are fixed in this example

# Evaluating the output of the model with the inputs from the previous cell
__output__  = m(x1)

