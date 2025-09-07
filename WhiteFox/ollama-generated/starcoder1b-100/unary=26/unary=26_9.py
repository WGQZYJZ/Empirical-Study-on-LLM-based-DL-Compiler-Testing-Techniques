
class Model(nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.negative_slope = negative_slope
        self.conv = nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1 > 0 * self.negative_slope

# Initializing the model
m = Model()


