
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, negative_slope):
        return torch.where(x1 > 0, negative_slope * x1, x1)


# Initializing the model
m = Model()


