
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)
        self.bn = torch.nn.BatchNormXd(...)
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        output = self.bn(self.conv(x1))
        return self.linear(output)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
