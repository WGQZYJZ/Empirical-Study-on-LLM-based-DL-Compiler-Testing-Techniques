

class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 > 0
        v3 = v1 * -self.negative_slope

        # Select elements from the output of the convolution or the result of the multiplication based on the mask
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model
negative_slope  =  0.5
m = Model(negative_slope=negative_slope)

# Inputs to the model
x1  =  torch.randn(1, 3, 64, 64) 
