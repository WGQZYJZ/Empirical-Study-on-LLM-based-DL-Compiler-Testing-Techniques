
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.bn1 = nn.BatchNorm2d(8)
        self.conv2 = torch.nn.Conv2d(8, 8, 1)
        self.bn2 = nn.BatchNorm2d(8)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v1 = self.bn1(v1)
        v2 = self.conv2(v1)
        v2 = self.bn2(v2)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
