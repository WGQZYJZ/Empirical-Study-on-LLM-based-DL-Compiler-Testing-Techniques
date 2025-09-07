
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 4)
        self.bn1   = torch.nn.BatchNorm2d(8)
        self.relu1 = torch.nn.ReLU()
 
        self.conv2 = torch.nn.Conv2d(8, 16, 2)
        self.bn2   = torch.nn.BatchNorm2d(16)
        self.relu2 = torch.nn.ReLU()
 
        self.conv3 = torch.nn.Conv2d(16, 32, 1)
        self.bn3   = torch.nn.BatchNorm2d(32)
        self.relu3 = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.bn1(v1)
        v3 = self.relu1(v2)
 
        v4 = self.conv2(v3)
        v5 = self.bn2(v4)
        v6 = self.relu2(v5)
 
        v7 = self.conv3(v6)
        v8 = self.bn3(v7)
        v9 = self.relu3(v8)
        return v9


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 256, 256)
