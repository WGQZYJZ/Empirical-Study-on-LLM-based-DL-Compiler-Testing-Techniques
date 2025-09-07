
class Model(torch.nn.Module):
    def __init__(self, max_value=1000., min_value=-20):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min_value=-20.) # Clamp the minimum value of -20 to -inf
        v3  = torch.clamp_max(v2, max_value=1000.) # Clamp the maximum value of 1000 to +inf
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
