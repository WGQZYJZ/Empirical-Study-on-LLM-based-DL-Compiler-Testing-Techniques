
class Model(torch.nn.Module):
    def __init__(self, mode="eval"):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 32, kernel_size=3, padding=0)

        if mode == "train":
            self.bn = torch.nn.BatchNorm2d(32, eps=0.001, momentum=0.95, affine=True)

    def forward(self, x):
        if self.training:
            return self.bn(self.conv(x))
        else:
            return F.conv2d(x, self.conv.weight, None,
                            self.conv.bias, self.conv.stride,
                            padding=0, groups=1)


# Initializing the model with "eval" mode
m = Model("eval")
# Inputs to the model
x = torch.randn(1, 1, 28, 28)
