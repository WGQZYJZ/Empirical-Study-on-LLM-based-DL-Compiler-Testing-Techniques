
class Model(torch.nn.Module):
    def __init__(self, **kwargs)
        self.conv = torch.nn.ConvTranspose2d()
        self.min  = min(kwargs['min'])
        self.max  = max(kwargs['max'])
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min) 
        return torch.clamp_max(v2, self.max)

# Initializing the model with keyword arguments
m = Model(min=[0.4], max=[5])


# Inputs to the model
x1  = torch.randn(1, 8, 3, 3))
__output__  = m(x1)

