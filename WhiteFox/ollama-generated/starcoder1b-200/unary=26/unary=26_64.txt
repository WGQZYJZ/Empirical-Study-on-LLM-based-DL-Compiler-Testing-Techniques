
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.negative_slope * v1 > 0
        v3 = torch.where(v2, v1, -v1 + self.negative_slope)
        return v3


# Initializing the model
m = Model()


