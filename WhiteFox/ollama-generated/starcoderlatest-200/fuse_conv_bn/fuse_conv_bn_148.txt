
class Model(torch.nn.Module):
    def __init__(self, conv=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(...) if conv else None

    def forward(self, x1):
        if self.conv is not None:
            v1 = self.conv(x1)
        else:
            v1 = F.conv2d(...)
        return bn(v1)


class Model_functional(torch.nn.Module):
    def __init__(self, conv=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(...) if conv else None

    def forward(self, x1):
        v1 = F.conv2d(...)
        return F.batch_norm(..., ..., v1)
# Initializing the model
m  = Model(conv=True)

m_functional  = Model_functional(conv=True)

# Inputs to the model
x1 = torch.randn(1, 3, 2, 4)


# The output of `model` and `model_functional` should be same after executing `fuse_bn_conv`. Please check the log below.
