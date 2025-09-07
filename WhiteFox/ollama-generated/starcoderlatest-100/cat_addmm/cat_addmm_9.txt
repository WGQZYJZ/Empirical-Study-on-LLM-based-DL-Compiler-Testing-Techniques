
class Model(torch.nn.Module):
    def __init__(self, n_conv=2, kernel_size=3, stride=2, padding=1):
        super().__init__()
        self.n_conv = n_conv
        for _ in range(n_conv):
            setattr(self, 'layer{}'.format(_+1), torch.nn.Conv2d(in_channels=3, out_channels=8, kernel_size=kernel_size, stride=stride, padding=padding))

    def forward(self, x):
        for _ in range(self.n_conv):
            getattr(self, 'layer{}'.format(_+1))(x)
            x = getattr(self, 'layer{}'.format(_+1))(x)
        return x


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
