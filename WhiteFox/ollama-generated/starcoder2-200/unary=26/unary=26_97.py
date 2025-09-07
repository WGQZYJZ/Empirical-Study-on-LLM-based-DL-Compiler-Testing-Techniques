
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1)
        negative_slope = 0.75
 
        def leakyrelu(x):
            return torch.where(x < 0, x * negative_slope, x)
 
    def forward(self, x1):
        v1 = self.convT(x1) # Apply pointwise transposed convolution to the input tensor
        mask = (v1 > 0).float()
 
        def f(x):
            return leakyrelu(x) * negative_slope
        v3 = torch.where(mask, v1, f(v1))
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

