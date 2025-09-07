
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 4, stride=2, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return torch.tanh(v1)


# Initializing the model
m = Model()


# Inputs to the model
__input__ = torch.randn(1, 8, 32, 32)
output = m(__input__)