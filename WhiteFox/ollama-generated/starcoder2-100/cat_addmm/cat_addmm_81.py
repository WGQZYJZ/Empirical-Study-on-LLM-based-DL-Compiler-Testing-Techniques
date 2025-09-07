
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, mat1, mat2, dim=0):  # The input is a tuple of three tensors (x1, mat1, mat2) along with the index by which to concatenate the result tensor.
        v1 = torch.addmm(x1, mat1, mat2)
        v2 = torch.cat([v1], dim)
        return v2


# Initializing the model 
m = Model()
 
# Inputs for the model
mat1 = torch.randn((5, 3)) # Shape (5, 3), a random matrix
mat2 = torch.randn(5, 4) # Shape (5, 4), another random matrix
x1 = torch.randn(60, 78, 198) # A tensor of shape (60, 78, 198). This will be the input to the model

 