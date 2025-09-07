
class Model(torch.nn.Module):
    def __init__(self, in_channels=3, out_channels=16):
        super().__init__()

        # Conv
        self._conv = torch.nn.ConvXd(in_channels=in_channels)
        
        # BatchNorm
        self._batchnorm = torch.nn.BatchNormXd(out_channels)

    def forward(self, x):
        return self._batchnorm(self._conv(x))


# Initializing the model
m  = Model()

# Input to the model
x1  = torch.randn(20, 3, 32, 32)

__output__  = m(x1)

