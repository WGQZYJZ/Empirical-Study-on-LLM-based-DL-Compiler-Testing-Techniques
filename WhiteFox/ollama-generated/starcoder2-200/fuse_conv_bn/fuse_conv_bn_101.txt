
class FusedModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 10, kernel_size=(4, 5))

    def forward(self, x):
        # fusing the convolution and batch normalization layers into a single layer
        return conv_bn_fuse(x)


class FusedModel2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 10, kernel_size=(4, 5))

    def forward(self, x):
        # fusing the convolution and batch normalization layers into a single layer with conv_bn_fuse_functional
        return conv_bn_fuse_functional(x)


# Initializing the model
m = FusedModel()
m2 = FusedModel2()

# Inputs to the model
x1  = torch.randn(3, 4, 50, 68) # 3 is the batch size, 4 and 5 are spatial dimensions, and 68 is the number of channels

