
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(2, 3, 2)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x1):
        conv_output = self.conv(x1).permute(0, 3, 1, 2)
        bn_output   = self.bn(conv_output)

        # The optimization is triggered here:
        return bn_output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4, 8, 12)
