
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn   = torch.nn.BatchNormXd(...)  # X should match with ConvXd
        self.fc   = torch.nn.Linear(...)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        x = self.fc(x)
        return x


# Initializing the model
m = Model()


