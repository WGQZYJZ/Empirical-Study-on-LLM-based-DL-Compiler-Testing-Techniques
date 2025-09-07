
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.linear = torch.nn.Linear(8, 1)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, x2, mat) # Perform a matrix multiplication of x2 and mat and add it to the input tensor
        v2 = torch.cat([v1], dim) # Concatenate the result along a specified dimension
        return v2


# Initializing the model
m = Model(dim=0)

# Inputs to the model
x1  = torch.randn(1, 8, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
mat = torch.randn(1, 3, 3, 3)
