
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(3, 8, 1)

    def forward(self, x1):
        return torch.where(x1 > 0, 1 - (x1 ** (-self.negative_slope)), - (x1 ** (-self.negative_slope)))


# Initializing the model
m = Model()

