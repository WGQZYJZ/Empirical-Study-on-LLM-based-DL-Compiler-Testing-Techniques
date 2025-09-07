
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.Conv3d(256, 1024)
        bn   = torch.nn.BatchNorm3d()

        output = bn(conv(x1))


# Initializing the model
m = Model()

# Inputs to the model
__input__ = torch.randn(1, 3, 800, 600) # Input should be 4D in this example. But, you may use input with a larger dimensionality for your experiments.

