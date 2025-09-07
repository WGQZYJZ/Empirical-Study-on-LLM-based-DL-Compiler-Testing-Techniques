
class Model(torch.nn.Module):
    def __init__(self, bn=False):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 10, 3) if not bn else torch.nn.Conv2dBnReLU(1, 10, 3)

    def forward(self, x):
        output = self.conv(x)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 1, 32, 32)
