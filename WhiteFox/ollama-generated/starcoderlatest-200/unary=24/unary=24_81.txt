
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) > 0
        v2 = v1 * -0.05 # Modify the output of the convolution so that negative values become smaller than zero (e.g., set all values to positive and then multiply by negative_slope)
        return v6
 
    def extra_repr(self):
        return 'Negative slope: {}'.format(-0.05)

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
