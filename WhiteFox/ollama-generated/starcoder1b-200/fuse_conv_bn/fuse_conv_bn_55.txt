
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(...)  # X can be 1, 2, or 3 representing the dimension
        self.conv2 = torch.nn.Conv2d(...)  # X should match with Conv2d
        self.bn1   = torch.nn.BatchNorm2d(...)  # X should match with ConvXd and the input of Conv2d
        self.bn2   = torch.nn.BatchNorm2d(...)  # X should match with BatchNormalizationXd, and the input of BatchNormalizationXd
        self.linear = torch.nn.Linear(...)

    def forward(self, x1):
        output1 = self.conv1(x1)
        bn_out = self.bn1(output1)

        output2 = self.conv2(output1)  # X should match with Conv2d and the input of ConvXd.

        output3 = self.bn2(output2)  # X should match with BatchNormalizationXd and the input of BatchNormalizationXd.
        v3 = self.linear(output3)

        return bn_out, v3


# Initializing the model
m = Model()


__output__, __error__ = m(x1)

