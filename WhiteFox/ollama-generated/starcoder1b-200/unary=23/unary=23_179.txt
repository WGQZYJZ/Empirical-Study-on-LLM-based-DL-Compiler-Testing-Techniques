
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x2):
        v1 = self.conv(x2)
        return v1


# Initializing the model
m = Model()
__input__ = torch.randn(1, 8, 64, 64)
v2 = m(__input__)
