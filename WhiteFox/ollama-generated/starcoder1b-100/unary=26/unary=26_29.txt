
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1) > 0
        v2 = v1 * -1
        v3 = v2 * negative_slope
        return v3


# Inputs to the model
input_tensor = torch.randn(5, 3, 64, 64)
