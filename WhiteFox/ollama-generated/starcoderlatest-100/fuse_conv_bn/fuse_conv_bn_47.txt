
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 2, 3)
        if dim == 1:
            self.bn = torch.nn.BatchNorm1d(2)
        elif dim == 2:
            self.bn = torch.nn.BatchNorm2d(2)
        else:
            self.bn = torch.nn.BatchNorm3d(2)

    def forward(self, x1):
        v1 = torch.nn.functional.conv2d(x1, self.conv.weight, self.conv.bias)
        if x1.ndim == 4 and x1.shape[0] == 1:
            # the shape of input tensor is [bsz, 1, h, w]
            v2 = torch.nn.functional.batch_norm(v1, self.bn.running_mean, self.bn.running_var)
        else:
            # the shape of input tensor is [bsz, n, c, h, w] or [bsz, c, h, w]
            v2 = torch.nn.functional.batch_norm(v1, self.bn.running_mean[None], self.bn.running_var[None])
        return v2

# Initializing the model
m = Model(dim=2)

# Inputs to the model
x1 = torch.randn(1, 2, 4, 4)
