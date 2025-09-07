
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(...)
        self.bn    = torch.nn.BatchNorm1d(...)

    def forward(self, x):
        # Fuse convolution and batch norm to get the desired tensor
        output = self.bn(self.conv(x))
        return output


# Initializing the model
m = Model()


