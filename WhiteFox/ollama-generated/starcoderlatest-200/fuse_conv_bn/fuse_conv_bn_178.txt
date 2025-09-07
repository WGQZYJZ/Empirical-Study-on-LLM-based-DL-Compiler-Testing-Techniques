
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 5, 2)

    def forward(self, x):
        x = self.conv1(x) # conv1 is removed from the graph after fuse_conv_bn optimization
        return x

# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(1, 3, 28, 28)
