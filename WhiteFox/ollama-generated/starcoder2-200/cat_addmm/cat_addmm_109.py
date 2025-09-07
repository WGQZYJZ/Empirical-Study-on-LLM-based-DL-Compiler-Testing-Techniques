
class Model(torch.nn.Module):
    def __init__(self, mat1 = torch.ones((32, 3)), mat2=None):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.addmm(x1, mat1) 
        return torch.cat([v1], dim)

# Initializing the model with default parameters
m = Model()

# Inputs to the model
x1 = torch.randn(128,3) # Generate a random input tensor of shape (128, 3)
