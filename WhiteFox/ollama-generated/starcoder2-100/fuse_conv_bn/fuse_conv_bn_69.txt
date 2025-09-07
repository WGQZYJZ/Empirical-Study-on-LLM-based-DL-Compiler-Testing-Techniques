
class Model(torch.nn.Module):
    def __init__(self, conv_dims, bn_dims=None):
        super().__init__()
        self._conv = torch.nn.ConvXd(
            in_channels=32 if conv_dims is None else 1 + sum(conv_dims), 
            out_channels=64 if conv_dims is None else int(prod(conv_dims) / 8.), 
            kernel_size=[7] * len(conv_dims))
        self._bn = torch.nn.BatchNormXd(*([len(conv_dims)] + list(conv_dims)))

    def forward(self, x):
        return self._bn(self._conv(x))


# Initializing the model
m = Model(None)

x1 = torch.randn(10, 32 if conv_dims is None else sum(conv_dims), 32//8 * 7, 48//5 * 9)

# Inputs to the model
x2 = m(x1)

