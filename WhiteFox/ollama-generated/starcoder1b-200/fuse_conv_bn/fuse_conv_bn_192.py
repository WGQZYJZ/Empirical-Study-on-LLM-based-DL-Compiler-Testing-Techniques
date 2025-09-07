
class Module(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(2, 2)

    def forward(self, x1):
        return torch.relu(self.conv_bn(x1))

    # Fuse the conv and bn to a single BN layer
    def conv_bn(self, x):
        return torch.nn.functional.conv2d(x, self.linear.weight, self.linear.bias)


# Inputs to the model
x1 = torch.randn(1, 3, 4, 5)
