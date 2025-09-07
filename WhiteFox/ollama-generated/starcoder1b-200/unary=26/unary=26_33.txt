
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 4, stride=2, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x):
        v  = self.conv(x)
        v  = torch.where(v > 0, v, -self.negative_slope * (v ** 2))  # Add the neg slope times twice of the absolute values to the elements that are less than 1.
        return v


# Initializing the model
m  = Model()


