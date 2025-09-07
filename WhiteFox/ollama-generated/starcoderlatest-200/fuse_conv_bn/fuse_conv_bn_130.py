
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, kernel_size=(5, 5), stride=1)
        self.bn1   = torch.nn.BatchNorm2d(num_features=64)
        self.pool  = torch.nn.MaxPool2d(kernel_size=2)
        self.conv2 = torch.nn.Conv2d(64, 32, kernel_size=(5, 5), stride=1)
        self.bn2   = torch.nn.BatchNorm2d(num_features=32)

    def forward(self, x):
        x = self.pool(F.relu(self.bn1(self.conv1(x))))
        x = F.relu(self.bn2(self.conv2(x)))
        return x


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 30, 45)
