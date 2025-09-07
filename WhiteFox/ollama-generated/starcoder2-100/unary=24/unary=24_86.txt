
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.15):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = (v1 > 0).float() * v1 # Select elements greater than or equal to zero in the convolution output based on a boolean mask
        v3  = -negative_slope * ((~(v1 < 0)).float() * v1) + v2 # Multiply negative slope by negative mask
        return v3


# Initializing the model with a negative slope of `0.15`
m = Model(-0.15)


