
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn = torch.nn.BatchNormXd(...)  # X should match with ConvXd
        self.linear = torch.nn.Linear(self.input_channels * 3, ...)

    def forward(self, x):
        if self.training:
            return self.batch_norm(self.conv(x))
        else:
            return self.linear(self.conv(x))


# Initializing the model
m = Model()


