
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.Conv2d(3, 48, kernel_size=7)
        bn = torch.nn.BatchNorm2d(48)
        output = bn(conv(x1))

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 50, 60)
