
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=2)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = (v1 > 0).float()
        v2 = torch.where(mask, v1, -v1 * self.negative_slope)
        return v2


# Initializing the model
m = Model(-0.039)


