 2
class FusedBatchNorm(torch.nn.Module):
    def __init__(self, n_features: int, eps: float = 1e-5, momentum: float = 0.9, affine: bool = True):
        super().__init__()
        self.gamma = torch.nn.Parameter(torch.ones(n_features)) if affine else None

    def forward(self, x):
        return FusedBatchNormFunction.apply(x, self.gamma)


class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)
        self.bn  = FusedBatchNorm(...)

    def forward(self, input_tensor):
        output1 = self.conv(input_tensor) # convolution layer that is tracked in the batch norm layer
        output2 = self.bn(output1)     # batchnorm layer
        return output2
