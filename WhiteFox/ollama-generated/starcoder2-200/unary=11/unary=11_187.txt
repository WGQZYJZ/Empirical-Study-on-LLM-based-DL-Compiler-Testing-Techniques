
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(32, 80, kernel_size=5)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3
        return torch.clamp_min(v2, min=0).clamp_max(6).div_(6)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 80, 45, 45)
__output__  = m(x1)