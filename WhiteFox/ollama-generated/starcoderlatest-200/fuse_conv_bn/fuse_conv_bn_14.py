
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        conv = torch.nn.Conv2d(3, 16, 3)
        bn = torch.nn.BatchNorm2d(16)
        output = bn(conv(x))
        return output


# Inputs to the model
x = torch.randn(2, 3, 4, 5)
