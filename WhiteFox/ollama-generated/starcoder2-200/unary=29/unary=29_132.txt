
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1) 
        return torch.clamp_min(v1, min_value), torch.clamp_max(torch.clamp_min(v1, min_value), max_value)


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(256, 3, 80, 80)


# Expected output: 
__output__  = m(x1)[0]
