
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvXd(...)
        self.bn    = torch.nn.BatchNormXd(...)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.bn(v1)
        return v2


# Initializing the model
m = Model()
m.eval()  # Set to evaluation mode
