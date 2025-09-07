

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v1 ** 3 # Cube the output of the transposed convolution to compute v4 (output of the multiplication to be added with v3)
        v4  = torch.nn.functional.normalize(v3, p=2, dim=(1,)) * 0.044715 
        v6  = x1 + v4 # Add v3 to the output of the transposed convolution (to compute v5 which is added with v9)
        v8  = torch.nn.functional.normalize(v6 ** 2, p=2, dim=(1,)) * 0.7978845608028654 # Compute v9 (output of the multiplication to be added with v3)
        v10 = x1 + torch.nn.functional.normalize(v8 ** 2, p=2, dim=(1,)) * v9 # Add output of v8 (v10 is actually a copy of the output of the transposed convolution) to the output of v5 (which is also v3) and the second time add the second argument of torch.nn.functional.normalize
        v12 = v7 + 1  # Compute v11 by adding 1 to v4 (the input to v7 in the hyperbolic tangent function) and then multiplying v2 with v11
        v13 = v6 + v9 # Add v5 from before with output of v8 
        return torch.nn.functional.normalize(v10 ** 2, p=2, dim=(1,)) * v13 # Compute output of the hyperbolic tangent function and then multiply it by the output of addition


# Initializing the model:
m = Model()
 
# Inputs to the model:
x1 = torch.randn(50, 8, 47, 29)

