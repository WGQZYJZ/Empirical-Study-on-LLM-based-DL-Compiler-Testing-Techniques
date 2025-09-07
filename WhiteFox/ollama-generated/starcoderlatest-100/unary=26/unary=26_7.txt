
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1) > 0
        negative_slope = -2 * math.log((1 + math.sqrt(math.pi)) / (1 - math.sqrt(math.pi)))
        v2 = v1 * negative_slope
        return torch.where(v1, x1, v2)
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
