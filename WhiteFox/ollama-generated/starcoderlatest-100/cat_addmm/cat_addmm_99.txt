
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, mat1, mat2):
        v1 = torch.addmm(x1, mat1, mat2)  # Perform a matrix multiplication of mat1 and mat2 and add it to the input tensor
        v2 = torch.cat([v1], dim=0)  # Concatenate the result along the dimension corresponding to the index '0'
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
mat1 = torch.rand(8, 3, dtype=torch.float32)
mat2 = torch.rand(8, 3, dtype=torch.float32)
