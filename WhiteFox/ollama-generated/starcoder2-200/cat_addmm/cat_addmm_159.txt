

import torch

class Model(torch.nn.Module):
    def __init__(self, mat1, mat2, dim):
        super().__init__()
 
        self.mat1  = mat1 
        self.mat2  = mat2 
        self.dim   = dim 

    def forward(self, input):
        t1  = torch.addmm(input, self.mat1, self.mat2) # Perform a matrix multiplication of the model matrices and the input tensor, and add it to the result of this operation
        t2  = torch.cat([t1], self.dim) 
        return t2

# Initializing the model
mat1  = torch.randn(50, 48) # A matrix with random values
mat2  = torch.randn(50, 63) # A matrix with random values
m     = Model(mat1, mat2, dim=0)

# Inputs to the model
x1    = torch.randn(7948, 1000) 

