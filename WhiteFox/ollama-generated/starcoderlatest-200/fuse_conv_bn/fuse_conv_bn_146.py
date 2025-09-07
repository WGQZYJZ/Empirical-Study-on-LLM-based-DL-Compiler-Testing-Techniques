
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)  # Conv2d or Conv3d can be replaced with ConvNd for higher dimensions

    def forward(self, x1):
        output = self.conv(x1)
        return self.bn(output)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 16, 30, 50)
