
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(...)  # X can be 1, 3 or 4 representing the dimension
        self.bn = torch.nn.BatchNorm2d(...)  # X should match with Conv2d

        conv = torch.nn.functional.conv2d(..., ...)
        bn = torch.nn.functional.batch_norm(...)

    def forward(self, x):
        output = self.conv1(x)
        return self.bn(output)


# Inputs to the model
x1 = torch.randn(2, 3, 4, 4)
