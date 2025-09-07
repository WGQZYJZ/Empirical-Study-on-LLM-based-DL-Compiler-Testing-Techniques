
class Model(nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv  = nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1) * self.negative_slope
        v2 = torch.where(v1 > 0, x1, v1 * 0.5) # Apply pointwise convolution with kernel size 1 to the input tensor
        return v2


# Initializing the model
m = Model()

