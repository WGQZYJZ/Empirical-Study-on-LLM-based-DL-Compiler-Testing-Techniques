
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(8, 3, 5)
 
    def forward(self, x1):
        v1 = self.deconv(x1)
        v2 = torch.clamp_min(v1, min_value=0.)
        v3 = torch.clamp_max(v2, max_value=1.)
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(8, 8, 64, 64)
