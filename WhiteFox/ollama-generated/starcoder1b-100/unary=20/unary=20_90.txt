
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x):
        t1 = self.conv(x)
        t2 = torch.sigmoid(t1)
        return t2


# Inputs to the model
__input__ = torch.randn(1, 3, 64, 64)
x   = __input__
