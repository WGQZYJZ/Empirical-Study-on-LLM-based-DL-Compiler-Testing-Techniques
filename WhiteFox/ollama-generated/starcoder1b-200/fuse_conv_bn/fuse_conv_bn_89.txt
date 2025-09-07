
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvXd(...)
        self.bn  = torch.nn.BatchNormXd(...)

    def forward(self, x):
        v = self.conv1(x)
        return self.bn(v)


# Initializing the model
m = Model()


