
class Model(torch.nn.Module):
    def __init__(self, in_channels):
        super().__init__()

        # Fuse conv and batch normalization into a single convolution layer
        self.conv = torch.nn.Conv2d(in_channels=in_channels, out_channels=100, kernel_size=(3, 3), stride=1)
        self.bn = torch.nn.BatchNorm2d(num_features=100, eps=0.00100, momentum=0.1, affine=True, track_running_stats=False)

    def forward(self, x):
        output = self.conv(x).mean([1, 3])

        # If the output tensor is used by other nodes, this optimization will not be performed
        return self.bn(output)
# Inputs to the model
in_channels 2
