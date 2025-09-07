
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()

    def forward(self, input1, mat1, mat2):
        v1 = torch.addmm(input1, mat1, mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input tensor
        v2 = torch.cat([v1], dim) # Concatenate the result along a specified dimension
        return v2


# Initializing the model
m = Model(dim=0)

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
mat1 = torch.randn(8, 8)
mat2 = torch.randn(8, 8)
