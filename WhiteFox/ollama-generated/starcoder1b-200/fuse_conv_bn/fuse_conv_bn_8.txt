
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn   = torch.nn.BatchNormXd(...)  # X should match with ConvXd
        self.linear  = torch.nn.Linear(self.bn.num_features, 1)

    def forward(self, x1):
        conv_output = self.conv(x1)
        bn_output   = self.bn(conv_output)
        return self.linear(bn_output)


# Inputs to the model
x1 = torch.randn(1, 2, 3)
