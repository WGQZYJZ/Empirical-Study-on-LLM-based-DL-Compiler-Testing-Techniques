
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(...)
        self.bn    = torch.nn.BatchNorm2d(...)

    def forward(self, x1):
        conv_x  = self.conv(input_tensor)
        bn_x    = self.bn(conv_x)
        return bn_x


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3, 4)
