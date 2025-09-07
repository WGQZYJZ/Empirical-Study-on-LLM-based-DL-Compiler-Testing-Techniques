
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn   = torch.nn.BatchNormXd(...)

    def forward(self, x):
        output = self.bn(self.conv(x))
        return output


# Initializing the model
m = Model()
m.eval()
__output = m(x1)

