
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(...)  # Batch norm layer should be inserted before ConvNd layers

    def forward(self, x):
        v1 = self.conv1(x)  # Output is fed into batch norm layer and the input of conv layer is bn_output
        return v1


# Input to the model (X can be different in case when ConvNd is inserted before BatchNormNd layers).
x = torch.randn(1, 3, 32, 32)


