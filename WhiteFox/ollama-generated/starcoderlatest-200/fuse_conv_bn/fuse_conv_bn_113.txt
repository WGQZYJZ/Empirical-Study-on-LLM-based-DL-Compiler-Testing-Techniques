
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 10, kernel_size=(3, 3))
        self.batch_norm1 = torch.nn.BatchNorm2d(10)
        self.maxpool = torch.nn.MaxPool2d((2,2))

    def forward(self, x):
        # Use conv2d layer instead of convXd to generate the valid pattern
        # conv2d is used instead of ConvXd for consistency with FusionOptimizer which does not support ConvXd yet
        # See Note [ConvXD in PyTorch] section in Convolutional Neural Network.md for details
        # The model should also be different from the previous one
        x = self.conv1(x)
        x = self.batch_norm1(x)
        return self.maxpool(x)


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 1, 28, 28)
