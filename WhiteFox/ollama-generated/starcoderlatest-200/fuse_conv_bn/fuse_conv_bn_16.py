
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)  # (1, 2) or (2, 3) or (3, 2), the dimension can be any combination of {1, 2, 3}
        self.bn = torch.nn.BatchNorm2d(...)  # (1, 2)

    def forward(self, x1):
        output = self.conv(x1)
        output = self.bn(output)
        return output


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(32, 1, 28, 28)
