
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
        self.clamp_min = torch.clamp_min
        self.clamp_max = torch.clamp_max
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.clamp_min(v1, min=kwargs['min'])  # Min clamping value
        v3 = self.clamp_max(v2, max=kwargs['max'])  # Max clamping value
        return v3

# Initializing the model with custom keyword arguments
min_, max_  = torch.tensor([0.5]), torch.tensor([1])
m  = Model(min=min_, max=max_)


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
 
__output__  = m(x1)

