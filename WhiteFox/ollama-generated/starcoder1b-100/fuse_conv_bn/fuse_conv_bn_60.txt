
class Model(torch.nn.Module):
    def __init__(self, ...):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)  # X can be 1 or 3 representing the dimension
        self.bn = torch.nn.BatchNorm2d(...)  # X should match with Conv2d

    def forward(self, input_tensor):
        output = self.bn(self.conv(input_tensor))
        return output


# Initializing the model
m = Model()

