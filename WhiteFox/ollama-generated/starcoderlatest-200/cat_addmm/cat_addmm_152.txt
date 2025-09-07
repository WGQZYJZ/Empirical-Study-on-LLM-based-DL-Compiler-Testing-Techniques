
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, mat1, mat2, dim=0):
        v1 = torch.addmm(x1, mat1, mat2)  # Perform a matrix multiplication of mat1 and mat2 and add it to the input tensor
        v2 = torch.cat([v1], dim)  # Concatenate the result along a specified dimension
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
mat1 = torch.randn(64, 8)
mat2 = torch.randn(3, 8)
dim = 1 # axis=0: concatenate along a row, i.e., the height dimension, and axis=1: concatenate along a column, i.e., the width dimension
