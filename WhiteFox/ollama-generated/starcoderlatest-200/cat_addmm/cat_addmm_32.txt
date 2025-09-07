
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1, x2):
        v1  = torch.addmm(x1, x2.transpose(-2, -1), x1) # A matrix multiplication is performed between two tensors and then added to an input tensor
        v2  = torch.cat([v1], dim=self.dim) # Concatenate the result along a specified dimension
        return v2


# Initializing the model
m = Model(0)

# Inputs to the model
x1  = torch.randn(8, 3, 64, 64)
x2  = torch.randn(8, 3, 64, 64)
__output__  = m(x1, x2)

 