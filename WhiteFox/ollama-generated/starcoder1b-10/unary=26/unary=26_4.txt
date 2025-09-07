
class Model(nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv  = nn.Conv2d(3, 8, 1) # We have a convolution layer with kernel size 1
        self.negative_slope = negative_slope
 
    def forward(self, x):
        # We first run a convolution and select the element of the output that is larger than zero.
        v1 = F.leaky_relu(self.conv(x), negative_slope=self.negative_slope)
        # Next we multiply each element in the selected mask by this number.
        v2 = v1 * -0.7071067811865476
        # Then we run another convolution with a mask that selects elements from t1 or t3.
        v3 = F.leaky_relu(self.conv(x), negative_slope=self.negative_slope)
        return v2 * -0.5 + v3


# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
