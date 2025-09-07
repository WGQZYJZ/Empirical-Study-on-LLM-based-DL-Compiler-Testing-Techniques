
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, kernel_size=1, stride=1, padding=0)
 
    def forward(self, x):
        v = self.conv(x) + 3
        v = torch.clamp(v, 0, 6)
        return v / 6


# Inputs to the model
x  = torch.randn(1, 8, 64, 64)
