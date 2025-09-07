
class Model(torch.nn.Module):
    def __init__(self, n_channel=32, num_classes=1000):
        super().__init__()

        self.model = torch.nn.Sequential(
            torch.nn.ConvTranspose2d(n_channel, n_channel // 4, kernel_size=(1, 5), stride=2, padding=(0, 2)), # Apply pointwise transposed convolution to the input tensor
            torch.nn.LeakyReLU(),

            torch.nn.ConvTranspose2d(n_channel // 4, n_channel // 8, kernel_size=3, stride=1, padding=0), # Apply pointwise transposed convolution to the previous layer's output and add a `conv1x1` layer
            torch.nn.LeakyReLU(),

            torch.nn.Conv2d(n_channel // 8, num_classes, kernel_size=(3,5), stride=1, padding=0) # Apply pointwise convolution to the previous layer's output
        )

    def forward(self, x):
        return self.model(x)

m = Model()

