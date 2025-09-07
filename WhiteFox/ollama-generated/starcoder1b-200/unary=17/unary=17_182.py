
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, kernel_size=1, stride=1, padding=0)
 
    def forward(self, x2):
        v2 = self.conv(x2)
        v3 = v2 * 0.5
        return v3


# Initializing the model
m = Model()


# Inputs to the model
__input__ = torch.randn(1, 8, 64, 64)
x2  = m(__input__)
