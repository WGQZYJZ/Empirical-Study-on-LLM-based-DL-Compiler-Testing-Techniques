
class Model(torch.nn.Module):
    def __init__(self, min_value=0.25, max_value=100.0):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v = self.conv(x)
        return torch.clamp_min(v, min_value), torch.clamp_max(v, max_value)


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)


