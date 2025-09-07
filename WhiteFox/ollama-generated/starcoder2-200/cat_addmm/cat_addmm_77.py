
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1, mat1, mat2):
        v1  = torch.addmm(x1, mat1, mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        v2  = torch.cat([v1], self.dim) 
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 64) # Input tensor with size (batch_size x vector dimensionality)
mat1 = torch.randn(64, 96)
mat2 = torch.randn(96, 8) 

