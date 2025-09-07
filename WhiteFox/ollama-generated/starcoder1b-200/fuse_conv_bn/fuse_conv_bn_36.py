
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvXd(...)
        self.bn1  = torch.nn.BatchNormXd(...)
        self.linear = torch.nn.Linear(..., ...)

    def forward(self, x1):
        x2 = self.conv1(x1)
        x3 = self.bn1(x2)
        return self.linear(x3)


# Initializing the model
m  = Model()

