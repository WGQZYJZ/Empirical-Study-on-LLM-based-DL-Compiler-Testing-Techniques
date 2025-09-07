
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, kernel_size=3, stride=1, padding=1)

    def forward(self, x1):
        m = self.conv(x1)
        mask = x1 > 0
        return torch.where(mask, m, x1 * negative_slope)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
