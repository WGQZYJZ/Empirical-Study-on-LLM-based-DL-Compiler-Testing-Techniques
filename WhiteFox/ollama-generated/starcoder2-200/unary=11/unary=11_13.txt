
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(32, 16, kernel_size=5)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3
        return torch.clamp_min(v2, 0), torch.clamp_max(v2, 8), v2 / 6


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 4, 5)
__output__, __output__2, __output__3 = m(x1)
