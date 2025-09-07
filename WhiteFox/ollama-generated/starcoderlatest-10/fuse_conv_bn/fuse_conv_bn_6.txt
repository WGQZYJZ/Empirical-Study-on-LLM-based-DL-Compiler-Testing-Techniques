
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        bn = torch.nn.BatchNorm2d(...)
        conv = torch.nn.Conv2d(...)
        output = bn(conv(x1))
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 20, 5)
