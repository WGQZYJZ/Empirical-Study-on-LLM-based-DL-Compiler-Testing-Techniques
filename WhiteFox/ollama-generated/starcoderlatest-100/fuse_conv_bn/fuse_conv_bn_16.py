
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.Conv2d(...)
        bn = torch.nn.BatchNorm2d(...)
        output = bn(conv(input_tensor))
        return output


# Inputs to the model
x1 = torch.randn(1, 3, 28, 28)
