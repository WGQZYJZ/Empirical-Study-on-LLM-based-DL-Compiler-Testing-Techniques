
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 > 0).type(torch.float) # Boolean mask
        v3 = v1 * self.negative_slope # Multiplication by negative slope
        v4 = torch.where(v2, v1, v3) # If condition is true: Output of convolution, if condition is false: Negative slope from where the element was picked
        return v4


# Initializing the model with negative_slope=0.05
m = Model(negative_slope=0.05)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
