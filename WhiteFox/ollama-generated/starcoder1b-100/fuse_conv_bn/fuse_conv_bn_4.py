
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)  # Input dimensions should match with the convolution layers
        self.bn = torch.nn.BatchNorm2d(...)  # Use the conv layer as input and the bn layer as output

    def forward(self, x1):
        output = self.conv(x1)
        return self.bn(output)

# Inputs to the model
input_tensor = ... 
