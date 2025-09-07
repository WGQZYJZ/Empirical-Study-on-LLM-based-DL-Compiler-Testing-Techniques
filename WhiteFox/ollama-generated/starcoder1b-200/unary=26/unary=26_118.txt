
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=4, stride=2, padding=1)

    def forward(self, x):
        v = self.conv(x)
        return v


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
