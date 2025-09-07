
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 16, stride=4, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1) > 0
        negative_slope = -0.5
        t3 = v1 * negative_slope
        t4 = torch.where(v1, v2, t3)
        return t4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
