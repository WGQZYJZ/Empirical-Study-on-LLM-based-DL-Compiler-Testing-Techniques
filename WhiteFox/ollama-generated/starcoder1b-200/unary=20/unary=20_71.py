
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(16, 32, 4, stride=2, padding=1)
 
    def forward(self, x):
        v = self.conv_transpose(x)
        return v * 0.5


# Initializing the model
m = Model()

# Inputs to the model
__input__ = torch.randn(16, 32, 64, 64)
x = m(__input__)

