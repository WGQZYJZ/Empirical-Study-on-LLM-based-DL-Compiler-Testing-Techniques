
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 4)

    def forward(self, x1):
        t1 = self.conv(x1)
        t2 = torch.sigmoid(t1)
        return t2


# Inputs to the model
__input__ = torch.randn(1, 8, 64, 64)
x = Model()
output = x(__input__)

