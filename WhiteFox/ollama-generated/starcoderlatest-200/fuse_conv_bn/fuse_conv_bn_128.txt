
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 10, kernel_size=3)

    def forward(self, x):
        v = self.conv(x)
        return v


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 1, 28, 28)
