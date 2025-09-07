
class Model(torch.nn.Module):
    def __init__(self, bn_track=True):
        super().__init__()
        self.bn = torch.nn.BatchNormXd(16)
        self.conv = torch.nn.ConvXd(2, 4)

    def forward(self, x1):
        v1 = self.conv(x1)
        output = self.bn(v1)
        return output
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 4)
