
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn1 = torch.nn.BatchNormXd(...)  # X should match with ConvXd
        self.relu = torch.nn.ReLU()  # Apply ReLU function to the input tensor
        self.conv2 = torch.nn.ConvXd(...)

    def forward(self, x):
        v = self.bn1(self.relu(self.conv1(x)))  # X should match with ConvXd
        return self.conv2(v)


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 2, 2)
