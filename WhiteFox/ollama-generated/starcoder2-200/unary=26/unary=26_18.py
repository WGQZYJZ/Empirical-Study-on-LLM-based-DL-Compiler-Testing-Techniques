
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = (v1 > 0).to(dtype=torch.float)
        v3  = v1 * negative_slope
        return torch.where((v1 > 0), v1, v3)


# Initializing the model with negative slope of 0.5 and applying it to a random input tensor
negative_slope = 0.5
m = Model(negative_slope=negative_slope)
x1 = torch.randn(1, 3, 64, 64)
y1 = m(x1)

