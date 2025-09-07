
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvXd(2, 2) # X can be 1, 2, or 3 representing the dimension
        self.bn1 = torch.nn.BatchNormXd(...)  # X should match with ConvXd
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        v = self.conv1(x)
        bn = self.bn1(v)
        return self.relu(bn)

# Inputs to the model
x = torch.randn(1, 2, 2)
