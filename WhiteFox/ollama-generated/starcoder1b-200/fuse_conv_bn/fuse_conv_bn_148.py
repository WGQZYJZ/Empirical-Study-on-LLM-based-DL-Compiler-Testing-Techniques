
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)
        self.bn  = torch.nn.BatchNormXd(...)

    def forward(self, x1):
        conv  = self.conv(x1)
        bn    = self.bn(conv)
        output = bn(conv)
        return output


# Initializing the model
m = Model()


