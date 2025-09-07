
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
 
    def forward(self, x1, mat1, mat2):
        v1  = torch.addmm(x1, mat1, mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        v3  = torch.cat([v1], dim=dim) 
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(4, 5, 80, 72) # Input tensor of shape (4, 5, 80, 72)
mat1  = torch.randn(396, 72) # A randomly generated 396x72 tensor as a parameter to the model
mat2  = torch.randn(396, 72) # A randomly generated 396x72 tensor as another parameter to the model


