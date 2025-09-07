
class Generator(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(8, 3, kernel_size=1, stride=1, padding=0)
 
    def forward(self, x6):
        v6 = self.deconv(x6) * 0.5
        return v6


# Inputs to the model
x6 = torch.randn(1, 8, 32, 32)
