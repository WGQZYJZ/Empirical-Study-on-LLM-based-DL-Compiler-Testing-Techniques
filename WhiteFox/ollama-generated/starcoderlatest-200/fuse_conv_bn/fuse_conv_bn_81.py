
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_channels=3, out_channels=16, kernel_size=4) # X can be 1, 2, or 3 representing the dimension
        self.bn = torch.nn.BatchNorm2d(num_features=16)

    def forward(self, x):
        conv_out = self.conv(x)
        bn_out = self.bn(conv_out)
        return bn_out


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 4, 4)
