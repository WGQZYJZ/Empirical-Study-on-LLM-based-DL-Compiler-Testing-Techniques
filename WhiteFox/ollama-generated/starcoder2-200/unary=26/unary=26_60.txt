
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = self.conv(x1)
        mask = v1 > 0
        v3 = torch.where(mask, v1, -v2 * v3)


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(8, 5, 64, 64)
