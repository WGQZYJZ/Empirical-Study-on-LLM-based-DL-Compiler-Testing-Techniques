
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.3):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 64, 1, stride=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = (v1 > 0).float()
        slope = -negative_slope
        return v1 * slope * mask


# Initializing the model
m = Model(0.3)

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)

# Output of the model
