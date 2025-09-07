
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.addmm(x1, mat1, mat2) # A PyTorch implementation of matrix multiplication.
        return torch.cat([v1], 0)


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(3,4)
mat1  = torch.randn(5, 2) # A 2D tensor of size [5 x 2] used in matrix multiplication with another input tensor.
mat2  = torch.randn(5, 2) # A 2D tensor of size [5 x 2] used in matrix multiplication with another input tensor.
__output__  = m(x1, mat1, mat2)

