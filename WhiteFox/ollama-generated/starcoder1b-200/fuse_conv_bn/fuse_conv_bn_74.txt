
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn1 = torch.nn.BatchNormXd(...)  # X should match with ConvXd
        self.conv2 = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn2 = torch.nn.BatchNormXd(...)  # X should match with ConvXd

    def forward(self, x):
        conv_x = self.conv1(x)
        bn_x = self.bn1(conv_x)
        conv_x = self.conv2(conv_x)
        bn_x = self.bn2(conv_x)
        output = bn_x
        return output


# Initializing the model
m = Model()


