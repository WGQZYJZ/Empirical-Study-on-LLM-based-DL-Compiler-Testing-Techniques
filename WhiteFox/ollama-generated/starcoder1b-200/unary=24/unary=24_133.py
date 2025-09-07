
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = self.conv(x1) * (self.negative_slope + 1e-5) # 0.2 or -1.2 for example
        return v1


# Initializing the model
m = Model()

