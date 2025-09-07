
class Model(torch.nn.Module):
    def __init__(self, negative_slope: float = 1.0):
        super().__init__()
        self.conv   = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.neg_slope = negative_slope

    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 * self.negative_slope
        v3 = v2 > 0
        v4 = v3 * self.negative_slope + v1
        return v4


# Initializing the model
m = Model()


