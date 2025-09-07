
class Model(torch.nn.Module):
    def __init__(self, conv_type="conv2d", bn_type="batch_norm2d"):
        super().__init__()
        self.conv = torch.nn.Conv[conv_type](1, 2, kernel_size=1)
        if bn_type == "batch_norm":
            self.bn = torch.nn.BatchNorm2d(1)

    def forward(self, x):
        y = self.conv(x)
        if self.bn is not None:
            y = self.bn(y)
        return y

# Initializing the model
m = Model(conv_type="Conv3d", bn_type="batch_norm3d")


# Inputs to the model
x1 = torch.randn(1, 2, 2, 4)
