
class Model(nn.Module):
    def __init__(self, negative_slope=1e-05):
        super().__init__()
        self.negative_slope = negative_slope
        self.conv  = nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.where(v1 < self.negative_slope, v1, (v1 - self.negative_slope))
        return v2


# Initializing the model
m = Model()

