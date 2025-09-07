
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, x2, 0) # Multiply the first element in each tensor by the second one and then sum them up to get a single scalar value of the matrix multiplication between the two tensors
        v2 = torch.cat([v1], self.dim) # Concatenate the result along the specified dimension
        return v2


# Initializing the model
m = Model(0)

# Inputs to the model
x1  = torch.randn(2, 8)
x2  = torch.randn(4, 8)
