
class Model(torch.nn.Module):
    def __init__(self, min_value=1., max_value=20.):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.clamp = torch.nn.functional.clamp
        
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.clamp(v1, min_value=min_value, max_value=max_value)
        v3 = self.clamp(v2, min_value=0., max_value=1.)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
