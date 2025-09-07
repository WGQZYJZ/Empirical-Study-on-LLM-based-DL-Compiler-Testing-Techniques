
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise transposed convolution to the input tensor
        mask = v1 > 0 
        v2 = v1 * negative_slope
        v4  = torch.where(mask,v1,v2) # Apply where function for selecting elements from t1 or t3 based on mask.
        return v4


# Initializing model
m  = Model()


# Inputs to the model
x1 = torch.randn(50, 3, 64, 64)


