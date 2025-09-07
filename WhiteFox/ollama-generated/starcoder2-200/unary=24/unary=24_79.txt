
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1) # Apply pointwise convolution with kernel size 1 to the input tensor
 
    def forward(self, x):
        v1 = self.conv(x) 
        v2  = v1 > 0
        v3  = v1 * negative_slope
        v4  = torch.where(v2, v1, v3) # Select elements from t1 or t3 based on the mask t2
        return v4

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
