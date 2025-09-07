
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 2, kernel_size=(1,2), stride=1, padding=0)
        self.bn = torch.nn.BatchNorm2d(2, affine=False)

    def forward(self, x):
        conv_out = self.conv(x)
        bn_out = self.bn(conv_out)

        return bn_out


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 4, 5)
