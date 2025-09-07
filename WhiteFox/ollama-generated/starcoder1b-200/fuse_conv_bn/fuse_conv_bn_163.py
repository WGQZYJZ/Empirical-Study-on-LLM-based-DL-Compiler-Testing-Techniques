
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn1  = torch.nn.BatchNormXd(...)  # X should match with ConvXd
        self.conv2 = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn2  = torch.nn.BatchNormXd(...)  # X should match with ConvXd

    def forward(self, x):
        output = x.view(-1, x.size(-1))
        output = self.conv1(output)
        output = self.bn1(output)
        output = self.conv2(output)
        output = self.bn2(output)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 1, 4, 5)
