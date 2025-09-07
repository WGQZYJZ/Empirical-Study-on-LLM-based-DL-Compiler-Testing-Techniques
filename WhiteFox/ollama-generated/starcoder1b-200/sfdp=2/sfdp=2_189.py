
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.bn1  = torch.nn.BatchNorm2d(8)
        self.pool = torch.nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.conv2 = torch.nn.Conv2d(8, 16, 3, stride=2, padding=1)
        self.bn2  = torch.nn.BatchNorm2d(16)
        self.pool = torch.nn.MaxPool2d(kernel_size=4, stride=2, padding=0)
        self.conv3 = torch.nn.Conv2d(16, 32, 3, stride=2, padding=1)
        self.bn3  = torch.nn.BatchNorm2d(32)
 
    def forward(self, x):
        x  = F.relu(self.bn1(self.conv1(x)))
        x  = self.pool(x)
        x  = F.relu(self.bn2(self.conv2(x)))
        x  = self.pool(x)
        x  = F.relu(self.bn3(self.conv3(x)))
        return x


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
