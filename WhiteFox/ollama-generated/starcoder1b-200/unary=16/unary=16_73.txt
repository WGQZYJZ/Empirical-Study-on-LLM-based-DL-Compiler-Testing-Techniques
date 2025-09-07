
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 5, stride=1)
        self.bn1  = torch.nn.BatchNorm2d(8)
        self.conv2 = torch.nn.Conv2d(8, 16, 5, stride=1)
        self.bn2  = torch.nn.BatchNorm2d(16)
        self.conv3 = torch.nn.Conv2d(16, 32, 5, stride=1)
        self.bn3  = torch.nn.BatchNorm2d(32)
        self.fc   = torch.nn.Linear(400, 256)
        self.relu = torch.nn.ReLU()
        self.fc2  = torch.nn.Linear(256, 10)
 
    def forward(self, x):
        v = self.bn1(self.conv1(x))
        v = self.relu(v)
        v = self.bn2(self.conv2(v))
        v = self.relu(v)
        v = self.bn3(self.conv3(v))
        v = self.relu(v)
        v = v.view(v.size(0), -1)
        v = self.fc(v)
        v = self.relu(v)
        v = self.fc2(v)
        return v


# Initializing the model
m  = Model()


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
