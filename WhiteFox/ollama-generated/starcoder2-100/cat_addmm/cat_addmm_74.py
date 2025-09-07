
class Model(torch.nn.Module):
    def __init__(self, mat1=None, mat2=None):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.Tensor([7]) 
        v1  = torch.randn((3, 4)) # generate a random 2D matrix with shape (3, 4)
        v2 = v1 + 5
        v3 = v0 * v2
        v4 = torch.mm(v1, v3) # Perform the multiplication between two matrices and then add it to another tensor
        v5  = torch.cat([v4], dim=1) 
        return v5

# Initializing the model with default values for mat1 & mat2
m  = Model()
m(x1)

