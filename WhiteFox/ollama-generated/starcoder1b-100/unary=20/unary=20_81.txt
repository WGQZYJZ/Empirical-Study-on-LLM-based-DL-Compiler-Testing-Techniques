
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv(x)
        return torch.sigmoid(v1)


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(2, 8, 64, 64)
