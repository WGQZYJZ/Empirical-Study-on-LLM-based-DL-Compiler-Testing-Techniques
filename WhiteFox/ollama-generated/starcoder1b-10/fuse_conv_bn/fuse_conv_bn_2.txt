
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn    = torch.nn.BatchNormXd(...) # X should match with ConvXd
        self.linear = torch.nn.Linear(3, 2)

    def forward(self, x1):
        # X is input tensor to the module
        x1 = self.conv(x1)  # fuse conv_bn
        x1 = self.bn(x1)    # fuse batch norm

        # Apply linear transformation using v1
        output = self.linear(x1)
        return output


# Initializing the model
m = Model()


