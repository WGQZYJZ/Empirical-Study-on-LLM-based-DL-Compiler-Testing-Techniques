
class Model(torch.nn.Module):
    def __init__(self, min_value=-1., max_value=2.):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 4, stride=2, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return torch.clamp_min(v1, min_value), torch.clamp_max(v1, max_value)


# Initializing the model
m = Model(-1., 2.)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
