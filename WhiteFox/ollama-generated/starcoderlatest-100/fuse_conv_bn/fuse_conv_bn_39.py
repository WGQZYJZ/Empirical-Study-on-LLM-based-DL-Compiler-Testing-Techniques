
class Model(torch.nn.Module):
    def __init__(self, in_channels=1, out_channels=2):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_channels, out_channels, 3)
        self.bn = torch.nn.BatchNorm2d(out_channels)

    def forward(self, x):
        conv = self.conv(x) # The output of this node is used in the next nodes
        bn = self.bn(conv) # This operation is not triggered
        return bn


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 1, 2, 2)
