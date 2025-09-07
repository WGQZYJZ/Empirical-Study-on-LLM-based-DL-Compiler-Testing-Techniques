
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 32, kernel_size=4)
        self.bn = torch.nn.BatchNorm2d(32)

    def forward(self, x1):
        x2 = torch.nn.functional.conv2d(x1, self.conv.weight, self.conv.bias, self.conv.stride, self.conv.padding)
        y = torch.nn.functional.batch_norm(x2, self.bn.running_mean, self.bn.running_var, self.bn.eps, True)
        return y
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 1, 28, 28)
