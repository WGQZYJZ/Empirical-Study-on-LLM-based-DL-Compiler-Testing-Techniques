
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3, 8, 5)
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1  = self.convT(x1) # Apply pointwise transposed convolution to the input tensor
        v2  = (v1 > 0).float() 
        v3  = torch.where(v2, v1, -self.negative_slope * v1)   # Apply the where function to select elements from t1 or t3 based on the mask t2
        return v3

# Initializing the model with negative slope
m  = Model(0.45)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

