
class Model(nn.Module):
    def __init__(self, negative_slope=1):
        super().__init__()
        self.conv = nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x):
        v = self.conv(x)
        mask = (v > 0).type(torch.FloatTensor)
        return self.negative_slope * (mask * (self.conv(x)) + ((1 - mask) * v))


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
