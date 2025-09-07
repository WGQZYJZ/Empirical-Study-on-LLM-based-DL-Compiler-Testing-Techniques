
class Model(torch.nn.Module):
    def __init__(self, ...):
        super().__init__()
        self.conv = torch.nn.ConvNd(...)
        self.bn = torch.nn.BatchNormNd(...)

    def forward(self, x1):
        conv_output = self.conv(x1)
        bn_output   = self.bn(conv_output)
        return bn_output


# Initializing the model
m = Model()


