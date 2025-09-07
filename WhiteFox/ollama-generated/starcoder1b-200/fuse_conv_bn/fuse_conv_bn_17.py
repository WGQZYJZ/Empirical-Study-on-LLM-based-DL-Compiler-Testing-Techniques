
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn = torch.nn.BatchNorm2d(...)
        self.linear  = torch.nn.Linear(16, 1)

    def forward(self, x):
        v1 = self.conv(x).permute(0, 2, 3, 1)  # Input must be in the following format: (batch_size, channels, height, width)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Inputs to the model
x = torch.randn(1, 3, 8, 8)  # Input must be in the following format: (batch_size, channels, height, width)
