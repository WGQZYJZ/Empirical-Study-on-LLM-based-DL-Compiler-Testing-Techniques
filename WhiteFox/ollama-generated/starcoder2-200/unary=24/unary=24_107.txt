
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.leakyrelu = torch.nn.LeakyReLU(negative_slope=0.1)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor 
        v2 = v1 > 0 # Create a boolean mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise 
        v3 = negative_slope * torch.ones_like(v1)
        v4 = v1 + (-torch.where(v2 & torch.isfinite(v1), negative_slope * (1-v1/abs(v1)), -negative_slope * (1-(-negative_slope*v3)))) # Add the result of the multiplication to a negative slope
        return self.leakyrelu(v4)

# Initializing the model with a negative slope of 0.25
negative_slope = 0.25
m  = Model(negative_slope=negative_slope)
 
# Inputs to the model
x1 = torch.randn(8,3,64,64)
 
