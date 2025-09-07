
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1) # Apply pointwise convolution with kernel size 1 to the input tensor
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 > 0).float() * -negative_slope 
        return torch.where(v1 >= 0., v1, v2)


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
