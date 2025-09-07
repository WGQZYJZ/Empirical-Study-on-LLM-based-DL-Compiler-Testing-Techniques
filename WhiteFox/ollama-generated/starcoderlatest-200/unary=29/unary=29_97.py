
class Model(torch.nn.Module):
    def __init__(self, min=0., max=1.):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(8, 3, 4, stride=4)
        self.min, self.max = min, max
 
    def forward(self, x1):
        t1 = self.conv_t(x1)
        t2 = torch.clamp_min(t1, min_value=self.min)
        t3 = torch.clamp_max(t2, max_value=self.max)
        return t3


# Initializing the model
m = Model(min=0., max=1.)

# Inputs to the model
x1  = torch.randn(1, 8, 64, 64)
