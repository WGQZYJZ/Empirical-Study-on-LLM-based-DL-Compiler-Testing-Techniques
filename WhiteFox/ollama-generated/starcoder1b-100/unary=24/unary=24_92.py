
class Model(torch.nn.Module):
    def __init__(self, negative_slope=10e-6):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope

    def forward(self, x1):
        mask = (x1 > 0).float()
        v1 = self.conv(x1) * mask
        v2 = torch.where(mask, v1, -self.negative_slope * x1)
        return v2


# Initializing the model
m = Model()
