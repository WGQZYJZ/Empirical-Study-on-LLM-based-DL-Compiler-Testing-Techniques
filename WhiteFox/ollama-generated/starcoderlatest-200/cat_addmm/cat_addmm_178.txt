
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.addmm(x1, mat1, mat2)  # Add matrix multiplication of two matrices and add it to the input tensor
        v2 = torch.cat([v1], dim)   # Concatenate along a specified dimension
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
