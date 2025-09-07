
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3
        v3  = torch.clamp_min(v2, 0)
        v4  = torch.clamp_max(v3, 6)
        return v4 / 6


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 8, 52978/64, 64)) # this should be a 4-D tensor, whose first dimension is 1

 __output__  = m(x1)
