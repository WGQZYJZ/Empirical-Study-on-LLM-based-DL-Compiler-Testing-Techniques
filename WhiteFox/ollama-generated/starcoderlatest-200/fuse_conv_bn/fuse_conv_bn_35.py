 
class FusedBatchNorm2d(nn.Module):
    def __init__(self, num_features: int, eps: float = 1e-5, momentum: float = 0.1, affine=True):
        super().__init__()
        self.num_features = num_features
        self.eps = eps
        self.momentum = momentum

        if affine:
            self.weight = nn.Parameter(torch.Tensor(self.num_features).fill_(1))
            self.bias = nn.Parameter(torch.Tensor(self.num_features).zero_())
        else:
            self.register_parameter('weight', None)
            self.register_parameter('bias', None)

    def forward(self, x: torch.Tensor):
        return FusedBatchNorm2dFunction.apply(x, self.eps, self.momentum, self.num_features,
                                              self.weight, self.bias if self.bias is not None else None)

    @staticmethod
    def backward(ctx, grad_output):
        return grad_output
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=(7, 7))
        self.bn = FusedBatchNorm2d(num_features=64)

    def forward(self, x):
        return self.bn(self.conv(x))


# Initializing the model and setting training mode on
m = Model()
m.train()

# Inputs to the model
input_tensor = torch.randn(10, 3, 224, 224)
