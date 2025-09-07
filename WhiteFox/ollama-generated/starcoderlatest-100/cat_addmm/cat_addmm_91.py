
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1):
        v1  = torch.addmm(x1, x2, x3) # Perform a matrix multiplication of x2 and x3 and add it to the input tensor
        v2 = torch.cat([v1], dim=self.dim) # Concatenate the result along the dimension specified by `self.dim`
        return v2


# Initializing the model
m = Model(10)

# Inputs to the model
x1  = torch.randn(2, 3, 64, 64)
__output__  = m(x1)

