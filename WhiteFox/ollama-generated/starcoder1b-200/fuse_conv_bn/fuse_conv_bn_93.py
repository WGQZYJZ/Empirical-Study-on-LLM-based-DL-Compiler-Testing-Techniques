
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn = torch.nn.BatchNormXd(...)  # X should match with ConvXd

        # This is equivalent to:
        # self.linear  = torch.nn.Linear(2, 2)
        # self.conv    = torch.nn.Conv1d(...)
        # self.conv_bn = torch.nn.Sequential(self.conv, self.bn)

    def forward(self, x):
        v = x.permute(0, 2, 1)
        b = torch.relu(self.conv(v))
        b = self.bn(b)
        return b


# Initializing the model
m = Model()


