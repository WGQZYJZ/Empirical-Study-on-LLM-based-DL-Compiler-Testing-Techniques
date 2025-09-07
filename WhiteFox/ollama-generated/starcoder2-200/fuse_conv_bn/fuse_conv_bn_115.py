
class ConvBNModel(torch.nn.Module):
    def __init__(self, channels: int) -> None:
        super().__init__()

        self._conv1 = torch.nn.Conv2d(in_channels=3, out_channels=channels, kernel_size=(7, 7))
        self._conv2 = torch.nn.Conv2d(
            in_channels=channels,
            out_channels=channels // 2,
            kernel_size=(1, 3),
            stride=2,
            padding=[0, 1]
        )

        self._batchNorm1 = torch.nn.BatchNorm2d(num_features=channels)

    def forward(self, input: torch.Tensor):
        conv1 = self._conv1(input) # shape should be [N, 3, H, W]
        bn = self._batchNorm1(conv1)

        conv2 = self._conv2(bn) # shape should be [N, 8, 40 / 2 , 56]

        return conv2


m = ConvBNModel(channels=3)
x = torch.randn((16, 3, 96, 78))
out_convBN = m(x) # Shape should be [N, 8, 40 / 2, 56]

