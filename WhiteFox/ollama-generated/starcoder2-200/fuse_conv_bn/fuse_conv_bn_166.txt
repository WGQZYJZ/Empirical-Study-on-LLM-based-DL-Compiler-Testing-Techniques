
class Conv2d(torch.nn.Conv2d):
    def __init__(self, in_channels, out_channels, kernel_size, stride=1,
                 padding=0, dilation=1, groups=1, bias=True):
        self.in_channels = in_channels
        self.out_channels = out_channels

        self.kernel_size  = _ntuple(2)(kernel_size)
        self.stride  = _ntuple(2)(stride)
        self.padding  = _ntuple(2)(padding)
        self.dilation  = _ntuple(2)(dilation)
        self.groups  = groups

        if in_channels % groups != 0:
            raise ValueError('in_channels must be divisible by groups')
        self._validate_indices()

    def forward(self, input):
        fused = False
        # ...
        return fused_tensor


class BatchNorm2d(torch.nn.BatchNorm2d):
    def __init__(self, num_features, eps=1e-5, momentum=0.1,
                 affine=True, track_running_stats=True):

        self._num_features = num_features
        self.eps  = eps

    @property
    def num_features(self):
        return self._num_features

    # ...
    # ...

# Initializing the model
conv2d = Conv2d(..., ...)
bnorm = BatchNorm2d(...)


# Inputs to the model: 3-D input tensor.
x1 = torch.randn(10, 5)

# Outputs of the model.
out_of_conv2d = conv2d(x1)
out_of_bnorm  = bnorm(out_of_conv2d)


