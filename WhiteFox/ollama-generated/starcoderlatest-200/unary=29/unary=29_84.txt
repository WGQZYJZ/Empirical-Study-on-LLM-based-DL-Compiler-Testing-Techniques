
class Model(torch.nn.Module):
    def __init__(self, min=0., max=1.):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_t(x1)
        v2 = torch.clamp_min(v1, min=min)
        v3 = torch.clamp_max(v2, max=max)
        return v3

# Initializing the model
m = Model(0., 1.)

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
