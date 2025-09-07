
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...) # X can be 1, 2, or 3 representing the dimension
        self.bn   = torch.nn.BatchNormXd(...) # X should match with ConvXd

    def forward(self, x1):
        conv_out = self.conv(x1)
        bn_out   = self.bn(conv_out)
        return bn_out


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
