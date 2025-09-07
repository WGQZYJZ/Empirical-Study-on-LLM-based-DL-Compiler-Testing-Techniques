
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = torch.where((v1 > 0).float(), v1, (v1 * self.negative_slope)).gt(0)
        return torch.mul(mask, v1)


# Initializing the model
m = Model()


