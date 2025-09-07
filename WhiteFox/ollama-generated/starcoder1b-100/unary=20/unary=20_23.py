
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(16, 8, kernel_size=3)

    def forward(self, x1):
        return self.conv_transpose(x1) * (1 - 0.5 * self.sigmoid(self.conv(x1)))


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
