
class Model(torch.nn.Module):
    def __init__(self,  in_channels = 32, out_channels=64, kernel_size=3):
        super().__init__()

        self._conv1 = nn.ConvNd(in_channels, out_channels, (kernel_size,))

        self._norm1 = nn.BatchNormXd(out_channels)

    def forward(self,  x):
      y = torch.nn.functional.convXd(x, self._conv1, bias=None, stride=2,)
      y = torch.nn.functional.batch_norm(y, momentum=0.56,  affine=True)

      return y

