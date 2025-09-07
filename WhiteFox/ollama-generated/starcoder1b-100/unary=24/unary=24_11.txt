
class Model(nn.Module):
    def __init__(self, negative_slope: float = 0.25):
        super().__init__()
        self.conv = nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = torch.greater(v1, 0)
        v2 = v1 * negative_slope[mask]
        return torch.where(mask, x1, v2)


# Initializing the model
m = Model()


