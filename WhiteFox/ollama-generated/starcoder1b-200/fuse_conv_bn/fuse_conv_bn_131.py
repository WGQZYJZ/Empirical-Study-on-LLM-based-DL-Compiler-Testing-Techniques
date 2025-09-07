
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn = torch.nn.BatchNorm2d(...)  # X should match with Conv2d

        # This optimization is triggered when the convolution and batch normalization layers are in evaluation mode (not in training mode),
        # and the batch normalization layer is tracking running statistics. 
        if not self.training:
            self.fuse_conv_bn = True

    def forward(self, x):
        output = self.bn(self.conv(x))  # Fuse the two convolution layers. If the output of the convolution layer is used by other nodes, the optimization will not be performed.
        return output


# Initializing the model
m = Model()


