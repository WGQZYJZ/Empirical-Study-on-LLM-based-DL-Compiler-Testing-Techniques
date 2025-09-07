
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 5, stride=2, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model with a minimum value of 0.5 and a maximum value of 1.
m = Model(min_value=0.5, max_value=1.)

# Inputs to the model
x1 = torch.randn(1, 8, 32, 32)
