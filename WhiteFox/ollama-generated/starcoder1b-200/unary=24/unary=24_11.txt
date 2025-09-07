
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.where(v1 > 0, v1 * self.negative_slope, torch.zeros(v1.size()))
        return v2


# Initializing the model
m = Model(negative_slope=0.1)


