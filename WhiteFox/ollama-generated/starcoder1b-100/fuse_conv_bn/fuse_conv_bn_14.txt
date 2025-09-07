
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)
        self.bn  = torch.nn.BatchNormXd(...)
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        return self.bn(self.conv(self.relu(x1)))


# Initializing the model
m = Model()


