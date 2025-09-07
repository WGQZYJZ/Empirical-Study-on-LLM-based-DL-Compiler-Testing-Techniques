
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)
        self.bn   = torch.nn.BatchNorm2d(...)
        self.relu  = torch.nn.ReLU()

    def forward(self, x1):
        output = self.relu(self.bn(self.conv(x1)))
        return output


# Initializing the model
m = Model()


