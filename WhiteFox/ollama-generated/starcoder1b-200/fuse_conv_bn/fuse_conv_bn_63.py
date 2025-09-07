
class Model(torch.nn.Module):
    def __init__(self, x1):
        super().__init__()
        self.conv  = torch.nn.ConvXd(...) # X can be 1, 2, or 3 representing the dimension
        self.bn    = torch.nn.BatchNormXd(...) # X should match with ConvXd
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.bn(v1).linear(self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m = Model(torch.randn(1, 3, 256, 512))


# Inputs to the model
x1  = torch.randn(1, 2, 2)
