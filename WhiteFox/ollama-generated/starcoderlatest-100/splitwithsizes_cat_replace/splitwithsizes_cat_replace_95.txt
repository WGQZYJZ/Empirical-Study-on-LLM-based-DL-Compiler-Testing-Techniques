
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1):
        s1, s2, s3  = torch.split(x1, [self.dim/2, 0.5 * self.dim, 0.7071067811865476 * self.dim], dim=self.dim) # Split the input tensor into three tensors along a given dimension
        s4 = torch.erf(s3) # Apply the error function to the output of the convolution
        c = torch.cat([s1, s2, s4], dim=self.dim) # Concatenate all the split tensors along the same dimension and then compute the output of the model
        return c


# Initializing the model
m = Model(2)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
