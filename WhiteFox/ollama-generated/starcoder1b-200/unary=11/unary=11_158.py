
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + 3
        return torch.clamp_min(v1, 0), torch.clamp_max(t4, 6), torch.clamp_max(t5, 6)


# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
