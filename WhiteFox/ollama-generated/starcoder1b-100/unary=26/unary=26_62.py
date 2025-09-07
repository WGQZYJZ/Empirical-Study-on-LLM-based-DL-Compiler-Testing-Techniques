
class Model(nn.Module):
    def __init__(self, negative_slope: float):
        super().__init__()
        self.conv = nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope

    def forward(self, x: torch.Tensor):
        v1 = F.leaky_relu(self.conv(x)) * -0.5
        v2 = self.conv(v1) * self.negative_slope
        v3 = torch.where(v2 > 0, x, v2)
        return v3


# Initializing the model
m = Model(negative_slope=0.75)


