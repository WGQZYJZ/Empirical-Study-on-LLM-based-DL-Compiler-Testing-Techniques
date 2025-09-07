
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        input = x1
        mat1 = torch.rand(4, 4)
        mat2 = torch.rand(8, 6)
        v1  = torch.addmm(input, mat1, mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        v2 = torch.cat([v1], dim=1) # Concatenate the result along a specified dimension
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 8, 6, 56)
