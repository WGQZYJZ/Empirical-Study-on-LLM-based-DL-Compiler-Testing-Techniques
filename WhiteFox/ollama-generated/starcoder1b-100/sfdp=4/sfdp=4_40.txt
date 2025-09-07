
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.bn1  = torch.nn.BatchNorm2d(8)
        self.conv2 = torch.nn.Conv2d(8, 8, 1)
        self.bn2  = torch.nn.BatchNorm2d(8)
 
    def forward(self, x1):
        v1 = F.relu(self.bn1(self.conv1(x1)))
        v2 = F.relu(self.bn2(self.conv2(v1)))
        return self.conv2(F.max_pool2d(torch.tanh(v2), 2))


# Initializing the model
m = Model()

