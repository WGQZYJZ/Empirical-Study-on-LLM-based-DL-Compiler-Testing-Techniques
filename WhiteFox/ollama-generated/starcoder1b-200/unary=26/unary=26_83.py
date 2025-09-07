
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=(1, 64), stride=2)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 > 0).float() * self.negative_slope
        v3 = v1 * (1 - v2)
        return v3


# Initializing the model
m = Model()


