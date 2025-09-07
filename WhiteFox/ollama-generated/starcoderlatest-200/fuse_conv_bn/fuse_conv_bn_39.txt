
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 3, 3)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x1):
        conv_output = self.conv(x1)
        bn_output = self.bn(conv_output)
        return bn_output


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(4, 1, 28, 28)
