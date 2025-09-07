
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 64, kernel_size=3)
        self.bn = torch.nn.BatchNorm2d(64)

    def forward(self, x1):
        v1 = torch.nn.functional.conv2d(x1, self.conv.weight, self.conv.bias, stride=self.conv.stride, padding=self.conv.padding, dilation=self.conv.dilation, groups=self.conv.groups)
        v2 = torch.nn.functional.batch_norm(v1, self.bn.running_mean, self.bn.running_var, self.bn.num_batches_tracked, self.bn.eps, training=True) 
        return v2
# Inputs to the model
x1 = torch.randn(3, 3, 4, 4)
