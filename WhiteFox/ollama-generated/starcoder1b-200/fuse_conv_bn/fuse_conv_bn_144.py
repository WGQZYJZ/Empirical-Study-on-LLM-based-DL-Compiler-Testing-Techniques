
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn = torch.nn.BatchNormXd(...)  # X should match with ConvXd
        self.linear = torch.nn.Linear(3, 2)

    def forward(self, x):
        v1 = self.conv(x).view(-1, 8)  # X can be 1, 2, or 3 representing the dimension
        v2 = self.bn(v1)  # This operation is only applied when in evaluation mode (not training mode), and tracking running statistics
        v3 = torch.nn.functional.linear(v2, self.linear.weight, self.linear.bias)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 4, 5, 8)
