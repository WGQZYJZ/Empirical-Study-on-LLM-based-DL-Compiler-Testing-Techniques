
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        return self.conv(x).pow_(0.5).mul_(0.7071067811865476).erf_()


# Inputs to the model
x = torch.randn(2, 3, 32, 32)
