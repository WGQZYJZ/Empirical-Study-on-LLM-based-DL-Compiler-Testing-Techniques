
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)  # Replace convXd with Conv2d and bnXd with BatchNorm2d
        self.bn   = torch.nn.BatchNorm2d(...)

    def forward(self, x1):
        v1 = self.conv(x1)  # Replace input_tensor with v1 in the above pattern
        output = self.bn(v1)  # Replace v1 with output in the above pattern
        return output

# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(3, 2, 2)
