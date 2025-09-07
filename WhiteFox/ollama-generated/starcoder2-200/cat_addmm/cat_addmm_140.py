
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.addmm(x1, mat1, mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        v3  = torch.cat([v1], dim) 
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(batch_size, 784) # Randomly generated 2D array
mat1 = torch.randn(input_dim, mat_dim) # Randomly generated 2D array with the input dimension as rows and a fixed number of columns
mat2 = torch.randn(mat_dim, output_dim) # Randomly generated 2D array with a fixed number of rows and the output dimension as columns


__output__=m(x1)