
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1)

    def forward(self, x):
        v  = self.conv(x) + 3
        return v


# Inputs to the model
x  = torch.randn(64, 8, 64, 64)
