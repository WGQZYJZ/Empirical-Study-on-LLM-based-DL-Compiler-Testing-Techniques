
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.125):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 4, stride=4, padding=2)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        t1 = v1 > 0
        negative_slope = 0.125
        t3 = v1 * negative_slope
        v4 = torch.where(t1, t1, t3)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
