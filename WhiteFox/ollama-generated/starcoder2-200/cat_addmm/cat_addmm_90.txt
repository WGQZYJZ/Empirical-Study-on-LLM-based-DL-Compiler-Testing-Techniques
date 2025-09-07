
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.dim = dim
 
    def forward(self, input):
        v1  = torch.addmm(input, mat1, mat2) # Applying matrix multiplication to the input tensor
        v3  = torch.cat([v1], self.dim)  # Concatenating the result of the matrix multiplication along a specified dimension
 
        return v3


# Initializing the model and generating input for it
mat1 = torch.randn(4, 5)
mat2 = torch.randn(6, 7)
input_tensor = torch.rand(40, 98)
 
m = Model(dim=0)
