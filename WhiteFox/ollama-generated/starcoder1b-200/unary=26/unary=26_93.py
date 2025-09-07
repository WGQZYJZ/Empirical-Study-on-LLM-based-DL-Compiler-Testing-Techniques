
class Model(nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv  = nn.ConvTranspose2d(3, 8, 1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        mask = torch.abs(x1) >= 0.5
        v1 = self.conv(x1 * mask)
        v2 = (v1 - 0.5) * self.negative_slope
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
