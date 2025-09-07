
class Model(torch.nn.Module):
    def __init__(self, x: torch.Tensor):
        super().__init__()
        self.conv  = torch.nn.functional.conv2d(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn   = torch.nn.BatchNorm2d(...)  # X should match with ConvXd

    def forward(self, x: torch.Tensor):
        return self.bn(self.conv(x))


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
