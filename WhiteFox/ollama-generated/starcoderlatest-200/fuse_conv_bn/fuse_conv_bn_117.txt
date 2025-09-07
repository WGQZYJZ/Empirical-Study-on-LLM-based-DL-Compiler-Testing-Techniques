
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 32, kernel_size=5)
        self.bn1   = torch.nn.BatchNorm2d(32)

    def forward(self, x1):
        output = self.bn1(self.conv1(x1))
        return output


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(1, 1, 48, 64)
