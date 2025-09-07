
class ResidualNetwork(nn.Module):
    def __init__(self, num_layers=4):
        super().__init__()
 
        layers = []

        for i in range(num_layers):
            layers.append(nn.Sequential())

            # Each input should have 8 units.
            for _ in range(8):
                layers[-1].add_module("conv_%i" % (i + 1), nn.Conv2d(in_channels=3, out_channels=8, kernel_size=1))

            # We do not use Relu as a nonlinearity here but apply it after the convolution to reduce its
            # complexity and get a feature map of a similar size.
            layers[-1].add_module("relu_%i" % (i + 1), nn.ReLU())

            # The output of each unit must have 8 units so use `upsample` as activation function after the
            # transposed convolution. Each output tensor from the upsampled feature map is multiplied by
            # 2, to give a tensor of twice the size of the input.
            layers[-1].add_module("upsample_%i" % (i + 1), nn.Upsample(scale_factor=2))

            for _ in range(8):
                layers[-1].add_module("conv_%i_relu" % (i + 1), nn.Conv2d(in_channels=8, out_channels=8, kernel_size=1))

        self.network = nn.Sequential(*layers)

    def forward(self, x):
        return self.network(x)

# Initializing the model
model = ResidualNetwork()


