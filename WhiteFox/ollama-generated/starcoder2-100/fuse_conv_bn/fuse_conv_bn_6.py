
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.Conv2d(3, 64, 7)
        bn = torch.nn.BatchNorm2d(64)

        # The fused Conv-BN layer
        conv_bn = conv(x1).relu().add(conv(x1), alpha=0.).relu()
        return conv_bn

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(3, 784)
__output__  = m(x1)

