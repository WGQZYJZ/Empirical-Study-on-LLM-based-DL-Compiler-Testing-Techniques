
class ConvBnModel(torch.nn.Module):
    def __init__(self, in_channels: int = 128, out_channels: int = 3):
        super().__init__()

        self._conv = torch.nn.Conv1d(in_channels, out_channels)
        self._bn   = torch.nn.BatchNorm1d(out_channels)

    def forward(self, x):
        return self._bn(torch.nn.functional.conv1d(x, self._conv.weight))


m  = ConvBnModel()
x1 = torch.randn(1024, 3) # Input tensor for the model.
__output__  = m(x1).view(-1)
