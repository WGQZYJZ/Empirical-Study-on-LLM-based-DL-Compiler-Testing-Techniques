
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=2, padding=0)

    def forward(self, x):
        v = self.conv(x).view(-1, 3, 64, 64)
        v = self.conv_transpose(v).view(-1, 3, 1, 1)
        return v


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(2, 3, 32, 32)
