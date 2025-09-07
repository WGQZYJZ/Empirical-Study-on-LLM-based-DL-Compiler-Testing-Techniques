
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) > 0
        v2 = v1 * -1
        v3 = v1 * 2.5
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
