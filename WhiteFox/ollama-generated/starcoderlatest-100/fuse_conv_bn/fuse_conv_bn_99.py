
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(...)
        self.bn = torch.nn.BatchNorm2d(...)

    def forward(self, x1):
        # Apply the convolution layer followed by batch normalization layer
        out  = self.bn(self.conv1(x1))
        return out


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 8, 8)
