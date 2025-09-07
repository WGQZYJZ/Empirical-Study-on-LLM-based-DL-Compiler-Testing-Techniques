
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(8)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=2, padding=0)
        self.bn2 = torch.nn.BatchNorm2d(16)
        self.fc1 = torch.nn.Linear(7 * 7 * 16, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = F.max_pool2d(F.relu(x), 2)

        x = self.conv2(x)
        x = self.bn2(x)
        x = F.max_pool2d(F.relu(x), 2)
        x = x.view(-1, 7 * 7 * 16)
        x = F.relu(self.fc1(x))

        return x

# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(1, 3, 80, 80)
