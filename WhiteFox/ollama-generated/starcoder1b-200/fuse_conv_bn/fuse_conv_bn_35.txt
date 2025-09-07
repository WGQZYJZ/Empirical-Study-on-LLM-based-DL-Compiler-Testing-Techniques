
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)
        self.bn   = torch.nn.BatchNormXd(...)

    def forward(self, x1):
        conv_output  = self.conv(x1)
        bn_output    = self.bn(conv_output)
        output       = bn_output
        return output


# Initializing the model
m  = Model()


