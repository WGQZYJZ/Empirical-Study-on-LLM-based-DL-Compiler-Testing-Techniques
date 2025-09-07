
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)

    def forward(self, x1):
        output = self.conv(x1)
        return output


class BatchNormModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bn = torch.nn.BatchNorm3d(...)

    def forward(self, x1):
        output = self.bn(x1)
        return output

# Initializing the model
m  = Model()
mbn = BatchNormModel()

# Inputs to the model
x1 = torch.randn(1, 2, 2, 2)
