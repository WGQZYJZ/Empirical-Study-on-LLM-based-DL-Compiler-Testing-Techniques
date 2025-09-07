
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(2, 6, kernel_size=(3, 3))
        self.bn1 = torch.nn.BatchNorm2d(6)
        self.maxpool = torch.nn.MaxPool2d((2, 2), stride=2)

    def forward(self, x):
        output = self.conv1(x)
        output = self.bn1(output)
        output = self.maxpool(output)
        return output

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 2, 3, 3)
