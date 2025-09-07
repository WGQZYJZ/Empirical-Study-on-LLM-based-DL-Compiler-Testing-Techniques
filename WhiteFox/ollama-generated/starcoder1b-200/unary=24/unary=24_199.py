
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1) * self.negative_slope
        v2 = v1 > 0
        return torch.where(v2, x1, x1 * negative_slope)


# Initializing the model
m = Model()

