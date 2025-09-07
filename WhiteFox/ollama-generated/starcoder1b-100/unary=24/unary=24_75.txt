
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x):
        v1 = self.conv(x)
        return v1 * self.negative_slope


# Initializing the model
m = Model(0.25)

# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
