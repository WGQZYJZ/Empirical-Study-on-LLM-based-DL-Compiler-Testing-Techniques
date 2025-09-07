
class Model(torch.nn.Module):
    def __init__(self, negative_slope=1):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) > 0
        v2 = v1 * negative_slope
        v3 = v1 * negative_slope
        v4 = torch.where(v2, x1, v3)
        return v4


# Initializing the model
m = Model()

