
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 10, kernel_size=(3, 3), stride=1, padding=1)
        self.bn = torch.nn.BatchNorm2d(10)

    def forward(self, x):
        output = F.relu(self.conv(x))
        output = self.bn(output)
        return output
# Inputs to the model
x = torch.randn(1, 1, 32, 32)
