
class Model(torch.nn.Module):
    def __init__(self, conv_dim: int = 32) -> None:
        super().__init__()
        self.conv = torch.nn.ConvNd(
            in_channels=100, out_channels=conv_dim, kernel_size=(3,) * conv_dim
        )

        self.conv = torch.nn.ConvNd(
            in_channels=512,
            out_channels=self.conv.out_channels // 8, # This is just to make it work on a single channel image input
            groups=self.conv.in_channels,
            kernel_size=(3,) * conv_dim
        )

    def forward(self):
        return self.conv(torch.randn(100))

# Initializing the model
m = Model()

