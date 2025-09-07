
class Model(torch.nn.Module):
    def __init__(self, min_value=-10, max_value=256):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min_value=min_value)
        v3  = torch.clamp_max(v2, max_value=max_value)
        return v3


# Initializing the model
m  = Model(min_value=-5, max_value=4096)
 
# Inputs to the model
x1  = torch.randn(1, 3, 728, 728)
__output__  = m(x1)