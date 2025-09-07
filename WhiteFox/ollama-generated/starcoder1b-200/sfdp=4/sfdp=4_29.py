
class Model(torch.nn.Module):
    def __init__(self, dim=512, depth=64):
        super().__init__()
        self.layers = torch.nn.Sequential()

        # Encoder layers
        for i in range(depth):
            self.layers.add_module("layer-{}.conv".format(i + 1), torch.nn.Conv2d(dim, dim * 4, kernel_size=3, stride=2, padding=1))
            self.layers.add_module("layer-{}.norm1".format(i + 1), torch.nn.BatchNorm2d(dim * 4))
            self.layers.add_module("layer-{}.relu".format(i + 1), torch.nn.ReLU(inplace=True))
            self.layers.add_module("layer-{}.norm2".format(i + 1), torch.nn.BatchNorm2d(dim * 4))

        # Decoder layers
        for i in range(depth - 1, -1, -1):
            self.layers.add_module("layer-{}.conv".format(i + 1), torch.nn.ConvTranspose2d(dim * 4, dim, kernel_size=3, stride=2, padding=1))
            self.layers.add_module("layer-{}.norm1".format(i + 1), torch.nn.BatchNorm2d(dim))
            self.layers.add_module("layer-{}.relu".format(i + 1), torch.nn.ReLU(inplace=True))
            self.layers.add_module("layer-{}.norm2".format(i + 1), torch.nn.BatchNorm2d(dim))

        # Final layer
        self.layers.add_module("final.conv", torch.nn.Conv2d(dim, dim, kernel_size=3, stride=1, padding=1))
        self.layers.add_module("final.norm", torch.nn.BatchNorm2d(dim))

    def forward(self, x):
        return self.layers(x)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
