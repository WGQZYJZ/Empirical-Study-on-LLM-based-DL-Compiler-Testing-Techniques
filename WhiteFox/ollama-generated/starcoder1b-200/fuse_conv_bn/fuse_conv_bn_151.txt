
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def conv1d(x, x_size, stride=1, bias=True, padding=0, dilation=1, groups=1,
               stride_after=False, name='conv1d'):
        # The padding is applied when `stride_after` is False, and the padding is removed otherwise.
        if (padding == 0) or stride_after:
            return nn.Conv1d(x_size, x_size, kernel_size=1, bias=bias)

        def conv_with_padding(x):
            # The input dimension will be (batch_size, in_channels, ... ,in_channels-1), which is the same as Conv2d.
            return nn.Conv1d(in_channels=x.shape[2], out_channels=x_size, kernel_size=1,
                              stride=stride, bias=bias)
        x = conv_with_padding(x)
        if padding == 'same':
            x = torch.nn.functional.pad(x, [0, 0])

        return x

    def forward(self, x):
        # The batch_size and channel dimension of `x` will be (batch_size, in_channels, ... ,in_channels-1),
        # so we need to change the input dimension to (batch_size, out_channels=x.shape[1], ... ,out_channels-1).
        x = self.conv1d(x, x.shape[-1])  # X should match with Conv1d
        return x


# Initializing the model
m = Model()


