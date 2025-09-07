
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.125):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=2, padding=0)
        self.relu = torch.nn.LeakyReLU(negative_slope)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = (v1 > 0).float()
        slope = -self.relu(mask) * self.relu((v1 - 1) / self.relu(mask) + mask)
        t1 = v1 * slope
        return t1

# Initializing the model
m = Model()

 # Inputs to the model
 x1 = torch.randn(4, 3, 64, 64)
 