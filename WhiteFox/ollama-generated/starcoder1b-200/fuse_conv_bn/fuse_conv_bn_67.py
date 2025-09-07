
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvXd(...)
        self.bn   = torch.nn.BatchNormXd(...)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        return self.bn(self.conv(v1))


# Initializing the model
m = Model()

