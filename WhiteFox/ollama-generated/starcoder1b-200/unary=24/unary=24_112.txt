
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        v = self.conv(x)
        mask = (v > 0) & (v < 5)
        return mask * -4


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
