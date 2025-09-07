
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=2)
 
    def forward(self, x):
        v = self.conv(x)
        v = v * (0.5 + 2 * v)
        return v


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 8, 64, 64)
