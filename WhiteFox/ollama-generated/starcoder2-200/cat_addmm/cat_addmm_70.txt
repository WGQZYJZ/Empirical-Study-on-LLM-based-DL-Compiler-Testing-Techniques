
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.mat1  = torch.randn([320, 64]) # First matrix for performing matrix multiplication with size (320 x 64)
        self.mat2  = torch.randn([8, 9753]) # Second matrix for performing matrix multiplication with size (8 x 9753)
        self.dim  = dim

    def forward(self, x1):
        v1  = x1
        v2  = torch.addmm(v1, mat1, mat2) 
        v3  = torch.cat([v2], dim) # Concatenate the output of the matrix multiplication with the given dimension
        return v3

# Initializing the model
m = Model(0)

# Inputs to the model
x1  = torch.randn(8, 9753)
__output__  = m(x1)

# Initializing the model
m = Model(2)

# Inputs to the model
x1  = torch.randn(80, 4360)
__output__  = m(x1)

