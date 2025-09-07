
class Generator(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(16, 8, 4, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        return torch.sigmoid(v1)


# Inputs to the generator
x2 = torch.randn(4, 8, 64, 64)
