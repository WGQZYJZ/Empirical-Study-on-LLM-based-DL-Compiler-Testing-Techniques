
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x):
        mask = x > 0
        v1 = self.conv(x, output_padding=1) * self.negative_slope
        v2 = v1 + 1
        return v2


# Initializing the model
m = Model(-2.5)


