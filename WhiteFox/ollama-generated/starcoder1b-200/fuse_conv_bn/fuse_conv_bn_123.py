
class Model(torch.nn.Module):
    def __init__(self, x1):
        super().__init__()
        self.conv  = torch.nn.ConvXd(...)
        self.bn    = torch.nn.BatchNormXd(...)
        self.linear = torch.nn.Linear(x1.shape[0], 2)

    def forward(self, x1):
        conv_out = self.conv(x1)
        bn_out   = self.bn(conv_out)
        return self.linear(bn_out)


# Initializing the model
m = Model(torch.randn(1, 2, 2))


# Inputs to the model
x1  = torch.randn(1, 2, 2)
