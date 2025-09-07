
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1, x2, x3, ..., xN):
        return torch.cat([torch.matmul(x1, x2), ..., torch.matmul(xN, xN)])

# Initializing the model
m = Model(10)


# Inputs to the model
x1  = torch.randn(4, 3, 64, 64) # Input tensor for first matrix
x2  = torch.randn(5, 4, 64, 64) # Input tensor for second matrix
