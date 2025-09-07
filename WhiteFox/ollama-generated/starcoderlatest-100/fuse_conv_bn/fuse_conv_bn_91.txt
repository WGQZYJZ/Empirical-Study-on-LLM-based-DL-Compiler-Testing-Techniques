
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(...)  # (3, 5) input channel, and 7x7 kernel

    def forward(self, x):
        output = self.conv1(x)   # (2, 2, 60, 80) after conv1, the spatial dimension is reduced from 60*80 to 35*45

        return output


class Model_fapi(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)
        # Note: this will be removed and replaced with the module pattern after fuse conv bn is done
        self.batchnorm = torch.nn.BatchNorm2d(...)

    def forward(self, x):
        output = self.conv1(x)   # (2, 2, 60, 80) after conv1, the spatial dimension is reduced from 60*80 to 35*45
        bn_output = self.batchnorm(bn_input)   # Note: this will be replaced with fuse pattern

        return output


# Initialize the model in module API form
m_fapi = Model()
