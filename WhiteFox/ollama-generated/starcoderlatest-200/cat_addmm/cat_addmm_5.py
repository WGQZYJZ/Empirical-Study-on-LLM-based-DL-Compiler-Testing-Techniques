
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
 
    def forward(self, input, mat1, mat2):
        v1 = torch.addmm(input, mat1, mat2)  # perform matrix multiplication and add to the tensor
        v2 = torch.cat([v1], dim)  # concatenate along the specified dimension
        return v2


# Initializing the model
m = Model()

# Inputs to the model
mat1 = torch.randn(3, 8)
mat2 = torch.randn(8, 8)
input = torch.randn(3, 8)
