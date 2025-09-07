
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        conv = torch.nn.Conv2d(...)
        bn  = torch.nn.BatchNorm2d(...)
        return conv(x) + bn(x)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 40, 80)
