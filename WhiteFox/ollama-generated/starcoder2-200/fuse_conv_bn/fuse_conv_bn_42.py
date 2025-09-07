
class Model(torch.nn.Module):
    def __init__(self, dim1=32, dim2=64):
        super().__init__()

        # conv_layer is 1x1 convolution for this example
        self.conv = torch.nn.ConvXd(dim1, dim2)
        self.bn = torch.nn.BatchNormXd(dim2)

    def forward(self, input):
        return self.bn(self.conv(input))

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1,32)

__output__  = m(x1)

